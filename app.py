from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("../model/model.pkl")
scaler = joblib.load("../model/scaler.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        features = np.array([[
            float(data["CGPA"]),
            int(data["Internships"]),
            int(data["Projects"]),
            int(data["Workshops"]),
            float(data["AptitudeTestScore"]),
            float(data["SoftSkillsRating"]),
            int(data["ExtraCurricularActivities"]),
            int(data["PlacementTraining"]),
            float(data["SSC_Marks"]),
            float(data["HSC_Marks"])
        ]])

        # Scale
        features = scaler.transform(features)

        # Predict
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        result = "Placed" if prediction == 1 else "Not Placed"
        percentage = round(probability * 100, 2)

        # 🔥 STEP 1: Define suggestions FIRST
        suggestions = []

        # 🔥 STEP 2: Add logic
        if float(data["CGPA"]) < 7:
            suggestions.append("Improve your CGPA above 7")

        if int(data["Internships"]) < 2:
            suggestions.append("Try doing more internships")

        if int(data["Projects"]) < 3:
            suggestions.append("Work on more projects")

        if float(data["AptitudeTestScore"]) < 60:
            suggestions.append("Practice aptitude regularly")

        if float(data["SoftSkillsRating"]) < 5:
            suggestions.append("Improve communication skills")

        if int(data["PlacementTraining"]) == 0:
            suggestions.append("Attend placement training")

        if int(data["ExtraCurricularActivities"]) == 0:
            suggestions.append("Participate in extracurricular activities")

        if not suggestions:
            suggestions.append("You are doing great! Keep it up!")

        # 🔥 STEP 3: Return it
        return jsonify({
            "result": result,
            "probability": percentage,
            "suggestions": suggestions
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)