<!DOCTYPE html>
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
  font-family: 'Poppins', sans-serif;
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
  animation: glitch 1s infinite;
}

h2 {
  font-size: 30px;
  color: #fff;
}

p {
  color: #aaa;
}

a {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  border: 2px solid #0ff;
  color: #0ff;
  text-decoration: none;
  transition: 0.3s;
}

a:hover {
  background: #0ff;
  color: black;
  box-shadow: 0 0 20px #0ff;
}

@keyframes glitch {
  0% { transform: translate(0); }
  20% { transform: translate(-5px, 5px); }
  40% { transform: translate(5px, -5px); }
  60% { transform: translate(-5px, -5px); }
  80% { transform: translate(5px, 5px); }
  100% { transform: translate(0); }
}

/* stars */
.stars {
  position: fixed;
  width: 100%;
  height: 100%;
  background: url('https://i.imgur.com/9a0f3VY.png');
  animation: moveStars 60s linear infinite;
}

@keyframes moveStars {
  from { background-position: 0 0; }
  to { background-position: 10000px 5000px; }
}
</style>
</head>

<body>

<div class="stars"></div>

<div class="container">
  <h1>404</h1>
  <h2>Lost in Space 🚀</h2>
  <p>Oops! The page you’re looking for doesn’t exist.</p>
  <a href="/">Go Home</a>
</div>

</body>
</html>
