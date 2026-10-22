
from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "sms_model.joblib"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Model not found. Run: python train_model.py"
    )

model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message = ""
    confidence = None

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            prediction = int(model.predict([message])[0])

            probabilities = model.predict_proba([message])[0]
            confidence = round(float(max(probabilities)) * 100, 1)

            if prediction == 1:
                result = "Potential Spam"
            else:
                result = "Likely Non-Spam"

    return render_template(
        "index.html",
        result=result,
        message=message,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
