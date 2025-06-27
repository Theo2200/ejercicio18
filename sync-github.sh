#!/bin/bash

# Este script automatiza el proceso de subir cambios a GitHub

# Verificamos si hay cambios usando git status
if [[ -n $(git status --porcelain) ]]; then
  echo "Hay cambios en el proyecto. Subiendo a GitHub..."

  # Agregamos todos los archivos modificados
  git add .

  # Creamos un commit con un mensaje automático
  git commit -m " Commit automático semanal"

  # Subimos los cambios a la rama main del repositorio remoto
  git push origin main

  # Guardamos la fecha y hora en el README.md
  FECHA=$(date "+%Y-%m-%d %H:%M:%S")
  echo "Última actualización automática: $FECHA" >> README.md

  # Se Sube el nuevo README
  git add README.md
  git commit -m "📄 Actualización del README con fecha"
  git push origin main

  echo "Todo listo: Cambios subidos y README actualizado."

else
  # Si no hay cambios, se muestra este mensaje
  echo "📭 No hay cambios nuevos para subir."
fi
