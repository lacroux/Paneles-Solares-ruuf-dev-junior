🟩 Tarea Dev Junior – Ruuf
👋 Introducción

Este repositorio contiene la solución al desafío técnico para la postulación al cargo Dev Junior en Ruuf.

El objetivo es implementar un algoritmo que calcule la máxima cantidad de paneles solares rectangulares que pueden instalarse en un techo rectangular, considerando distintas orientaciones y combinaciones posibles.

Además, se incluye una explicación clara del funcionamiento del código, cómo ejecutarlo y las decisiones de diseño tomadas.

🎯 Objetivo del Problema

Dadas las dimensiones:

Panel solar: a x b

Techo: x x y

Se debe calcular cuántos paneles caben sin superposición, permitiendo:

Rotación de paneles

Uso de combinaciones mixtas

Aprovechamiento óptimo del espacio

La función debe devolver un número entero.

🛠️ Tecnologías Utilizadas

Python

JSON

📂 Estructura del Proyecto
.
├── main.py
├── test_cases.json
└── README.md


main.py: Contiene la solución del problema y el runner de pruebas

test_cases.json: Casos de prueba utilizados para validar el algoritmo

README.md: Documentación del proyecto

⚙️ Cómo Ejecutar el Proyecto

Clona el repositorio o descarga los archivos

Abre una terminal en la carpeta del proyecto

Ejecuta:

python main.py


El programa cargará los casos de prueba desde test_cases.json y mostrará si cada uno pasa o falla.

🧠 Lógica de la Solución

La función principal es:

calculate_panels(panel_width, panel_height, roof_width, roof_height)

Enfoque utilizado

Orientación simple
Se calcula cuántos paneles caben sin rotarlos y luego rotados.

Combinaciones mixtas
Se prueban configuraciones por columnas:

Parte del techo usa una orientación

El espacio restante se llena con la orientación rotada

Optimización
En cada caso se guarda el valor máximo encontrado.

Este enfoque permite resolver casos donde una sola orientación no es suficiente (por ejemplo, techos 3x5 con paneles 1x2).

🔍 Opciones Consideradas

Cálculo por área: descartado, ya que no garantiza una distribución válida.

Solo una orientación: no aprovecha bien techos irregulares.

Combinaciones mixtas: elegida por ser más flexible y eficiente.

🧪 Casos de Prueba

Los escenarios están definidos en test_cases.json:

{
  "panelW": 1,
  "panelH": 2,
  "roofW": 3,
  "roofH": 5,
  "expected": 7
}


El programa compara automáticamente el resultado esperado con el resultado real.

🎥 Video Explicativo

Link Video:

👉 https://www.youtube.com/watch?v=4--E3I1xtK4


👤 Autor

Yobany La Cruz
Postulación Dev Junior – Ruuf