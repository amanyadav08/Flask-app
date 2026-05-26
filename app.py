from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>PATHNEX - DevOps Training & Placement Institute</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
    scroll-behavior:smooth;
}

body{
    background:#020617;
    color:white;
    overflow-x:hidden;
}

/* Animated Background */

.bg-animation{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    z-index:-1;
    overflow:hidden;
}

.bg-animation span{
    position:absolute;
    display:block;
    width:20px;
    height:20px;
    background:rgba(14,165,233,0.2);
    animation:animate 25s linear infinite;
    bottom:-150px;
    border-radius:50%;
}

.bg-animation span:nth-child(1){
    left:10%;
    width:80px;
    height:80px;
    animation-delay:0s;
}

.bg-animation span:nth-child(2){
    left:20%;
    width:40px;
    height:40px;
    animation-delay:2s;
    animation-duration:12s;
}

.bg-animation span:nth-child(3){
    left:70%;
    width:60px;
    height:60px;
    animation-delay:4s;
}

.bg-animation span:nth-child(4){
    left:40%;
    width:100px;
    height:100px;
    animation-delay:0s;
    animation-duration:18s;
}

.bg-animation span:nth-child(5){
    left:65%;
    width:40px;
    height:40px;
    animation-delay:0s;
}

.bg-animation span:nth-child(6){
    left:75%;
    width:110px;
    height:110px;
    animation-delay:3s;
}

.bg-animation span:nth-child(7){
    left:35%;
    width:150px;
    height:150px;
    animation-delay:7s;
}

.bg-animation span:nth-child(8){
    left:50%;
    width:25px;
    height:25px;
    animation-delay:15s;
    animation-duration:45s;
}

@keyframes animate{
    0%{
        transform:translateY(0) rotate(0deg);
        opacity:1;
        border-radius:0;
    }

    100%{
        transform:translateY(-1000px) rotate(720deg);
        opacity:0;
        border-radius:50%;
    }
}

/* Navbar */

nav{
    width:100%;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:25px 8%;
    position:fixed;
    top:0;
    z-index:1000;
    background:rgba(2,6,23,0.7);
    backdrop-filter:blur(15px);
}

.logo{
    font-size:42px;
    font-weight:800;
    color:#38bdf8;
    letter-spacing:3px;
}

nav ul{
    display:flex;
    list-style:none;
    gap:35px;
}

nav ul li a{
    color:white;
    text-decoration:none;
    font-size:18px;
    transition:0.3s;
}

nav ul li a:hover{
    color:#38bdf8;
}

/* Hero Section */

.hero{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:0 10%;
    position:relative;
}

.hero-content{
    max-width:1100px;
    animation:fadeIn 2s ease;
}

.hero h1{
    font-size:90px;
    line-height:1.2;
    font-weight:800;
    margin-bottom:30px;
    background:linear-gradient(to right,#38bdf8,#67e8f9,#06b6d4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero p{
    font-size:26px;
    line-height:2;
    color:#cbd5e1;
    margin-bottom:50px;
}

.btn{
    display:inline-block;
    padding:18px 45px;
    background:linear-gradient(45deg,#06b6d4,#3b82f6);
    color:white;
    border-radius:50px;
    text-decoration:none;
    font-size:20px;
    font-weight:600;
    transition:0.4s;
    box-shadow:0 0 30px rgba(59,130,246,0.5);
}

.btn:hover{
    transform:scale(1.08);
    box-shadow:0 0 60px rgba(59,130,246,0.9);
}

/* Fade Animation */

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(50px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Common Section */

section{
    padding:120px 8%;
}

.section-title{
    text-align:center;
    font-size:60px;
    margin-bottom:80px;
    color:#38bdf8;
    position:relative;
}

.section-title::after{
    content:'';
    position:absolute;
    width:120px;
    height:5px;
    background:#06b6d4;
    left:50%;
    transform:translateX(-50%);
    bottom:-15px;
    border-radius:20px;
}

/* About */

.about{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    align-items:center;
}

.about img{
    width:100%;
    border-radius:25px;
    transition:0.5s;
    box-shadow:0 0 40px rgba(14,165,233,0.3);
}

.about img:hover{
    transform:scale(1.03);
}

.about-text{
    font-size:22px;
    line-height:2;
    color:#cbd5e1;
}

/* Courses */

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:35px;
}

.card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    padding:40px;
    border-radius:25px;
    backdrop-filter:blur(15px);
    transition:0.5s;
}

.card:hover{
    transform:translateY(-15px);
    box-shadow:0 0 40px rgba(14,165,233,0.4);
    background:rgba(255,255,255,0.08);
}

.card h3{
    font-size:32px;
    margin-bottom:20px;
    color:#22d3ee;
}

.card p{
    color:#cbd5e1;
    line-height:1.9;
}

/* Stats */

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:35px;
}

.stat-box{
    background:#0f172a;
    padding:50px;
    border-radius:30px;
    text-align:center;
    transition:0.5s;
}

.stat-box:hover{
    transform:scale(1.06);
    box-shadow:0 0 35px rgba(14,165,233,0.4);
}

.stat-box h2{
    font-size:65px;
    color:#38bdf8;
}

.stat-box p{
    margin-top:15px;
    font-size:24px;
    color:#cbd5e1;
}

/* Placement */

.placement{
    background:linear-gradient(135deg,#111827,#0f172a);
    padding:80px;
    border-radius:35px;
    text-align:center;
    box-shadow:0 0 40px rgba(14,165,233,0.15);
}

.placement h2{
    font-size:60px;
    margin-bottom:35px;
    color:#38bdf8;
}

.placement p{
    font-size:24px;
    line-height:2;
    color:#cbd5e1;
}

/* Testimonials */

.testimonials{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:35px;
}

.testimonial{
    background:#111827;
    padding:40px;
    border-radius:25px;
    transition:0.5s;
}

.testimonial:hover{
    transform:translateY(-12px);
    box-shadow:0 0 30px rgba(14,165,233,0.3);
}

.testimonial h3{
    color:#38bdf8;
    margin-bottom:20px;
    font-size:28px;
}

.testimonial p{
    line-height:1.9;
    color:#cbd5e1;
}

/* Gallery */

.gallery{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:30px;
}

.gallery img{
    width:100%;
    border-radius:25px;
    transition:0.5s;
}

.gallery img:hover{
    transform:scale(1.05);
}

/* Contact */

.contact{
    background:#0f172a;
    padding:80px;
    border-radius:35px;
    text-align:center;
}

.contact h2{
    font-size:55px;
    margin-bottom:35px;
    color:#38bdf8;
}

.contact p{
    font-size:24px;
    color:#cbd5e1;
    margin-bottom:18px;
}

/* Footer */

footer{
    background:#01040b;
    padding:35px;
    text-align:center;
    color:#94a3b8;
    font-size:18px;
}

/* Responsive */

@media(max-width:950px){

    .hero h1{
        font-size:55px;
    }

    .hero p{
        font-size:19px;
    }

    .about{
        grid-template-columns:1fr;
    }

    nav{
        flex-direction:column;
        gap:20px;
    }

    nav ul{
        flex-wrap:wrap;
        justify-content:center;
    }

}

</style>

</head>

<body>

<div class="bg-animation">
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
</div>

<nav>

<div class="logo">PATHNEX</div>

<ul>
<li><a href="#">Home</a></li>
<li><a href="#">Courses</a></li>
<li><a href="#">Placements</a></li>
<li><a href="#">Success</a></li>
<li><a href="#">Gallery</a></li>
<li><a href="#">Contact</a></li>
</ul>

</nav>

<section class="hero">

<div class="hero-content">

<h1>Build Your Career With Pathnex</h1>

<p>

Faridabad's Most Advanced DevOps Training & Placement Institute.

Learn Linux, AWS, Docker, Kubernetes, Jenkins, Terraform, CI/CD, Monitoring and Real Production-Level DevOps Projects with Industry Experts.

Get Placement Assistance & Crack Top MNC Interviews.

</p>

<a href="#" class="btn">Start Your DevOps Journey</a>

</div>

</section>

<section>

<h2 class="section-title">About Pathnex</h2>

<div class="about">

<img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop">

<div class="about-text">

Pathnex is a professional DevOps Training & Placement Center located in Faridabad, Haryana.

We focus on practical DevOps learning with real-time industry projects.

Students work on live CI/CD pipelines, Kubernetes deployments, AWS cloud infrastructure and monitoring tools exactly like production environments.

We prepare students for real company interviews with:
<br><br>

✔ Mock Interviews  
✔ Resume Building  
✔ LinkedIn Optimization  
✔ Live Production Projects  
✔ Company Referral Support  
✔ One-to-One Mentorship  
✔ Daily Practice Sessions  
✔ Cloud Labs & Assignments  

</div>

</div>

</section>

<section>

<h2 class="section-title">Our Courses</h2>

<div class="cards">

<div class="card">
<h3>Linux</h3>
<p>Master Linux administration, permissions, scripting and production troubleshooting.</p>
</div>

<div class="card">
<h3>AWS Cloud</h3>
<p>Learn complete AWS cloud infrastructure and deployment architecture.</p>
</div>

<div class="card">
<h3>Docker</h3>
<p>Containerize applications and manage enterprise-level deployments.</p>
</div>

<div class="card">
<h3>Kubernetes</h3>
<p>Master Pods, Deployments, Services, Ingress and Helm Charts.</p>
</div>

<div class="card">
<h3>CI/CD Pipeline</h3>
<p>Build complete Jenkins automation pipelines with GitHub & Docker.</p>
</div>

<div class="card">
<h3>Terraform</h3>
<p>Provision cloud infrastructure using Infrastructure as Code.</p>
</div>

<div class="card">
<h3>Monitoring</h3>
<p>Prometheus, Grafana, ELK Stack and enterprise monitoring solutions.</p>
</div>

<div class="card">
<h3>Placement Preparation</h3>
<p>Mock interviews, HR preparation and company interview guidance.</p>
</div>

</div>

</section>

<section>

<h2 class="section-title">Our Achievements</h2>

<div class="stats">

<div class="stat-box">
<h2>1500+</h2>
<p>Students Trained</p>
</div>

<div class="stat-box">
<h2>500+</h2>
<p>Placements Done</p>
</div>

<div class="stat-box">
<h2>100+</h2>
<p>Live Projects</p>
</div>

<div class="stat-box">
<h2>50+</h2>
<p>Hiring Partners</p>
</div>

</div>

</section>

<section>

<div class="placement">

<h2>100% Placement Assistance</h2>

<p>

At Pathnex, we not only teach technologies but also transform students into professional DevOps Engineers.

Students get:
<br><br>

✔ Real Production Experience  
✔ Resume Preparation  
✔ Interview Sessions  
✔ Cloud Projects  
✔ Company Referrals  
✔ Placement Support  

Our students are working as:
<br><br>

DevOps Engineers  
Cloud Engineers  
SRE Engineers  
Platform Engineers  
AWS Engineers  

</p>

</div>

</section>

<section>

<h2 class="section-title">Student Success Stories</h2>

<div class="testimonials">

<div class="testimonial">
<h3>Rahul Sharma</h3>
<p>
"Pathnex changed my career completely. I learned DevOps practically and got placed in a top MNC."
</p>
</div>

<div class="testimonial">
<h3>Ankit Verma</h3>
<p>
"Best DevOps institute in Faridabad. The real projects and CI/CD pipeline practice helped me crack interviews."
</p>
</div>

<div class="testimonial">
<h3>Priya Yadav</h3>
<p>
"The Kubernetes and AWS training was amazing. Highly recommended for DevOps aspirants."
</p>
</div>

</div>

</section>

<section>

<h2 class="section-title">Campus Gallery</h2>

<div class="gallery">

<img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop">

<img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=2070&auto=format&fit=crop">

<img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?q=80&w=2070&auto=format&fit=crop">

</div>

</section>

<section>

<div class="contact">

<h2>Contact Pathnex</h2>

<p>📍 Faridabad, Haryana, India</p>
<p>📞 +91 XXXXX XXXXX</p>
<p>📧 support@pathnex.com</p>
<p>🌐 DevOps Training & Placement Center</p>

</div>

</section>

<footer>

© 2026 PATHNEX | DevOps Training & Placement Center | Faridabad

</footer>

</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
