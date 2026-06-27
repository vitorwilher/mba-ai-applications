# 13. AI Applications — Ementa

**Programa:** MBA · **Módulo:** 13 — AI Applications
**Professor:** Vítor Wilher — Análise Macro
**Carga horária:** 4 encontros (laboratório aplicado)

---

## Propósito (importância da matéria)

Consolidar o aprendizado técnico em **aplicações concretas e integradas de IA** no contexto
de negócios reais. Esta disciplina funciona como **laboratório aplicado**, conectando
tecnologia com **valor entregue para o negócio**. O fio condutor é deixar de "usar a IA
como chat" e passar a **dirigir um agente** (Claude Code) que escreve, roda e versiona
projetos completos — do problema ao produto.

## Temas abordados

- Design de soluções de IA orientadas a valor: **do problema ao produto**
- Cases reais por setor: varejo, saúde, finanças, indústria e serviços
- Integração de múltiplas tecnologias: **ML + LLMs + dados + automação**
- Prototipagem rápida com ferramentas **no-code e low-code** de IA
- Apresentação e defesa de soluções de IA para **stakeholders executivos**

## Objetivo final

O aluno será capaz de **conceber, prototipar e apresentar** soluções completas de IA para
problemas reais de negócio, demonstrando domínio integrado de todos os conceitos
aprendidos ao longo do programa.

---

## Metodologia: CRISP-DM aplicada a agentes de IA

A disciplina adota o **CRISP-DM** (Cross-Industry Standard Process for Data Mining) como
mapa mental de todo projeto, reinterpretado para o trabalho **dirigindo um agente de IA**:

| Fase CRISP-DM | No contexto de agentes de IA |
|---|---|
| **Entendimento do Negócio** | Definir o problema e o valor; traduzir para um objetivo mensurável e um `CLAUDE.md`. |
| **Entendimento dos Dados** | Mapear fontes (APIs, bancos, documentos); avaliar qualidade, volume e custo de tokens. |
| **Preparação dos Dados** | Limpeza, extração de sinal, recorte de tokens; o agente escreve os coletores. |
| **Modelagem** | Prompts, **saída estruturada (Pydantic)**, escolha de LLMs, ML clássico quando cabe. |
| **Avaliação** | Validar em camadas (in-sample, holdout, walk-forward); nunca confiar num número só. |
| **Implantação** | Empacotar como produto reprodutível, versionado e **automatizado** (entrega contínua). |

**Regra de ouro:** nunca inventar número. Todo valor citado vem de uma execução real.

---

## Cronograma dos encontros

### Encontro 1 — O que a IA pode resolver
Panorama de **problemas reais** que a IA resolve, por setor (varejo, saúde, finanças,
indústria, serviços). Critérios para distinguir um bom caso de uso de um mau caso de uso.
Da tarefa pontual ao pipeline completo: onde está o valor.

### Encontro 2 — CRISP-DM aplicada a agentes de IA
A metodologia CRISP-DM como mapa de projeto, reinterpretada para o trabalho com **agentes**
(Claude Code). O papel do humano (direção científica, validação) e o papel do agente
(escrever, rodar, corrigir, versionar). Ciclo `explore → plan → code → commit`.

### Encontro 3 — CRISP-DM ao vivo: projeto Sentimento COPOM
Demonstração em tempo real: reconstrução, prompt a prompt com o Claude Code, de um projeto
real de pesquisa aplicada — um **Índice de Tom das atas do Copom** calibrado em pontos da
Selic, com **três LLMs em paralelo** (Gemini, Claude, GPT), saída estruturada, calibração
OLS e validação em três camadas, entregue como paper Quarto reprodutível.
Projeto: <https://vitorwilher.github.io/anthropic-academy-cursos/projetos/sentimento-copom/slides.html>

### Encontro 4 — Síntese, setup e automação (aula de fechamento)
Apresentação de fechamento em três partes:
1. **Recapitulação da CRISP-DM aplicada a agentes** (fixação por repetição, via COPOM).
2. **Setup do ambiente de trabalho**: VS Code + Python + extensão do Claude Code +
   integração Quarto + LaTeX.
3. **Projeto-exemplo de automação**: coletar dados → resumir com LLM → enviar **relatório
   semanal pelo WhatsApp** (inspirado num digest semanal).

Apresentação (slides): [`index.qmd`](index.qmd) → publicada em GitHub Pages.

---

## Avaliação — Trabalho final

Aplicar a metodologia **CRISP-DM** a um **problema qualquer** que possa ser resolvido com
IA e **consulta de modelos LLM via API**. Entrega individual ou em grupo, com código
reprodutível e apresentação para stakeholders.

Enunciado completo e rubrica de avaliação: [`trabalho-final.md`](trabalho-final.md).

---

## Pré-requisitos e ferramentas

- Conta no GitHub e Git instalado
- **VS Code** + **Python** ≥ 3.10
- **Claude Code** (extensão no VS Code)
- **Quarto** + **LaTeX** (TinyTeX) para entrega reprodutível
- Pelo menos uma **chave de API** de LLM (Anthropic, OpenAI ou Google)
