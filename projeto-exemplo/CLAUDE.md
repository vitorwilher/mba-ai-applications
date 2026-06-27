# CLAUDE.md — Projeto-exemplo: relatório semanal no WhatsApp

## Objetivo

Automação que, toda semana, **coleta** dados de uma fonte, **resume** com um LLM em
linguagem de negócio e **envia** o resumo pelo **WhatsApp**. É a fase de **Implantação**
do CRISP-DM virando produto.

## Fontes e ferramentas

- **Dados:** uma URL JSON configurável (`FONTE_URL` no `.env`). Padrão: série SGS/BCB.
- **LLM:** Anthropic (`claude-haiku-4-5`) com **saída estruturada** (schema Pydantic).
- **Entrega:** Meta WhatsApp Cloud API (Graph API).
- **Agendamento:** GitHub Actions (`.github/workflows/semanal.yml`) ou cron local.

## Módulos

- `coleta.py` — `coletar_semana()` busca e recorta os dados da janela.
- `resumo.py` — `resumir()` devolve um `RelatorioSemanal` (Pydantic) via LLM.
- `whatsapp.py` — `enviar_mensagem()` envia texto livre, com fallback para template.
- `main.py` — orquestra os três e formata a mensagem.

## Regra de ouro

**Nunca inventar número.** O LLM só pode usar valores presentes nos dados coletados.
Isso está reforçado no `INSTRUCOES_SISTEMA` de `resumo.py`.

## Segredos

Chaves **só** no `.env` (no `.gitignore`). Em CI, vêm dos *secrets* do repositório.
Nunca versionar `.env`.
