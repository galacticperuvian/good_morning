from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Buenos días hermosa</title>
        <style>
            body {
                background: linear-gradient(135deg, #ff9a9e, #fecfef);
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.9);
                padding: 30px 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                color: #e63946;
            }
            p {
                font-size: 1.2rem;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Buenos días, muñeca hermosa 😉</h1>
            <p>Solo quería que tu primer clic del día fuera una sonrisa.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
