from flask import Flask, Response

app = Flask(__name__)

# ✅ Home route
@app.route("/")
def home():
    return "<h1>🔥 Flask App is LIVE 🚀</h1>"

# ✅ Your custom 404 page (directly from string)
@app.errorhandler(404)
def page_not_found(e):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 - Lost in Space</title>
<style>
body {
  margin: 0;
  background: black;
  color: white;
  font-family: sans-serif;
  overflow: hidden;
}
.container {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
h1 {
  font-size: 120px;
  color: #0ff;
  text-shadow: 0 0 20px #0ff, 0 0 40px #0ff;
}
h2 { font-size: 30px; }
a {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  border: 2px solid #0ff;
  color: #0ff;
  text-decoration: none;
}
a:hover {
  background: #0ff;
  color: black;
}
</style>
</head>
<body>
<div class="container">
  <h1>404</h1>
  <h2>Lost in Space 🚀</h2>
  <p>Page not found</p>
  <a href="/">Go Home</a>
</div>
</body>
</html>"""
    return Response(html, status=404, mimetype='text/html')


if __name__ == "__main__":
    app.run()
