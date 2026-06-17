def generate_suggestions(data):
    suggestions = []

    if data["CGPA"] < 7:
        suggestions.append("Improve your CGPA above 7.5")

    if data["Internships"] < 2:
        suggestions.append("Try doing at least 2 internships")

    if data["Projects"] < 3:
        suggestions.append("Work on more real-world projects")

    if data["Aptitude"] < 60:
        suggestions.append("Practice aptitude daily (Quant + Reasoning)")

    if data["SoftSkills"] < 6:
        suggestions.append("Improve communication and speaking skills")

    if data["PlacementTraining"] == 0:
        suggestions.append("Attend placement training sessions")

    if len(suggestions) == 0:
        suggestions.append("You are doing great! Keep it up!")

    return suggestions