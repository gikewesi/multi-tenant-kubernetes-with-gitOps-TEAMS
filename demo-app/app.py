from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello Teams!</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: white;
        }
        h1 {
            font-size: 90px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(#00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 2s ease-in-out infinite alternate;
            margin-bottom: 40px;
        }
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #00c6ff, 0 0 20px #0072ff;
            }
            to {
                text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
            }
        }
        .box {
            padding: 40px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            text-align: center;
        }
        .btn {
            margin-top: 20px;
            padding: 15px 40px;
            font-size: 22px;
            font-weight: bold;
            color: white;
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .btn:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }
    </style>
    <script>
        function greetTeam() {
            alert("🚀 Welcome Team! Keep building awesome things!");
        }
    </script>
</head>
<body>
    <div class="box">
    <h1>Hello Teams!!! 🎉</h1>
        <button class="btn" onclick="greetTeam()">Click Me</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
