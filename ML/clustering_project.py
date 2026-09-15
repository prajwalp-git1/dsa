import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv(r"C:\Users\Prajwal P\Downloads\Mall_Customers.csv")
#print(df.head())
#print(df.shape)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#print(df.duplicated().sum())
X= df[["Annual Income (k$)","Spending Score (1-100)"]]

plt.figure(figsize=(8,6))
plt.scatter(X["Annual Income (k$)"], X["Spending Score (1-100)"])
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Distribution")
plt.show()

sclaler = StandardScaler()
#print(X)
#print("--------------------")
X_scaled = sclaler.fit_transform(X)
#print(X_scaled)

inertia = []
for k in range(2,11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,6))
plt.plot(range(2,11), inertia, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)
#print(df.head())

plt.figure(figsize=(10,7))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="Set1",
    s=100
)
plt.title("Customer Segmentation using K-Means Clustering")
plt.show()

score = silhouette_score(X_scaled, df['Cluster'])
print("Silhouette Score:", score)

cluster_summary = df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()
print(cluster_summary)