# Estadistica-con-Python
Ejersicio de simulacion realizado con Python para la materia de Estadistica 

Consigna: Armar una simulación basada en N=100 repeticiones que permita estimar el promedio de paquetes necesarios para conseguir llenar el álbum de figuritas del Mundial Qatar 2022. [OPCIONAL] Si es posible, representar el histograma de la cantidad de paquetes necesarios para completar el álbum a partir de la simulación. Puede usarse import seaborn as sns y sns.histplot().
A diferencia de la resolución a mano, aquí propondremos una versión más realista: el álbum del Mundial Qatar 2022 tiene figus_total=860 y vamos a suponer que el paquete no trae una figurita, sino varias: figus_paquete=5. Además, Panini, empresa creadora del álbum del Mundial Qatar 2022, asegura que NO vienen figuritas repetidas por paquete. 



Informe de la simulacion:

La simulación de 1000 escenarios revela un comportamiento promedio de 1258.07 paquetes, muy cercano al valor teórico esperado de 1261.57 paquetes, con una diferencia mínima de apenas 3.50 unidades (0.28% de error relativo), lo que valida la robustez del modelo teórico. 

La distribución muestra una dispersión moderada (desviación estándar de 224.44 paquetes) con un coeficiente de variación del 17.84%(Al ser menor al 20%, indica una dispersión relativa moderada que sugiere que el proceso es relativamente estable y predecible.), indicando una variabilidad aceptable en relación al promedio. 

Los cuartiles (Q1=1105.75, Q3=1378.25) delinean un rango intercuartílico de 272.5 paquetes, donde se concentra el 50% central de los datos, mientras los valores extremos (812 mín., 2669 máx.) evidencian la presencia de escenarios atípicos.

Los tests de normalidad (Shapiro-Wilk y Kolmogorov-Smirnov) confirman con alta significancia (p-valor ≈ 0) que la distribución no sigue un patrón normal, sugiriendo posibles sesgos o factores externos influyentes en la simulación.

El 50% de las simulaciones procesaron menos de 1218 paquetes y el otro 50% más de esta cantidad. La diferencia entre la mediana y la media (40.07 paquetes) indica una ligera asimetría en la distribución hacia valores más altos.

La no-normalidad de la distribución indica que el proceso está sujeto a factores que crean asimetría, posiblemente eventos aleatorios o condiciones variables que afectan el rendimiento. La proximidad entre el valor simulado (1258.07) y teórico (1261.57) valida el modelo matemático.

<img width="1842" height="1023" alt="Figure_1" src="https://github.com/user-attachments/assets/51544db4-ea3f-46e4-9fd8-1ede72246550" />

<img width="1842" height="1023" alt="Figure_2" src="https://github.com/user-attachments/assets/5d6954f1-249e-43e3-bf98-2fc16b54c65c" />


==================================================

ESTADÍSTICAS DE LA SIMULACIÓN:
  - Promedio de paquetes:     1258.07
  - Mediana:                  1218.00
  - Desviación estándar:      224.44
  - Valor mínimo:             812
  - Valor máximo:             2669
  - Primer cuartil (Q1):      1105.75
  - Tercer cuartil (Q3):      1378.25
  - Coeficiente de variación: 0.1784

Test de Shapiro-Wilk:
  - Estadístico: 0.930629
  - p-valor: 0.000000
  - ¿Normal?: No

Test de Kolmogorov-Smirnov:
  - Estadístico: 0.083408
  - p-valor: 0.000002
  - ¿Normal?: No
  
==================================================

Comparación con valor teórico:
  - Valor teórico aproximado: 1261.57 paquetes
  - Valor simulado:          1258.07 paquetes
  - Diferencia:              3.50 paquetes
  - Error relativo:          0.28%
