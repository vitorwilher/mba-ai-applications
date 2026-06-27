"""Envio pela Meta WhatsApp Cloud API (Graph API).

Credenciais lidas do ambiente (.env):
- WHATSAPP_TOKEN            token de acesso
- WHATSAPP_PHONE_NUMBER_ID  ID do número remetente (da conta WhatsApp Business)
- WHATSAPP_DESTINO          número que recebe (DDI+DDD+número, só dígitos)

Observação sobre a janela de 24h: a Cloud API só permite mensagem de TEXTO LIVRE
se o destinatário falou com você nas últimas 24h. Fora disso, é preciso um
TEMPLATE aprovado (ex.: o template de teste `hello_world`).
"""

from __future__ import annotations

import os

import requests

VERSAO_API = "v21.0"


def _url() -> str:
    phone_id = os.environ["WHATSAPP_PHONE_NUMBER_ID"]
    return f"https://graph.facebook.com/{VERSAO_API}/{phone_id}/messages"


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ['WHATSAPP_TOKEN']}",
        "Content-Type": "application/json",
    }


def _enviar(payload: dict) -> requests.Response:
    resposta = requests.post(_url(), headers=_headers(), json=payload, timeout=30)
    return resposta


def enviar_mensagem(texto: str) -> dict:
    """Envia `texto` como mensagem de texto livre; cai para template se falhar."""
    destino = os.environ["WHATSAPP_DESTINO"]

    payload_texto = {
        "messaging_product": "whatsapp",
        "to": destino,
        "type": "text",
        "text": {"body": texto},
    }

    resposta = _enviar(payload_texto)
    if resposta.status_code == 200:
        print("[whatsapp] mensagem de texto enviada")
        return resposta.json()

    # Provável janela de 24h fechada → tenta um template aprovado.
    print(f"[whatsapp] texto livre falhou ({resposta.status_code}); tentando template")
    payload_template = {
        "messaging_product": "whatsapp",
        "to": destino,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    resposta = _enviar(payload_template)
    if resposta.status_code == 200:
        print("[whatsapp] template enviado (configure um template próprio para produção)")
        return resposta.json()

    raise RuntimeError(f"Falha ao enviar WhatsApp: {resposta.status_code} {resposta.text}")


if __name__ == "__main__":
    enviar_mensagem("Teste do projeto-exemplo ✅")
