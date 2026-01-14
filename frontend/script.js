let chart = null;

function analyzeDecision() {
    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            decision_id: decisionSelect.value,
            frequency: frequency.value,
            time_period: time_period.value,
            dream_job: dream_job.value
        })
    })
    .then(res => res.json())
    .then(data => {
        result.style.display = "block";

        pattern.innerText = data.pattern;
        capability.innerText = "Capability: " + data.capability_percent + "%";
        advice.innerText = data.advice;

        const labels = Object.keys(data.impact);
        const values = Object.values(data.impact);
        const colors = values.map(v => v >= 0 ? "#22c55e" : "#ef4444");

        if (chart) chart.destroy();

        const ctx = document
            .getElementById("impactChart")
            .getContext("2d");

        chart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Impact Score",
                    data: values,
                    backgroundColor: colors
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    });
}