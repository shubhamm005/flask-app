html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 - Lost in Neon Space</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(circle at center, #020111, #000000);
  font-family: 'Orbitron', sans-serif;
  color: white;
}

/* STAR BACKGROUND */
.stars, .stars2, .stars3 {
  position: absolute;
  width: 100%;
  height: 100%;
  display: block;
  background: transparent;
}

.stars {
  background: url('https://raw.githubusercontent.com/Kalvium-Program/space-assets/main/stars.png') repeat;
  animation: moveStars 200s linear infinite;
}

.stars2 {
  background: url('https://raw.githubusercontent.com/Kalvium-Program/space-assets/main/stars.png') repeat;
  animation: moveStars 100s linear infinite;
  opacity: 0.5;
}

.stars3 {
  background: url('https://raw.githubusercontent.com/Kalvium-Program/space-assets/main/stars.png') repeat;
  animation: moveStars 50s linear infinite;
  opacity: 0.2;
}

@keyframes moveStars {
  from {transform: translateY(0px);}
  to {transform: translateY(-2000px);}
}

/* CENTER */
.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  text-align: center;
}

/* GLITCH TEXT */
.glitch {
  font-size: 140px;
  font-weight: 700;
  color: #00fff2;
  position: relative;
  animation: flicker 1.5s infinite;
  text-shadow: 0 0 20px #00fff2, 0 0 40px #00fff2;
}

.glitch::before,
.glitch::after {
  content: "404";
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  overflow: hidden;
}

.glitch::before {
  color: #ff00c8;
  animation: glitchTop 1s infinite linear alternate-reverse;
}

.glitch::after {
  color: #00ff6a;
  animation: glitchBottom 1s infinite linear alternate-reverse;
}

@keyframes glitchTop {
  0% {transform: translate(2px,-2px);}
  100% {transform: translate(-2px,2px);}
}

@keyframes glitchBottom {
  0% {transform: translate(-2px,2px);}
  100% {transform: translate(2px,-2px);}
}

@keyframes flicker {
  0%, 100% {opacity: 1;}
  50% {opacity: 0.6;}
}

h2 {
  font-size: 28px;
  margin-top: -20px;
  color: #ffffff;
  letter-spacing: 3px;
}

p {
  color: #aaa;
}

/* BUTTON */
a {
  display: inline-block;
  margin-top: 25px;
  padding: 12px 28px;
  border: 2px solid #00fff2;
  color: #00fff2;
  text-decoration: none;
  border-radius: 30px;
  transition: 0.3s;
  box-shadow: 0 0 10px #00fff2;
}

a:hover {
  background: #00fff2;
  color: black;
  box-shadow: 0 0 40px #00fff2;
  transform: scale(1.1);
}

/* FLOATING ORBS */
.orb {
  position: absolute;
  width: 10px;
  height: 10px;
  background: #00fff2;
  border-radius: 50%;
  box-shadow: 0 0 20px #00fff2;
  animation: float 6s infinite ease-in-out;
}

@keyframes float {
  0% {transform: translateY(0);}
  50% {transform: translateY(-40px);}
  100% {transform: translateY(0);}
}
</style>
</head>

<body>

<div class="stars"></div>
<div class="stars2"></div>
<div class="stars3"></div>

<!-- floating orbs -->
<div class="orb" style="top:20%; left:10%;"></div>
<div class="orb" style="top:70%; left:80%;"></div>
<div class="orb" style="top:40%; left:60%;"></div>

<div class="container">
  <div class="glitch">404</div>
  <h2>YOU ENTERED A GLITCHED UNIVERSE</h2>
  <p>The page you are looking for has been lost in space-time.</p>
  <a href="/">🚀 Return Home</a>
</div>

</body>
</html>"""
