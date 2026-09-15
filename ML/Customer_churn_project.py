import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix )

df = pd.read_csv(r"C:\Users\Prajwal P\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

df["TotalCharges"]= pd.to_numeric(df["TotalCharges"],errors="coerce")
df.dropna(inplace=True)
df.drop("customerID", axis=1, inplace=True)

churn_counts= df["Churn"].value_counts()
plt.bar( 
    churn_counts.index,
    churn_counts.values
)

plt.xlabel("Churn")
plt.ylabel("Customers")
plt.title("Customer Churn")

plt.show()

df= pd.get_dummies(
    df,
    drop_first=True
)

X= df.drop("Churn_Yes", axis=1)
y= df["Churn_Yes"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model= LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall =recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

cm= confusion_matrix(y_test,y_pred)
print(cm)

plt.imshow(cm)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.colorbar()
plt.xticks([0,1],
           ["No churn", "Churn"])
plt.yticks([0,1],
           ["No churn", "Churn"])

for i in range(2):
    for j in range(2):
        plt.text(j,i,cm[i,j],ha="center",va="center")
plt.show()