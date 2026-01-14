from flask import Flask, request, jsonify
from flask_cors import CORS

from logic.calculator import calculate_impact
from logic.patterns import detect_pattern
from logic.impact_map import calculate_butterfly_intensity

app = Flask(__name__)
CORS(app)

# 🔍 Infer requirements for ANY dream job
def infer_job_requirements(dream_job):
    job = dream_job.lower()

    if any(word in job for word in ["engineer", "developer", "programmer"]):
        return {"focus": 5, "career": 5, "health": 3}

    if any(word in job for word in ["data", "scientist", "analyst", "ai"]):
        return {"focus": 5, "career": 4, "health": 3}

    if any(word in job for word in ["entrepreneur", "startup", "business", "founder"]):
        return {"focus": 4, "career": 5, "health": 4}

    if any(word in job for word in ["government", "ias", "ips", "upsc", "ssc"]):
        return {"focus": 4, "career": 4, "health": 3}

    # fallback for ANY unknown job
    return {"focus": 4, "career": 4, "health": 3}


def calculate_capability(impact, dream_job):
    reqs = infer_job_requirements(dream_job)

    score = 0
    max_score = sum(reqs.values())

    for k in reqs:
        score += impact.get(k, 0)

    percent = int((score / max_score) * 100)
    percent = max(0, min(100, percent))

    # ✅ ERROR-FREE advice logic
    if percent < 30:
        advice = f"Harsh truth: agar aise hi chalta raha, {dream_job} banna mushkil hai. " \
                 "Sapna chhodne ki nahi, habits badalne ki zarurat hai."
    elif percent < 60:
        advice = f"Potential hai, par consistency nahi. {dream_job} banna possible hai, " \
                 "lekin sirf agar decisions improve hue."
    elif percent < 80:
        advice = f"Tu sahi direction me hai. {dream_job} achievable hai, " \
                 "bas distractions kam kar."
    else:
        advice = f"Strong alignment! {dream_job} ke liye tu sahi track pe hai. " \
                 "Ab self-sabotage mat kar."

    return percent, advice


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    decision_id = data.get("decision_id")
    frequency = int(data.get("frequency", 1))
    time_period = int(data.get("time_period", 1))
    dream_job = str(data.get("dream_job", "your dream")).lower()

    impact = calculate_impact(decision_id)
    pattern = detect_pattern(impact)
    butterfly_intensity = calculate_butterfly_intensity(
        impact, frequency, time_period
    )

    capability, advice = calculate_capability(impact, dream_job)

    return jsonify({
        "impact": impact,
        "pattern": pattern,
        "butterfly_intensity": butterfly_intensity,
        "capability_percent": capability,
        "advice": advice
    })


if __name__ == "__main__":
    app.run(debug=True)