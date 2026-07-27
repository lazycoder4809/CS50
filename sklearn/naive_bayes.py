import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("imdb.csv")

print(df.head())

X = df["review"]
y = df["sentiment"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

while True:

    review = input("\nWrite a review (or type quit): ")

    if review.lower() == "quit":
        break

    review_vector = vectorizer.transform([review])

    prediction = model.predict(review_vector)[0]

    probability = model.predict_proba(review_vector).max()

    print(f"\nPrediction : {prediction}")
    print(f"Confidence : {probability:.2%}")