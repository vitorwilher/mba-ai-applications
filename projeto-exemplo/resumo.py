"""Resumo dos dados com um LLM, em saída estruturada.

Usa a API da Anthropic forçando uma ferramenta (tool) cujo input_schema é o nosso
schema Pydantic. Assim o modelo é obrigado a devolver SEMPRE os mesmos campos —
nada de parsing frágil de prosa.

REGRA DE OURO: o modelo só pode usar números presentes nos dados. Nunca inventar.
"""

from __future__ import annotations

import json
import os

import anthropic
from pydantic import BaseModel, Field

MODELO = "claude-haiku-4-5"

INSTRUCOES_SISTEMA = (
    "Você é um analista de negócios. Resuma os dados da semana em português, "
    "com linguagem executiva e direta. REGRA DE OURO: use SOMENTE números que "
    "aparecem nos dados fornecidos — nunca invente valores. Se algo não estiver "
    "nos dados, não afirme."
)


class RelatorioSemanal(BaseModel):
    """Schema do relatório — os campos viram a mensagem do WhatsApp."""

    titulo: str = Field(description="Título curto do relatório da semana")
    bullets: list[str] = Field(description="3 a 5 pontos-chave, objetivos")
    numero_destaque: str = Field(description="O número mais importante da semana, com unidade")
    alerta: str | None = Field(default=None, description="Risco ou alerta, se houver; senão null")


def resumir(dados: list[dict]) -> RelatorioSemanal:
    """Gera o RelatorioSemanal a partir dos dados coletados."""
    cliente = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    ferramenta = {
        "name": "registrar_relatorio",
        "description": "Registra o relatório semanal estruturado.",
        "input_schema": RelatorioSemanal.model_json_schema(),
    }

    resposta = cliente.messages.create(
        model=MODELO,
        max_tokens=1024,
        temperature=0,
        system=INSTRUCOES_SISTEMA,
        tools=[ferramenta],
        tool_choice={"type": "tool", "name": "registrar_relatorio"},
        messages=[
            {
                "role": "user",
                "content": (
                    "Dados da semana (JSON):\n"
                    + json.dumps(dados, ensure_ascii=False)
                    + "\n\nGere o relatório semanal."
                ),
            }
        ],
    )

    # O bloco tool_use traz o input já validado contra o schema.
    for bloco in resposta.content:
        if bloco.type == "tool_use":
            return RelatorioSemanal.model_validate(bloco.input)

    raise RuntimeError("O modelo não retornou o relatório estruturado.")


if __name__ == "__main__":
    from coleta import coletar_semana

    print(resumir(coletar_semana()).model_dump_json(indent=2))
