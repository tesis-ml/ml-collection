# ML-Collection: Clustering Nutricional para Análisis de Alimentos

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://docker.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-green.svg)](https://scikit-learn.org)

## 📋 Descripción del Proyecto

Este repositorio contiene la implementación de algoritmos de clustering aplicados al análisis nutricional de alimentos como parte de una investigación de tesis. El proyecto utiliza técnicas de aprendizaje automático no supervisado para identificar patrones y agrupaciones en datos nutricionales, facilitando la clasificación automática de alimentos según sus perfiles nutricionales.

### 🎯 Objetivos

- **Análisis Nutricional**: Identificar patrones en los perfiles nutricionales de alimentos
- **Clustering Multidimensional**: Aplicar algoritmos K-means y K-medoids en diferentes dimensiones
- **Clasificación Automática**: Generar categorías de alimentos basadas en criterios nutricionales
- **Visualización de Datos**: Crear representaciones gráficas de los clusters identificados
- **Evaluación de Modelos**: Comparar la efectividad de diferentes enfoques de clustering

## 🏗️ Estructura del Proyecto

```
ml-collection/
├── 📊 datasets/
│   ├── foundation-food.csv          # Dataset principal USDA
│   ├── nuevos_alimentos.csv         # Alimentos adicionales
│   └── .ipynb_checkpoints/
├── 📓 notebooks/
│   ├── data-analysis.ipynb          # Análisis exploratorio de datos
│   ├── search-euclidean-distance.ipynb # Búsqueda por distancia euclidiana
│   ├── 🎯 K-means (2D)
│   │   ├── k-means-2d-fats-sugar.ipynb
│   │   ├── k-means-2d-protein-calories.ipynb
│   │   └── k-means-2d-sodium-potassium.ipynb
│   ├── 🎯 K-means (3D)
│   │   └── k-means-3d-protein-calories-fats.ipynb
│   ├── 🎯 K-means (Univariado)
│   │   └── k-means-univariate.ipynb
│   ├── 🎯 K-medoids (2D)
│   │   ├── k-medoids-2d-fats-sugar.ipynb
│   │   ├── k-medoids-2d-sodium-potassium.ipynb
│   │   └── k-medoids-3d-protein-calories-fats.ipynb
│   ├── 🚀 Producción
│   │   ├── prod-k-means-2d-fats-sugar.ipynb
│   │   └── prod-k-means-2d-sodium-potassium.ipynb
│   ├── 🐍 Python Scripts
│   │   ├── k-means-2d-sodium-potassium.py
│   │   └── k-medoids-2d-sodium-potassium.py
│   ├── 🤖 models/                   # Modelos entrenados (*.pkl)
│   ├── 📈 out-resources/            # Visualizaciones generadas
│   │   ├── clustering/              # Gráficos de clusters
│   │   ├── elbow_method/           # Gráficos método del codo
│   │   ├── boxplots/               # Análisis de distribuciones
│   │   └── data_analysis/          # Análisis exploratorio
│   └── 📄 out-csv/                 # Resultados exportados
├── 🐳 docker-compose.yml           # Configuración Docker
├── 🐳 Dockerfile                   # Imagen Docker personalizada
├── .gitignore
└── 📖 readme.md
```

## 🧬 Metodologías de Clustering Implementadas

### 1. **Grasa Total vs Azúcar** (`total_fat` vs `sugar`)
**Propósito**: Clasificación básica entre alimentos "azucarados" y "grasosos"

**Categorías Identificadas:**
- 🟩 **Baja grasa, bajo azúcar** → Alimentos saludables/neutros
- 🟥 **Alta grasa, alto azúcar** → Altamente calóricos/ultra procesados
- 🟨 **Baja grasa, alto azúcar** → Frutas dulces/jugos/golosinas
- 🟦 **Alta grasa, bajo azúcar** → Frutos secos/aceites/lácteos grasos

### 2. **Proteína vs Calorías vs Grasa Total** (3D)
**Propósito**: Distinguir fuentes de proteína magra vs proteína con grasa/calorías

**Categorías Identificadas:**
- **Alta proteína, baja grasa, bajas calorías** → Proteínas magras (pollo, pescado)
- **Alta proteína, alta grasa, altas calorías** → Proteínas densas (carne roja, queso)
- **Baja proteína, alta grasa/calorías** → Grasas sin proteína (aceites, manteca)
- **Baja proteína, bajas calorías/grasa** → Verduras, frutas acuosas

### 3. **Sodio vs Potasio**
**Propósito**: Clasificar alimentos según su impacto cardiovascular/renal

**Categorías Identificadas:**
- **Alto potasio, bajo sodio** → Alimentos cardioprotectores (plátano, aguacate)
- **Alto sodio, bajo potasio** → Procesados/embutidos/snacks salados
- **Ambos bajos** → Verduras, frutas neutras
- **Ambos altos** → Caldos, salsas industriales

### 4. **Carbohidratos vs Fibra vs Azúcar** (3D)
**Propósito**: Diferenciar entre carbohidratos simples y complejos

**Categorías Identificadas:**
- **Alta fibra, bajos azúcares** → Carbohidratos complejos saludables
- **Altos azúcares, baja fibra** → Azúcares simples/procesados
- **Carbohidratos moderados** → Cereales integrales/panes/arroz

### 5. **Vitaminas y Antioxidantes**
**Propósito**: Identificar alimentos ricos en micronutrientes inmunológicos

## 🔬 Algoritmos Implementados

### K-means
- **Ventajas**: Rápido, eficiente para clusters esféricos
- **Aplicaciones**: Clustering inicial, análisis exploratorio
- **Dimensiones**: 1D (univariado), 2D, 3D

### K-medoids
- **Ventajas**: Robusto a outliers, medoides como representantes reales
- **Aplicaciones**: Datos con ruido, interpretabilidad mejorada
- **Dimensiones**: 2D, 3D

## 🚀 Instalación y Uso

### Opción 1: Docker (Recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/tesis-ml/ml-collection.git
cd ml-collection

# Construir y ejecutar con Docker
docker-compose build
docker-compose up -d

# Acceder a Jupyter
# http://localhost:8888
```

### Opción 2: Instalación Local

```bash
# Crear entorno virtual
python -m venv ml-env
source ml-env/bin/activate  # Linux/Mac
# ml-env\Scripts\activate   # Windows

# Instalar dependencias
pip install jupyter scipy-notebook seaborn matplotlib scikit-learn scikit-learn-extra pandas numpy

# Ejecutar Jupyter
jupyter notebook
```

## 📊 Conjuntos de Datos

### Dataset Principal: `foundation-food.csv`
- **Fuente**: USDA (United States Department of Agriculture)
- **Registros**: ~900,000+ alimentos
- **Características**: 47 variables nutricionales
- **Variables principales**: Calorías, proteínas, grasas, carbohidratos, vitaminas, minerales

### Dataset Complementario: `nuevos_alimentos.csv`
- **Registros**: Alimentos adicionales locales/regionales
- **Propósito**: Expandir la base de datos con productos específicos

## 🔧 Técnicas de Preprocesamiento

1. **Limpieza de Datos**
   - Manejo de valores nulos
   - Detección y tratamiento de outliers
   - Normalización de unidades

2. **Escalado de Características**
   - MinMaxScaler para normalización 0-1
   - StandardScaler para estandarización Z-score

3. **Selección de Características**
   - Análisis de correlación
   - Eliminación de características redundantes

## 📈 Evaluación de Modelos

### Métricas Utilizadas
- **Método del Codo (Elbow Method)**: Determinar número óptimo de clusters
- **Silhouette Score**: Evaluar calidad de clustering
- **Distancia Intra-cluster**: Cohesión dentro de grupos
- **Distancia Inter-cluster**: Separación entre grupos

### Visualizaciones Generadas
- **Scatter plots 2D/3D**: Representación visual de clusters
- **Boxplots**: Distribución de variables por cluster
- **Heatmaps**: Correlaciones entre variables
- **Dendrogramas**: Análisis jerárquico

## 🎯 Casos de Uso

1. **Clasificación Dietética**: Identificar alimentos aptos para dietas específicas
2. **Análisis Nutricional**: Evaluar perfiles nutricionales de productos
3. **Recomendación de Alimentos**: Sugerir alternativas nutricionales
4. **Investigación en Salud**: Estudiar patrones alimentarios
5. **Desarrollo de Productos**: Optimizar formulaciones alimentarias

## 📚 Dependencias Principales

```python
# Análisis de datos
pandas >= 1.3.0
numpy >= 1.21.0

# Machine Learning
scikit-learn >= 1.0.0
scikit-learn-extra >= 0.2.0

# Visualización
matplotlib >= 3.4.0
seaborn >= 0.11.0

# Jupyter
jupyter >= 1.0.0
ipython >= 7.0.0
```

## 📖 Documentación Adicional

- **Notebooks de Análisis**: Cada notebook incluye documentación detallada
- **Comentarios en Código**: Explicaciones paso a paso
- **Visualizaciones**: Gráficos explicativos con interpretaciones

## 🔍 Resultados Destacados

- **Identificación de 5 patrones principales** en perfiles nutricionales
- **Clasificación automática** de alimentos en categorías funcionales
- **Reducción dimensional efectiva** para visualización
- **Modelos robustos** con alta interpretabilidad

## 📄 Contribuciones

Este proyecto forma parte de una investigación de tesis sobre aplicación de técnicas de machine learning en análisis nutricional. Los resultados contribuyen al entendimiento de patrones alimentarios y pueden ser utilizados en:

- Sistemas de recomendación nutricional
- Herramientas de análisis dietético
- Investigación en ciencias de la alimentación
- Desarrollo de políticas de salud pública

## 📞 Contacto

Para consultas académicas o colaboraciones relacionadas con esta investigación, favor contactar a través de los canales institucionales correspondientes.

---

**Nota**: Este repositorio contiene código y análisis desarrollados como parte de una investigación de tesis. Los modelos y resultados están en constante desarrollo y refinamiento.
