from firebase_config import db

catalog_data = [

    {
        "item_number": "2035-1",
        "lamp_type": "LED 12W",
        "dimensions": "D100MM X FH220MM X H1200MM",
        "finish": "ANTIQUE BRASS",
        "material": "METAL + ONYX MARBLE",
        "price": 10400
    },

    {
        "item_number": "2039-H",
        "lamp_type": "1XE14",
        "dimensions": "D130MM X FH150MM X H1200MM",
        "finish": "ANTIQUE BRASS",
        "material": "METAL + ONYX MARBLE",
        "price": 7800
    },

    {
        "item_number": "2026-RD",
        "lamp_type": "1XE14",
        "dimensions": "W100MM X FH210MM X H1200MM",
        "finish": "ANTIQUE BRASS",
        "material": "METAL + ONYX MARBLE",
        "price": 7900
    },

    {
        "item_number": "2026-1SQ",
        "lamp_type": "1XE14",
        "dimensions": "W100MM X FH210MM X H1200MM",
        "finish": "ANTIQUE BRASS",
        "material": "METAL + ONYX MARBLE",
        "price": 7900
    },

    {
        "item_number": "20488-1",
        "lamp_type": "LED",
        "dimensions": "D120MM X FH280MM X H1200MM",
        "finish": "ANTIQUE BRASS",
        "material": "METAL + ONYX MARBLE + ACRYLIC",
        "price": 11600
    }

]

for product in catalog_data:
    product["image_url"] = ""
    product["features"] = []
    db.collection("products").add(product)

print("Catalog uploaded successfully!")
