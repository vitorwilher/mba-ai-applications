# Projeto-exemplo — Relatório semanal no WhatsApp

Automação ponta a ponta: **dados → resumo com LLM → WhatsApp**, rodando toda semana.
É o projeto-exemplo da Aula 4 da disciplina *AI Applications*.

## Como rodar do zero

```bash
cd projeto-exemplo
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env                  # preencha as chaves
python main.py
```

## O que você precisa no `.env`

| Variável | Onde obter |
|---|---|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) → API Keys |
| `WHATSAPP_TOKEN` | [developers.facebook.com](https://developers.facebook.com) → seu app → WhatsApp → API Setup |
| `WHATSAPP_PHONE_NUMBER_ID` | mesma tela (API Setup) |
| `WHATSAPP_DESTINO` | número que recebe (DDI+DDD, só dígitos), cadastrado como destinatário de teste |
| `FONTE_URL` | URL JSON da sua fonte de dados (padrão: série SGS/BCB) |

## Estrutura

```
projeto-exemplo/
├── coleta.py      # busca e recorta os dados da semana
├── resumo.py      # LLM + schema Pydantic (saída estruturada)
├── whatsapp.py    # envio pela Meta WhatsApp Cloud API
├── main.py        # orquestra tudo
├── requirements.txt
├── .env.example
└── .github/workflows/semanal.yml   # agendamento semanal (GitHub Actions)
```

## Agendamento

- **GitHub Actions:** já incluso em `.github/workflows/semanal.yml` (cron `0 11 * * 1`).
  Cadastre as chaves em *Settings → Secrets and variables → Actions*.
- **cron local (macOS/Linux):**

  ```cron
  0 8 * * 1 cd /caminho/projeto-exemplo && .venv/bin/python main.py
  ```

## Observações

- A WhatsApp Cloud API só envia **texto livre** dentro da janela de 24h após o usuário
  falar com você. Fora disso, use um **template aprovado** (o código já faz fallback para
  o template de teste `hello_world`).
- Regra de ouro: o LLM **não inventa números** — usa só o que está nos dados.
