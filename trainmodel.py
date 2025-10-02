import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Synthetic dataset (replace with Kaggle CSV if you want)
def generate_data(n=1000):
    np.random.seed(42)
    locations = ["newyork", "sanfrancisco", "chicago", "boston"]
    data = []
    for _ in range(n):
        area = np.random.randint(500, 4000)
        bedrooms = np.random.randint(1, 6)
        bathrooms = np.random.randint(1, 4)
        doors = np.random.randint(1, 5)
        age = np.random.randint(0, 50)
        location = np.random.choice(locations)
        price = area * 300 + bedrooms*10000 + bathrooms*5000 - age*1000
        if location == "newyork": price *= 1.5
        if location == "sanfrancisco": price *= 1.8
        if location == "chicago": price *= 1.1
        data.append([area, bedrooms, bathrooms, doors, age, location, price])
    return pd.DataFrame(data, columns=["area","bedrooms","bathrooms","doors","age","location","price"])

# Load or generate dataset
df = generate_data()

X = df.drop(columns=["price"])
y = df["price"]

# Encode categorical manually (location)
X = pd.get_dummies(X, columns=["location"], drop_first=True)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²:", r2_score(y_test, y_pred))

# Save model and columns
joblib.dump({"model": model, "columns": X.columns.tolist()}, "house_price_model.pkl")
print("✅ Model saved as house_price_model.pkl")
