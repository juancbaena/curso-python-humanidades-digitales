# Día 5 — Web, APIs, medios digitales y proyecto integrador

Uso básico de APIs y extracción de información de la web, manipulación básica
de medios digitales (imagen, audio y video) y diseño del proyecto integrador para EH1023.

## Cuadernos

- `12_apis_y_extraccion_web.ipynb` — APIs y extracción de datos de la web.
- `13_actividad_con_monitor_ia.ipynb` — actividad con el monitor: tu primer **script local en VS Code**
  (crear carpeta y `analisis.py`, entorno virtual, instalar `pandas`/`seaborn`/`matplotlib`, ejecutar y
  guardar un PDF). Continúa la guía de `pip` y entornos virtuales del Día 3-4.
- `14_medios_digitales_y_proyecto_integrador.ipynb` — medios digitales y diseño del proyecto integrador.
- `15_proyecto_integrador_ia_local.ipynb` — **capstone**: analizador de textos literarios que
  reúne todo lo visto en la semana y ejecuta un **modelo de lenguaje local** (Ollama + Gemma 3n)
  dentro del propio cuaderno, sin clave de API.
- `16_autoevaluacion_final.ipynb` — **actividad de cierre del curso**: cuestionario de
  autoevaluación (15 enunciados *"puedo hacer…"* en escala 1-5, respondidos como formulario con
  `input()`) que cubre los 5 días. Calcula el nivel por día y global, recomienda el cuaderno de
  repaso/contenido a reforzar según cada respuesta y **genera un PDF** que el participante envía a
  **calderonf@javeriana.edu.co**. No se entregan soluciones de ejercicios: es un diagnóstico
  personal. Incluye una sección **para futuros docentes** sobre cómo reutilizarlo como diagnóstico
  de entrada/salida y rúbrica alineada con el EH1023.

> **Cuaderno 15 — requisitos.** Requiere entorno con **GPU T4** en Colab
> (*Entorno de ejecución → Cambiar tipo de entorno de ejecución → T4 GPU*). El modelo por defecto
> es `gemma3n:e2b`; para clases con conexión lenta puede cambiarse por `gemma3:1b` en la celda de
> configuración. El tema (análisis de textos literarios) responde al interés #1 de la encuesta del
> curso.
