from flask import Flask, request, jsonify
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from feature_extractor import extract_features
from firebase_config import db

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_all_products():
    products = []
    docs = db.collection("products").stream()
    for doc in docs:
        products.append(doc.to_dict())
    return products

@app.route("/identify", methods=["POST"])
def identify():
    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    uploaded_features = extract_features(filepath)

    products = get_all_products()

    best_score = 0
    best_product = None
    scores = []

    for product in products:
        stored_features = np.array(product["features"]).reshape(1, -1)
        score = cosine_similarity(uploaded_features, stored_features)[0][0]
        scores.append((score, product))

        if score > best_score:
            best_score = score
            best_product = product

    scores.sort(reverse=True, key=lambda x: x[0])

    if best_score < 0.70:
        return jsonify({
            "similar_products": [
                {
                    "item_number": p[1]["item_number"],
                    "price": p[1]["price"],
                    "image_url": p[1]["image_url"]
                }
                for p in scores[:3]
            ]
        })

    best_product["similarity"] = float(best_score)
    return jsonify(best_product)

if __name__ == "__main__":
    app.run(debug=True)
