# K-medoids clustering using a 2D vector (sodium and potassium)

import os
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
from sklearn_extra.cluster import KMedoids
import joblib

def show_boxplots(data, cols, prefix="", output_dir="./out-resources/boxplots"):
    for col in cols:
        print(f"Distribution of '{col}':")
        print(data[col].describe())
        print("-" * 40)

        plt.figure(figsize=(8, 4))
        sns.boxplot(x=data[col])
        plt.xlabel(col)
        plt.tight_layout()

        filename = f"{prefix}_boxplot_{col}.png" if prefix else f"boxplot_{col}.png"
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath)
        print(f"Plot saved at: {filepath}")
        
        plt.show()

def find_outliers(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    return df[(df[columna] < limite_inf) | (df[columna] > limite_sup)].index



# Load dataset
ruta_csv = "../datasets/foundation-food.csv"
df = pd.read_csv(ruta_csv, sep=',')

# Select relevant columns
selected_cols = ['sodium', 'potassium']
foods = df[selected_cols].copy()
foods = foods.sample(n=10000, random_state=42)

# Remove null values
foods = foods.dropna(subset=selected_cols)
print(f"Removed records: {len(df) - len(foods)}")

# Boxplots before cleaning
show_boxplots(foods, selected_cols, "pre-sodium-potassium")

# Outlier detection and removal
outliers_sodium_idx = find_outliers(foods, 'sodium')
outliers_potassium_idx = find_outliers(foods, 'potassium')
todos_outliers = outliers_sodium_idx.union(outliers_potassium_idx)
print(f"Total number of outliers (sodium or potassium): {len(todos_outliers)}")

foods_clean = foods.drop(index=todos_outliers)
print(f"Remaining records after removing outliers: {len(foods_clean)}")

# Boxplots after cleaning
show_boxplots(foods_clean, selected_cols, "post-sodium-potassium")

# Normalization
escalador = MinMaxScaler().fit(foods_clean.values)
foods_scaled = pd.DataFrame(escalador.transform(foods_clean.values), columns=selected_cols)

# K-Medoids clustering
kmedoids = KMedoids(n_clusters=6, metric='manhattan', init='k-medoids++', random_state=42).fit(foods_scaled.values)
foods_scaled["cluster"] = kmedoids.labels_

sil_kmeans = silhouette_score(foods_scaled.values, kmedoids.labels_, metric='manhattan')
print('Silhouette Score', sil_kmeans)

# Save models
joblib.dump(escalador, "./models/kmedoids-sodium-potassium-minmax-scaler.pkl")
joblib.dump(kmedoids, "./models/kmedoids-sodium-potassium-model.pkl")

# Cluster summary and visualization
foods_info = df.loc[foods_clean.index, ['id', 'sodium', 'potassium']].copy()
foods_info['cluster'] = kmedoids.labels_

min_max_summary = foods_info.groupby('cluster')[selected_cols].agg(['min', 'max'])
print(min_max_summary)

counts = foods_info['cluster'].value_counts().sort_index()
print("Record count per cluster:")
print(counts)


# Cluster plot
plt.figure(figsize=(10, 6), dpi=100)
colores = ["red", "blue", "orange", "black", "purple", "pink", "brown", "yellow"]

for cluster in range(kmedoids.n_clusters):
    plt.scatter(foods_scaled[foods_scaled["cluster"] == cluster]["sodium"],
                foods_scaled[foods_scaled["cluster"] == cluster]["potassium"],
                marker="o", s=180, color=colores[cluster], alpha=0.5)

    plt.scatter(kmedoids.cluster_centers_[cluster][0],
                kmedoids.cluster_centers_[cluster][1],
                marker="P", s=280, color=colores[cluster])

plt.xlabel("Sodio", fontsize=15)
plt.ylabel("Potasio", fontsize=15)
plt.text(1.15, 0.2, "K = %i" % kmedoids.n_clusters, fontsize=20)
plt.text(1.15, 0, "Inertia = %0.2f" % kmedoids.inertia_, fontsize=20)
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.tight_layout()

filename = "./out-resources/clustering/kmedoids-sodium-potassium.png"
plt.savefig(filename)
print(f"Plot saved as '{filename}'")
plt.show()

# Remove cluster column for elbow method
del foods_scaled["cluster"]

# Elbow method plot
def plot_elbow_method(df, label, k_min=2, k_max=10):
    values = df.values
    inercias = []

    for k in range(k_min, k_max):
        kmedoids = KMedoids(n_clusters=k, metric='manhattan', init='k-medoids++', random_state=42)
        kmedoids.fit(values)
        inercias.append(kmedoids.inertia_)

    plt.figure(figsize=(6, 4), dpi=100)
    plt.plot(range(k_min, k_max), inercias, marker="o", color="red", lw=2)
    plt.xlabel("Number of clusters")
    plt.ylabel("Inertia")
    plt.grid(True)
    plt.tight_layout()

    output_dir = "./out-resources/elbow_method/"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, f"kmedoids-{label}.png")
    plt.savefig(filename)
    print(f"Plot saved as '{filename}'")

    plt.show()

plot_elbow_method(foods_scaled, "sodium-potassium")
