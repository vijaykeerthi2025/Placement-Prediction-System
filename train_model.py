import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostClassifier
import joblib

# Load dataset
df = pd.read_csv("../data/placement.csv")

# Clean column names
df.columns = df.columns.str.strip()

# ❌ Drop StudentID (not useful)
df = df.drop("StudentID", axis=1)

# 🔷 Convert Yes/No to 1/0
df["ExtraCurricularActivities"] = df["ExtraCurricularActivities"].map({"Yes": 1, "No": 0})
df["PlacementTraining"] = df["PlacementTraining"].map({"Yes": 1, "No": 0})

# 🔷 Convert target column
df["PlacementStatus"] = df["PlacementStatus"].map({
    "Placed": 1,
    "NotPlaced": 0
})

# 🔷 Features (EXACT names from dataset)
feature_columns = [
    "CGPA",
    "Internships",
    "Projects",
    "Workshops",
    "AptitudeTestScore",
    "SoftSkillsRating",
    "ExtraCurricularActivities",
    "PlacementTraining",
    "SSC_Marks",
    "HSC_Marks"
]

X = df[feature_columns]
y = df["PlacementStatus"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train model
model = CatBoostClassifier(verbose=0)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "../model/model.pkl")
joblib.dump(scaler, "../model/scaler.pkl")

print("✅ Model trained successfully!")