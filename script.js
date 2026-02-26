// ===============================
// AI Smart Lighting - Frontend JS
// ===============================

const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const loader = document.getElementById("loader");
const resultBox = document.getElementById("resultBox");
const similarProducts = document.getElementById("similarProducts");

// ===============================
// Image Preview
// ===============================
imageInput.addEventListener("change", function () {
    const file = imageInput.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
});

// ===============================
// Form Submission
// ===============================
form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image.");
        return;
    }

    // Reset UI
    loader.style.display = "block";
    resultBox.style.display = "none";
    similarProducts.innerHTML = "";

    const formData = new FormData();
    formData.append("image", file);

    try {
        const response = await fetch("http://localhost:5000/identify", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        loader.style.display = "none";

        // If similar products returned
        if (data.similar_products) {
            displaySimilarProducts(data.similar_products);
        } 
        // Exact match
        else {
            displayProductDetails(data);
        }

    } catch (error) {
        loader.style.display = "none";
        alert("Error connecting to server. Make sure Flask is running.");
        console.error(error);
    }
});


// ===============================
// Display Exact Match
// ===============================
function displayProductDetails(data) {

    resultBox.style.display = "block";

    document.getElementById("itemNumber").innerText = data.item_number || "-";
    document.getElementById("lampType").innerText = data.lamp_type || "-";
    document.getElementById("dimensions").innerText = data.dimensions || "-";
    document.getElementById("finish").innerText = data.finish || "-";
    document.getElementById("material").innerText = data.material || "-";
    document.getElementById("price").innerText = data.price || "-";

    if (data.similarity) {
        document.getElementById("similarity").innerText =
            (data.similarity * 100).toFixed(2) + "%";
    } else {
        document.getElementById("similarity").innerText = "-";
    }
}


// ===============================
// Display Similar Products
// ===============================
function displaySimilarProducts(products) {

    similarProducts.innerHTML = "<h3>No exact match found. Showing similar products:</h3>";

    products.forEach(product => {

        const card = document.createElement("div");
        card.className = "similar-card";

        card.innerHTML = `
            <img src="${product.image_url}" alt="Product Image">
            <p><strong>${product.item_number}</strong></p>
            <p>₹${product.price}</p>
        `;

        similarProducts.appendChild(card);
    });
}
const firebaseConfig = {
  apiKey: "AIzaSyDrKlkBb5pEn2EYPORWEEfGXK5xjvVzsDY",
  authDomain: "lamp-f43f6.firebaseapp.com",
  projectId: "lamp-f43f6",
  storageBucket: "lamp-f43f6.firebasestorage.app",
  messagingSenderId: "728290121036",
  appId: "1:728290121036:web:2a6c33f53c2ea65963ebe9",
  measurementId: "G-4CL4MJVL2S"
};
