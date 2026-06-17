function predict() {

    const data = {
        CGPA: parseFloat(document.getElementById("cgpa").value),
        Internships: parseInt(document.getElementById("internships").value),
        Projects: parseInt(document.getElementById("projects").value),
        Workshops: parseInt(document.getElementById("workshops").value),

        AptitudeTestScore: parseFloat(document.getElementById("aptitude").value),
        SoftSkillsRating: parseFloat(document.getElementById("softskills").value),

        ExtraCurricularActivities: parseInt(document.getElementById("extracurricular").value),
        PlacementTraining: parseInt(document.getElementById("training").value),

        SSC_Marks: parseFloat(document.getElementById("ssc").value),
        HSC_Marks: parseFloat(document.getElementById("hsc").value)
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response:", data);

        // 🔴 Handle error
        if (data.error) {
            document.getElementById("result").innerText = "Error: " + data.error;
            document.getElementById("prob").innerText = "";
            document.getElementById("suggestions").innerHTML = "";
            return;
        }

        // ✅ Show result
        document.getElementById("result").innerText = "Result: " + data.result;
        document.getElementById("prob").innerText = "Chance: " + data.probability + "%";

        // ✅ Show suggestions
        let list = document.getElementById("suggestions");
        list.innerHTML = "";

        if (data.suggestions && data.suggestions.length > 0) {
            data.suggestions.forEach(s => {
                let li = document.createElement("li");
                li.innerText = s;
                list.appendChild(li);
            });
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Something went wrong!";
    });
}