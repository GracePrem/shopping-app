from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>GCP Shopping Store</title>
    </head>

    <body>
        <h1>Welcome to GCP Shopping Store-CI/CD Demo</h1>

        <h2>Products</h2>

        <p>Mobile Phone - ₹25,000</p>
        <button>Add to Cart</button>

        <p>Laptop - ₹55,000</p>
        <button>Add to Cart</button>

        <p>Headphones - ₹3,000</p>
        <button>Add to Cart</button>

        <p>Smart Watch - ₹5,000</p>
        <button>Add to Cart</button>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
