# MBA — AI Applications

Materiais da disciplina **AI Applications** (MBA, módulo 13) — um laboratório aplicado que
conecta **ML + LLMs + dados + automação** a valor de negócio, usando o **Claude Code** como
agente que escreve, roda e versiona os projetos.

**Professor:** Vítor Wilher — Análise Macro

## 📊 Apresentação da Aula 4

A apresentação de fechamento (slides reveal.js) está publicada no GitHub Pages:

➡️ **<https://vitorwilher.github.io/mba-ai-applications/>**

Ela cobre, em três partes:

1. **CRISP-DM aplicada a agentes de IA** — revisão do método via projeto *Sentimento COPOM*
2. **Setup do ambiente** — VS Code + Python + Claude Code + Quarto + LaTeX
3. **Projeto-exemplo** — relatório semanal automático no **WhatsApp**

## 📁 Conteúdo do repositório

| Arquivo | O que é |
|---|---|
| [`ementa.md`](ementa.md) | Ementa completa da disciplina (4 encontros) |
| [`index.qmd`](index.qmd) | Fonte da apresentação da Aula 4 |
| [`trabalho-final.md`](trabalho-final.md) | Enunciado e rubrica do trabalho final |
| [`projeto-exemplo/`](projeto-exemplo/) | Skeleton: relatório semanal → WhatsApp Cloud API |
| [`CLAUDE.md`](CLAUDE.md) | Briefing do repositório para o Claude Code |

## 🛠️ Como renderizar a apresentação

Pré-requisitos: [Quarto](https://quarto.org) ≥ 1.4 (e LaTeX via `quarto install tinytex`
para saída PDF).

```bash
quarto preview index.qmd   # preview ao vivo
quarto render              # gera docs/index.html (self-contained)
```

O GitHub Pages serve a pasta [`docs/`](docs/) na branch `main`.

## 🔗 Referência

Projeto base usado na revisão de método: **Sentimento COPOM** —
<https://vitorwilher.github.io/anthropic-academy-cursos/projetos/sentimento-copom/slides.html>

---

*Análise Macro — Ciência de Dados aplicada à Economia e ao Mercado Financeiro.*
