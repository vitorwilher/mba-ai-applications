# CLAUDE.md — MBA AI Applications

Briefing do repositório para o Claude Code. Leia antes de editar qualquer arquivo.

## O que é este repositório

Materiais da disciplina **AI Applications** (MBA, módulo 13), ministrada por
**Vítor Wilher — Análise Macro**. A disciplina é um **laboratório aplicado**: conecta
tecnologia (ML + LLMs + dados + automação) a **valor entregue para o negócio**, usando
o **Claude Code** como agente que escreve, roda e versiona o projeto.

Este repositório contém **a 4ª e última aula** (apresentação de fechamento) e os
documentos da disciplina: ementa, enunciado do trabalho final e um projeto-exemplo
completo de automação (relatório semanal via WhatsApp).

## Estrutura

```
.
├── CLAUDE.md            # este briefing
├── README.md           # porta de entrada do repositório
├── ementa.md           # ementa completa da disciplina (4 encontros)
├── index.qmd           # APRESENTAÇÃO da Aula 4 (slides reveal.js)
├── trabalho-final.md   # enunciado e rubrica do trabalho final
├── theme-am.scss       # tema visual da Análise Macro (reveal.js)
├── _quarto.yml         # projeto Quarto → renderiza para docs/
├── assets/             # logo, ilustrações SVG, imagem da ementa original
├── skill-paper-am/     # skill Claude Code: template de paper Quarto+LaTeX + exemplo
├── projeto-exemplo/    # skeleton: relatório semanal → WhatsApp Cloud API
└── docs/               # saída renderizada (GitHub Pages serve daqui)
```

## A apresentação da Aula 4 (`index.qmd`)

Apresentação reveal.js (Quarto), no **mesmo estilo do projeto Sentimento COPOM**
(`vitorwilher/anthropic-academy-cursos`). Tema `theme-am.scss`, logo Análise Macro,
slides de seção com fundo `#1c2d4f` e **caixas de PROMPT** (`::: {.prompt}`) com texto
colável no Claude Code. Três partes:

1. **CRISP-DM aplicada a agentes de IA** — recapitula a metodologia vista no projeto
   COPOM, por repetição, para fixar o mapa mental do aluno.
2. **Setup do ambiente** — instalar VS Code, Python, a extensão do Claude Code dentro do
   VS Code, e integrar Quarto + LaTeX (entrega reprodutível em HTML/PDF).
3. **Projeto-exemplo** — automação rápida que coleta dados, resume com um LLM e envia um
   **relatório semanal pelo WhatsApp** (Meta WhatsApp Cloud API), inspirada num digest
   semanal. Pipeline genérico e configurável.

## Convenções (herdadas do COPOM)

- **Idioma:** português do Brasil. Comentários de código em português.
- **Regra de ouro:** nunca inventar número. Todo valor citado vem de uma célula/execução
  real. Se não rodou, não entra.
- **Ciclo de trabalho:** `explore → plan → code → commit`. O agente escreve o código; o
  aluno é quem decide, valida e questiona.
- **Saída estruturada:** ao usar LLMs para extrair dados, force schema (Pydantic /
  structured output) — nada de parsing frágil de texto.
- **Segredos:** chaves de API **nunca** no código nem no git. Sempre em `.env` (no
  `.gitignore`), lidas por variável de ambiente. Há `.env.example` em `projeto-exemplo/`.

## Como renderizar a apresentação

```bash
quarto render            # gera docs/index.html (self-contained)
quarto preview index.qmd # preview ao vivo durante a edição
```

`index.qmd` usa `embed-resources: true` → o HTML é autossuficiente. O GitHub Pages
serve a pasta `docs/` na branch `main`.

## Stack

- **Quarto** ≥ 1.4 (slides reveal.js + documentos)
- **Python** ≥ 3.10 (projeto-exemplo)
- **LaTeX** (TinyTeX via `quarto install tinytex`) para saída PDF
- **Claude Code** como agente de desenvolvimento
