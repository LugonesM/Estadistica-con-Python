import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import time
from collections import Counter

class AlbumSimulator:
    def __init__(self, figus_total=860, figus_paquete=5):
        self.figus_total = figus_total
        self.figus_paquete = figus_paquete
    
    def comprar_paquete(self):
        """Genera un paquete de figuritas aleatorias"""
        return np.random.choice(self.figus_total, self.figus_paquete, replace=False)
    
    def cuantos_paquetes(self):
        """Simula llenar un álbum completo y retorna el número de paquetes necesarios"""
        album = set()
        paquetes_comprados = 0
        
        while len(album) < self.figus_total:
            paquete = self.comprar_paquete()
            album.update(paquete)
            paquetes_comprados += 1
        
        return paquetes_comprados
    
    def experimento_repetido(self, repeticiones=1000):
        """Ejecuta múltiples simulaciones y retorna estadísticas"""
        print(f"Ejecutando {repeticiones} simulaciones...")
        start_time = time.time()
        
        resultados = []
        for i in range(repeticiones):
            if (i + 1) % 100 == 0:
                print(f"Progreso: {i + 1}/{repeticiones}")
            paquetes = self.cuantos_paquetes()
            resultados.append(paquetes)
        
        end_time = time.time()
        print(f"Simulación completada en {end_time - start_time:.2f} segundos")
        
        return np.array(resultados)
    
    def calcular_estadisticas(self, resultados):
        """Calcula estadísticas descriptivas de los resultados"""
        stats_dict = {
            'promedio': np.mean(resultados),
            'mediana': np.median(resultados),
            'desviacion_std': np.std(resultados),
            'minimo': np.min(resultados),
            'maximo': np.max(resultados),
            'q25': np.percentile(resultados, 25),
            'q75': np.percentile(resultados, 75),
            'coef_variacion': np.std(resultados) / np.mean(resultados)
        }
        return stats_dict
    
    def mostrar_estadisticas(self, stats_dict):
        """Imprime las estadísticas de forma organizada"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS DE LA SIMULACIÓN")
        print("="*50)
        print(f"Promedio de paquetes:     {stats_dict['promedio']:.2f}")
        print(f"Mediana:                  {stats_dict['mediana']:.2f}")
        print(f"Desviación estándar:      {stats_dict['desviacion_std']:.2f}")
        print(f"Valor mínimo:             {stats_dict['minimo']}")
        print(f"Valor máximo:             {stats_dict['maximo']}")
        print(f"Primer cuartil (Q1):      {stats_dict['q25']:.2f}")
        print(f"Tercer cuartil (Q3):      {stats_dict['q75']:.2f}")
        print(f"Coeficiente de variación: {stats_dict['coef_variacion']:.4f}")
        print("="*50)
    
    def crear_graficos(self, resultados, stats_dict):
        """Crea visualizaciones de los resultados"""
        # Configurar el estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Crear figura con subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f'Análisis de Simulación: Álbum de {self.figus_total} figuritas\n'
                    f'Paquetes de {self.figus_paquete} figuritas - {len(resultados)} simulaciones', 
                    fontsize=16, fontweight='bold')
        
        # 1. Histograma con curva de densidad
        ax1 = axes[0, 0]
        ax1.hist(resultados, bins=50, density=True, alpha=0.7, color='skyblue', 
                edgecolor='black', linewidth=0.5)
        
        # Ajustar distribución normal
        mu, sigma = stats.norm.fit(resultados)
        x = np.linspace(resultados.min(), resultados.max(), 100)
        ax1.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
                label=f'Normal ajustada\n(μ={mu:.1f}, σ={sigma:.1f})')
        
        ax1.axvline(stats_dict['promedio'], color='red', linestyle='--', linewidth=2, 
                   label=f'Promedio: {stats_dict["promedio"]:.1f}')
        ax1.axvline(stats_dict['mediana'], color='green', linestyle='--', linewidth=2, 
                   label=f'Mediana: {stats_dict["mediana"]:.1f}')
        
        ax1.set_xlabel('Número de paquetes')
        ax1.set_ylabel('Densidad')
        ax1.set_title('Distribución de paquetes necesarios')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Box plot
        ax2 = axes[0, 1]
        box_plot = ax2.boxplot(resultados, patch_artist=True)
        box_plot['boxes'][0].set_facecolor('lightcoral')
        ax2.set_ylabel('Número de paquetes')
        ax2.set_title('Box Plot - Dispersión de resultados')
        ax2.grid(True, alpha=0.3)
        
        # Agregar estadísticas al box plot
        ax2.text(1.1, stats_dict['q75'], f'Q3: {stats_dict["q75"]:.0f}', 
                verticalalignment='center')
        ax2.text(1.1, stats_dict['mediana'], f'Med: {stats_dict["mediana"]:.0f}', 
                verticalalignment='center')
        ax2.text(1.1, stats_dict['q25'], f'Q1: {stats_dict["q25"]:.0f}', 
                verticalalignment='center')
        
        # 3. Gráfico de convergencia del promedio
        ax3 = axes[1, 0]
        promedios_acumulados = np.cumsum(resultados) / np.arange(1, len(resultados) + 1)
        ax3.plot(promedios_acumulados, color='blue', linewidth=1)
        ax3.axhline(y=stats_dict['promedio'], color='red', linestyle='--', 
                   label=f'Promedio final: {stats_dict["promedio"]:.1f}')
        ax3.set_xlabel('Número de simulaciones')
        ax3.set_ylabel('Promedio acumulado')
        ax3.set_title('Convergencia del promedio')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Q-Q plot para verificar normalidad
        ax4 = axes[1, 1]
        stats.probplot(resultados, dist="norm", plot=ax4)
        ax4.set_title('Q-Q Plot - Verificación de normalidad')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Gráfico adicional: Distribución de frecuencias detallada
        self.grafico_frecuencias(resultados)
    
    def grafico_frecuencias(self, resultados):
        """Crea un gráfico de barras con las frecuencias más comunes"""
        plt.figure(figsize=(12, 6))
        
        # Contar frecuencias
        counter = Counter(resultados)
        valores = list(range(min(resultados), max(resultados) + 1))
        frecuencias = [counter.get(v, 0) for v in valores]
        
        plt.bar(valores, frecuencias, alpha=0.7, color='lightgreen', edgecolor='black')
        plt.axvline(np.mean(resultados), color='red', linestyle='--', linewidth=2, 
                   label=f'Promedio: {np.mean(resultados):.1f}')
        
        plt.xlabel('Número de paquetes necesarios')
        plt.ylabel('Frecuencia')
        plt.title('Distribución de frecuencias detallada')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def test_normalidad(self, resultados):
        """Realiza tests estadísticos para verificar normalidad"""
        print("\n" + "="*50)
        print("TESTS DE NORMALIDAD")
        print("="*50)
        
        # Test de Shapiro-Wilk (para muestras pequeñas)
        if len(resultados) <= 5000:
            shapiro_stat, shapiro_p = stats.shapiro(resultados)
            print(f"Test de Shapiro-Wilk:")
            print(f"  Estadístico: {shapiro_stat:.6f}")
            print(f"  p-valor: {shapiro_p:.6f}")
            print(f"  ¿Normal?: {'Sí' if shapiro_p > 0.05 else 'No'}")
        
        # Test de Kolmogorov-Smirnov
        ks_stat, ks_p = stats.kstest(resultados, 'norm', 
                                    args=(np.mean(resultados), np.std(resultados)))
        print(f"\nTest de Kolmogorov-Smirnov:")
        print(f"  Estadístico: {ks_stat:.6f}")
        print(f"  p-valor: {ks_p:.6f}")
        print(f"  ¿Normal?: {'Sí' if ks_p > 0.05 else 'No'}")
        
        print("="*50)

def main():
    # Parámetros de la simulación
    figus_total = 860
    figus_paquete = 5
    repeticiones = 1000
    
    # Crear simulador
    simulador = AlbumSimulator(figus_total, figus_paquete)
    
    # Ejecutar simulaciones
    resultados = simulador.experimento_repetido(repeticiones)
    
    # Calcular estadísticas
    stats_dict = simulador.calcular_estadisticas(resultados)
    
    # Mostrar resultados
    simulador.mostrar_estadisticas(stats_dict)
    
    # Crear gráficos
    simulador.crear_graficos(resultados, stats_dict)
    
    # Tests de normalidad
    simulador.test_normalidad(resultados)
    
    # Cálculo teórico aproximado (Problema del coleccionista de cupones)
    teorico = figus_total * np.sum(1/np.arange(1, figus_total + 1)) / figus_paquete
    print(f"\nComparación con valor teórico:")
    print(f"Valor teórico aproximado: {teorico:.2f} paquetes")
    print(f"Valor simulado:          {stats_dict['promedio']:.2f} paquetes")
    print(f"Diferencia:              {abs(teorico - stats_dict['promedio']):.2f} paquetes")
    print(f"Error relativo:          {abs(teorico - stats_dict['promedio'])/teorico * 100:.2f}%")

if __name__ == "__main__":
    main()
    