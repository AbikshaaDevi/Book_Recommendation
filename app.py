from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load model and vectorizer
with open("kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load dataset for showing similar quotes
df = pd.read_csv(r"C:\Users\USER\Desktop\Data_Science\Book_Recommendation\Quotes.csv")
df['Quote'] = df['Quote'].fillna('')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cluster_quotes = []
    if request.method == "POST":
        user_quote = request.form["quote"]

        # Vectorize input
        user_vec = vectorizer.transform([user_quote])

        # Predict cluster
        cluster = model.predict(user_vec)[0]

        # Get similar quotes from the same cluster
        cluster_quotes = df.iloc[
            [i for i, q in enumerate(model.labels_) if q == cluster]
        ]['Quote'].head(5).tolist()

    return render_template("index.html", quotes=cluster_quotes)

if __name__ == "__main__":
    app.run(debug=True)
