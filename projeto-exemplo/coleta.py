"""Coleta dos dados da semana.

Genérico e configurável: a fonte é uma URL que devolve JSON (definida em FONTE_URL,
no .env). O padrão é uma série do SGS/BCB, mas troque a URL e a função de recorte
para qualquer API pública, planilha ou banco.
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def _sessao_com_retry() -> requests.Session:
    """Sessão HTTP com retry e backoff exponencial (resiliente a falhas de rede)."""
    sessao = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    sessao.mount("https://", HTTPAdapter(max_retries=retry))
    return sessao


def coletar_semana(dias: int = 7) -> list[dict]:
    """Busca os dados dos últimos `dias` na fonte configurada.

    Retorna uma lista pequena de dicts já filtrada pela janela de tempo. Mantemos
    o resultado enxuto de propósito: menos tokens no resumo, mais sinal.
    """
    url = os.environ.get(
        "FONTE_URL",
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json",
    )

    sessao = _sessao_com_retry()
    try:
        resposta = sessao.get(url, timeout=30)
        resposta.raise_for_status()
        dados = resposta.json()
    except (requests.RequestException, ValueError) as erro:
        # Não derrubamos o programa: devolvemos vazio e quem chama decide.
        print(f"[coleta] falha ao buscar dados: {erro}")
        return []

    # --- Recorte da semana (adapte ao formato da SUA fonte) ---
    # O SGS devolve [{"data": "dd/mm/aaaa", "valor": "..."}]. Filtramos a janela.
    corte = datetime.now() - timedelta(days=dias)
    recorte: list[dict] = []
    for item in dados if isinstance(dados, list) else []:
        try:
            data = datetime.strptime(item["data"], "%d/%m/%Y")
        except (KeyError, ValueError):
            continue
        if data >= corte:
            recorte.append(item)

    # Fallback: se a série for de baixa frequência e nada caiu na janela,
    # leva os últimos registros para o resumo não vir vazio.
    if not recorte and isinstance(dados, list) and dados:
        recorte = dados[-5:]

    print(f"[coleta] {len(recorte)} registros na janela de {dias} dias")
    return recorte


if __name__ == "__main__":
    from pprint import pprint

    pprint(coletar_semana())
