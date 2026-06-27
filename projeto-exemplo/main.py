"""Orquestrador do relatório semanal: dados → resumo (LLM) → WhatsApp.

Rode com:  python main.py
Agende com GitHub Actions (.github/workflows/semanal.yml) ou cron local.
"""

from __future__ import annotations

from coleta import coletar_semana
from resumo import RelatorioSemanal, resumir
from whatsapp import enviar_mensagem

try:
    # Em execução local, carrega o .env. Em CI, as chaves vêm dos secrets.
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def formatar_mensagem(relatorio: RelatorioSemanal) -> str:
    """Monta a mensagem do WhatsApp a partir do schema (negrito = *asteriscos*)."""
    linhas = [f"*{relatorio.titulo}*", ""]
    linhas += [f"• {b}" for b in relatorio.bullets]
    linhas += ["", f"📌 Destaque: {relatorio.numero_destaque}"]
    if relatorio.alerta:
        linhas += ["", f"⚠️ {relatorio.alerta}"]
    return "\n".join(linhas)


def main() -> None:
    print("[main] coletando dados da semana...")
    dados = coletar_semana()
    if not dados:
        print("[main] sem dados na janela — nada a enviar.")
        return

    print("[main] resumindo com o LLM...")
    relatorio = resumir(dados)

    mensagem = formatar_mensagem(relatorio)
    print("[main] mensagem montada:\n" + mensagem)

    print("[main] enviando pelo WhatsApp...")
    enviar_mensagem(mensagem)
    print("[main] concluído ✅")


if __name__ == "__main__":
    main()
