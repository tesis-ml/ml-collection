# ML-MODELS

### Run docker image

```
docker-compose build
docker-compose up -d
```

### Jupyter runs on port 8888

## Clusterings

---

### **1. `total_fat` vs `sugar`**
**Valor:** Clasificación básica entre alimentos “azucarados” y “grasosos”.

**Categorías posibles:**
- 🟩 Baja grasa, bajo azúcar → **Alimentos saludables / neutros**
- 🟥 Alta grasa, alto azúcar → **Altamente calóricos / ultra procesados**
- 🟨 Baja grasa, alto azúcar → **Frutas dulces / jugos / golosinas**
- 🟦 Alta grasa, bajo azúcar → **Frutos secos / aceites / lácteos grasos**

---

### **2. `protein` vs `calories` vs `total_fat`**
**Valor:** Excelente para distinguir **fuentes de proteína magra** vs **proteína acompañada de grasa/calorías**.

**Categorías posibles:**
- **Alta proteína, baja grasa, bajas calorías** → **Proteínas magras** (pollo, pescado blanco)
- **Alta proteína, alta grasa, altas calorías** → **Proteínas densas** (carne roja, queso)
- **Baja proteína, alta grasa/calorías** → **Grasas sin proteína** (aceites, manteca)
- **Baja proteína, bajas calorías y grasa** → **Verduras, frutas acuosas**

---

### **3. `carbs` vs `dietary_fiber` vs `sugar`**
**Valor:** Te ayuda a diferenciar entre **carbohidratos simples** y **complejos**, ideal para etiquetar **índice glucémico** estimado.

**Categorías posibles:**
- **Alta fibra, bajos azúcares** → **Carbohidratos complejos saludables** (avena, legumbres)
- **Altos azúcares, baja fibra** → **Azúcares simples / procesados**
- **Altos carbohidratos, fibra moderada y azúcares moderados** → **Cereales integrales / panes / arroz**

---

### **4. `vitamin_c` vs `vitamin_a` vs `carotenoids`**
**Valor:** Te permite identificar alimentos ricos en **antioxidantes y micronutrientes inmunológicos**.

**Categorías posibles:**
- **Altos en C y A (con carotenoides)** → **Frutas/verduras coloridas (zanahoria, papaya, mango, espinaca)**
- **Altos en A sin carotenoides** → **Alimentos de origen animal (hígado, huevo)**
- **Bajos en ambos** → **Cereales, carnes blancas, refinados**

---

### **5. `sodium` vs `potassium`**
**Valor:** Fundamental para clasificar alimentos según su **impacto cardiovascular / renal**.

**Categorías posibles:**
- **Alto potasio, bajo sodio** → **Alimentos protectores cardiovasculares (plátano, aguacate, papas)**
- **Alto sodio, bajo potasio** → **Procesados / embutidos / snacks salados**
- **Ambos bajos** → **Verduras, frutas neutras**
- **Ambos altos** → **Algunos caldos, salsas industriales**

---
