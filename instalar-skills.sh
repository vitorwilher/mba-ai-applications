#!/usr/bin/env bash
# Instala as skills deste repositório nas skills do seu Claude Code.
#
# Uso:
#   bash instalar-skills.sh            # instala para o usuário (~/.claude/skills)
#   bash instalar-skills.sh --projeto  # instala na pasta atual (.claude/skills)
#
# Rode de DENTRO da pasta do repositório (após git clone).

set -euo pipefail

DESTINO="$HOME/.claude/skills"
if [ "${1:-}" = "--projeto" ]; then
  DESTINO=".claude/skills"
fi

mkdir -p "$DESTINO"

instalar() {
  local origem="$1" nome="$2"
  if [ -d "$origem" ]; then
    rm -rf "${DESTINO:?}/$nome"
    cp -r "$origem" "$DESTINO/$nome"
    echo "  ✅ $nome → $DESTINO/$nome"
  else
    echo "  ⚠️  pasta não encontrada: $origem (rode a partir da raiz do repo)"
  fi
}

echo "Instalando skills em: $DESTINO"
instalar "skill-setup-am"  "setup-am"
instalar "skill-paper-am"  "paper-analise-macro"
echo "Pronto! No Claude Code, peça: \"use a skill setup-am\" ou \"use a skill paper-analise-macro\"."
