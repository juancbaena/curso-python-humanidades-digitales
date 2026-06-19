# analisis.py — mi primer script local con entorno virtual
# Usa tres librerias: pandas (datos), seaborn y matplotlib (graficos).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1) Datos de ejemplo: numero de obras literarias por genero
df = pd.DataFrame({
    "genero": ["Novela", "Poesia", "Teatro", "Cuento"],
    "obras":  [5, 4, 2, 3],
})
print("Datos cargados:")
print(df)

# 2) Estilo bonito con seaborn y un grafico de barras
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="genero", y="obras", hue="genero",
            palette="viridis", legend=False)

plt.title("Obras literarias por genero")
plt.xlabel("Genero")
plt.ylabel("Numero de obras")
plt.tight_layout()

# 3) Guardar el grafico como PDF en la misma carpeta del script
plt.savefig("grafica.pdf")
print("Listo: se guardo 'grafica.pdf' en la carpeta del proyecto.")