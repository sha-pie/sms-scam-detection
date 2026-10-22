
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Remove any rows with missing information
data = data.dropna(subset=["label", "message"])

# Prepare the messages and labels
X = data["message"].astype(str)
y = data["label"].map({"ham": 0, "spam": 1})

# Keep only recognised labels
valid_rows = y.notna()
X = X[valid_rows]
y = y[valid_rows].astype(int)

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Build the machine-learning pipeline
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            strip_accents="unicode"
        )
    ),
    ("classifier", MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("Model accuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")

print("\nClassification report:")
print(classification_report(
    y_test,
    predictions,
    labels=[0, 1],
    target_names=["Non-spam", "Spam"],
    zero_division=0
))

# Save the trained model
joblib.dump(model, "sms_model.joblib")

print("\nModel trained and saved successfully!")
