# Trabalho Final — AI Applications

**Disciplina:** 13. AI Applications — MBA
**Professor:** Vítor Wilher — Análise Macro

---

## 1. Objetivo

Aplicar a metodologia **CRISP-DM** a um **problema qualquer** que possa ser resolvido com
**IA** e **consulta de modelos LLM via API**. O trabalho deve demonstrar domínio integrado
de tudo o que vimos na disciplina: do **problema de negócio** ao **produto reprodutível**,
dirigindo o **Claude Code** como agente de desenvolvimento.

Não interessa o "chat bonito". Interessa o **pipeline**: uma solução que coleta dados,
usa um ou mais LLMs **via API** com **saída estruturada**, avalia o resultado e **entrega
valor** de forma reprodutível.

## 2. Escopo e regras

- **Tema livre**, desde que tenha **valor de negócio** claro (varejo, saúde, finanças,
  indústria, serviços, setor público — sua escolha).
- Uso obrigatório de **pelo menos um LLM via API** (Anthropic, OpenAI ou Google) com
  **saída estruturada** (Pydantic / structured output) em algum ponto do pipeline.
- **Dados reais** de pelo menos uma fonte (API pública, base própria, documentos, planilhas).
- Desenvolvimento dirigindo o **Claude Code**, no ciclo `explore → plan → code → commit`.
- **Regra de ouro:** nenhum número inventado. Todo valor citado vem de código que roda.
- **Segredos** (chaves de API) **nunca** versionados — sempre em `.env` no `.gitignore`.

> Pode ser **individual ou em grupo (até 3 pessoas)**. Combine o tema com o professor antes
> de começar a fase de Modelagem.

## 3. As seis fases (o que entregar em cada uma)

| Fase CRISP-DM | Entregável esperado |
|---|---|
| **1. Entendimento do Negócio** | Problema, quem decide, qual decisão muda, e **uma métrica de sucesso**. |
| **2. Entendimento dos Dados** | Fontes mapeadas, volume, qualidade, limitações e custo estimado de tokens. |
| **3. Preparação dos Dados** | Coleta + limpeza + recorte de sinal (código comentado). |
| **4. Modelagem** | LLM via API com **schema fixo**; prompts versionados; baseline simples para comparação. |
| **5. Avaliação** | Validação com **mais de uma métrica/camada**; análise crítica honesta dos limites. |
| **6. Implantação** | Produto reprodutível: documento Quarto e/ou automação (ex.: relatório/alerta). |

## 4. Entregáveis

1. **Repositório Git** (GitHub) contendo:
   - `CLAUDE.md` com o briefing do projeto e a regra de ouro;
   - código reprodutível (`requirements.txt`, instruções de `.venv`, `.env.example`);
   - `README.md` explicando como rodar do zero.
2. **Relatório técnico** em **Quarto + LaTeX (PDF)** percorrendo as seis fases do CRISP-DM,
   com os números gerados por código (nenhum digitado à mão). **Use a skill
   [`skill-paper-am/`](skill-paper-am/)**: o `template/paper.qmd` já traz a capa, o cabeçalho
   LaTeX e a estrutura; veja o paper renderizado em `skill-paper-am/exemplo/paper-exemplo.pdf`.
3. **Apresentação para stakeholders** (~10 min): slides no estilo executivo — problema,
   solução, resultado, valor e próximos passos.

## 5. Rubrica de avaliação (100 pontos)

| Critério | Pontos | O que se avalia |
|---|---:|---|
| **Aderência ao CRISP-DM** | 25 | As seis fases estão presentes, na ordem, e bem justificadas. |
| **Qualidade técnica** | 25 | LLM via API com saída estruturada; código limpo; baseline; tratamento de erros. |
| **Reprodutibilidade** | 15 | Roda do zero seguindo o README; segredos fora do git; ambiente isolado. |
| **Rigor na avaliação** | 15 | Mais de uma métrica/camada; análise honesta de limitações; regra de ouro respeitada. |
| **Valor de negócio** | 10 | O problema importa e a solução muda uma decisão real. |
| **Comunicação** | 10 | Relatório e apresentação claros para um público executivo. |

**Bônus (+5):** automação real (agendamento, alerta, envio por WhatsApp/e-mail) entregando
o resultado sem intervenção manual.

## 6. Sugestões de tema (opcional)

- **Digest semanal** de um indicador setorial, resumido por LLM e enviado por WhatsApp/e-mail
  (parte de hoje, em outro domínio).
- **Classificação estruturada** de tickets/avaliações/contratos com LLM + validação.
- **Extração de campos** de documentos (notas, laudos, editais) com schema Pydantic.
- **Índice de sentimento/tom** de notícias ou relatórios de um setor (no espírito do COPOM).
- **Triagem/priorização** de leads, chamados ou riscos com score gerado por LLM.

## 7. Prazos e formato de entrega

- **Definição do tema:** combinar com o professor antes da fase de Modelagem.
- **Entrega final:** link do repositório GitHub (público ou com acesso ao professor) +
  relatório renderizado + slides.
- Dúvidas: durante as aulas ou pelos canais da turma.

---

> **Dica final:** trate o Claude Code como um assistente de pesquisa sênior. Você traz a
> direção (o problema, a hipótese, o critério de qualidade); ele traz velocidade. O melhor
> trabalho não é o que tem o prompt mais esperto — é o que tem o **método mais claro**.
