#!/bin/bash

# Revisamos si hay cambios
if [[ -n $(git status --porcelain) ]]; then
  echo "Hay cambios, los subimos a GitHub..."

  git add .
  git commit -m "Actualización automática"
  git push origin main

  FECHA=$(date "+%Y-%m-%d %H:%M:%S")
  echo "Última actualización: $FECHA" > README.md
  git add README.md
  git commit -m "Actualización del README con fecha"
  git push origin main

  echo "¡Listo! Cambios subidos."
else
  echo "No hay cambios nuevos para subir."
fi
