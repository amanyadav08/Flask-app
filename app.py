from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Pathnex | DevOps Training & Placement Center</title>

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

/* Scrollbar */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#06b6d4;
    border-radius:20px;
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
    background:rgba(2,6,23,0.85);
    backdrop-filter:blur(10px);
}

.logo{
    font-size:38px;
    font-weight:800;
    color:#38bdf8;
}

nav ul{
    display:flex;
    gap:35px;
    list-style:none;
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
    height:100vh;
    background:
    linear-gradient(rgba(2,6,23,0.75),rgba(2,6,23,0.9)),
    url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop') center/cover;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:40px;
    position:relative;
}

.hero::before{
    content:'';
    position:absolute;
    width:500px;
    height:500px;
    background:#06b6d4;
    filter:blur(180px);
    opacity:0.25;
    animation:float 6s infinite ease-in-out;
}

@keyframes float{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-30px);}
    100%{transform:translateY(0px);}
}

.hero-content{
    max-width:1000px;
    z-index:10;
}

.hero h1{
    font-size:85px;
    font-weight:800;
    line-height:1.2;
    margin-bottom:25px;
    background:linear-gradient(to right,#38bdf8,#22d3ee,#67e8f9);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation:fadeIn 2s ease;
}

.hero p{
    font-size:25px;
    line-height:1.8;
    color:#cbd5e1;
    margin-bottom:45px;
    animation:fadeIn 3s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(40px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

.btn{
    padding:18px 45px;
    background:linear-gradient(45deg,#06b6d4,#0ea5e9);
    border:none;
    border-radius:50px;
    color:white;
    font-size:20px;
    cursor:pointer;
    text-decoration:none;
    transition:0.4s;
    box-shadow:0 0 25px rgba(14,165,233,0.5);
}

.btn:hover{
    transform:scale(1.08);
    box-shadow:0 0 45px rgba(14,165,233,0.9);
}

/* Section */

section{
    padding:120px 8%;
}

.section-title{
    text-align:center;
    font-size:60px;
    margin-bottom:70px;
    color:#38bdf8;
    position:relative;
}

.section-title::after{
    content:'';
    width:120px;
    height:5px;
    background:#06b6d4;
    position:absolute;
    left:50%;
    transform:translateX(-50%);
    bottom:-15px;
    border-radius:10px;
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
    transition:0.4s;
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
    border:1px solid rgba(255,255,255,0.1);
    padding:40px;
    border-radius:25px;
    transition:0.4s;
    backdrop-filter:blur(10px);
}

.card:hover{
    transform:translateY(-15px);
    background:rgba(255,255,255,0.1);
    box-shadow:0 0 30px rgba(14,165,233,0.4);
}

.card h3{
    font-size:30px;
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
    gap:30px;
}

.stat-box{
    background:#0f172a;
    padding:50px;
    border-radius:25px;
    text-align:center;
    transition:0.4s;
}

.stat-box:hover{
    transform:scale(1.05);
}

.stat-box h2{
    font-size:60px;
    color:#38bdf8;
}

.stat-box p{
    margin-top:15px;
    font-size:22px;
    color:#cbd5e1;
}

/* Placement */

.placement{
    background:linear-gradient(135deg,#0f172a,#111827);
    padding:70px;
    border-radius:30px;
    text-align:center;
}

.placement h2{
    font-size:55px;
    color:#38bdf8;
    margin-bottom:30px;
}

.placement p{
    font-size:24px;
    line-height:2;
    color:#cbd5e1;
}

/* Testimonials */

.testimonials{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:30px;
}

.testimonial{
    background:#111827;
    padding:35px;
    border-radius:25px;
    transition:0.4s;
}

.testimonial:hover{
    transform:translateY(-10px);
}

.testimonial h3{
    color:#38bdf8;
    margin-bottom:20px;
}

.testimonial p{
    line-height:1.8;
    color:#cbd5e1;
}

/* Contact */

.contact{
    text-align:center;
    background:#0f172a;
    padding:70px;
    border-radius:30px;
}

.contact h2{
    font-size:50px;
    margin-bottom:30px;
    color:#38bdf8;
}

.contact p{
    font-size:24px;
    margin-bottom:15px;
    color:#cbd5e1;
}

/* Footer */

footer{
    padding:35px;
    text-align:center;
    background:#01040b;
    color:#94a3b8;
    font-size:18px;
}

/* Responsive */

@media(max-width:950px){

    .hero h1{
        font-size:50px;
    }

    .hero p{
        font-size:18px;
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

<nav>
    <div class="logo">PATHNEX</div>

    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Courses</a></li>
        <li><a href="#">Placements</a></li>
        <li><a href="#">Success</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

<section class="hero">

<div class="hero-content">

<h1>Become a DevOps Engineer with Pathnex</h1>

<p>
Faridabad's Leading DevOps Training & Placement Institute.
Learn Real-Time DevOps Tools with Industry Experts and Get Placement Support in Top IT Companies.
</p>

<a href="#" class="btn">Start Your DevOps Journey</a>

</div>

</section>

<section>

<h2 class="section-title">About Pathnex</h2>

<div class="about">

<img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop">

<div class="about-text">

Pathnex is a modern DevOps Training and Placement Center located in Faridabad, Haryana.

We provide industry-level practical training on Linux, AWS, Docker, Kubernetes, Jenkins, Terraform, Git, Monitoring Tools, and CI/CD Pipelines.

Students work on real-world projects and production-level environments to gain actual company experience.

We focus on:
<br><br>

✔ Real-Time Projects  
✔ Mock Interviews  
✔ Resume Preparation  
✔ Placement Assistance  
✔ Production Environment Practice  
✔ Live Classes & Mentorship  

</div>

</div>

</section>

<section>

<h2 class="section-title">Our DevOps Courses</h2>

<div class="cards">

<div class="card">
<h3>Linux Administration</h3>
<p>Master Linux commands, shell scripting, permissions, processes and server management.</p>
</div>

<div class="card">
<h3>AWS Cloud</h3>
<p>Learn EC2, IAM, VPC, S3, Load Balancer, Auto Scaling and real cloud deployments.</p>
</div>

<div class="card">
<h3>Docker</h3>
<p>Containerize applications and deploy production-ready environments using Docker.</p>
</div>

<div class="card">
<h3>Kubernetes</h3>
<p>Master Pods, Deployments, Services, Ingress, Helm Charts and Kubernetes Architecture.</p>
</div>

<div class="card">
<h3>Jenkins CI/CD</h3>
<p>Build automated pipelines using Jenkins, GitHub Webhooks and Docker deployments.</p>
</div>

<div class="card">
<h3>Terraform</h3>
<p>Automate complete AWS infrastructure using Infrastructure as Code.</p>
</div>

<div class="card">
<h3>Monitoring Tools</h3>
<p>Prometheus, Grafana and monitoring production systems like real DevOps Engineers.</p>
</div>

<div class="card">
<h3>Interview Preparation</h3>
<p>Mock interviews, resume building and placement preparation sessions.</p>
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
At Pathnex, we not only teach DevOps technologies but also prepare students for real company environments.

Students receive:
<br><br>

✔ Resume Building  
✔ LinkedIn Optimization  
✔ Mock Interviews  
✔ HR Preparation  
✔ Real Production Projects  
✔ Company Referrals  

Our students are working as:
<br><br>

DevOps Engineers  
Cloud Engineers  
SRE Engineers  
AWS Engineers  
Platform Engineers  

</p>

</div>

</section>

<section>

<h2 class="section-title">Student Success Stories</h2>

<div class="testimonials">

<div class="testimonial">
<h3>Rahul Sharma</h3>
<p>
"Pathnex completely changed my career. I learned DevOps from scratch and got placed in an MNC as a DevOps Engineer."
</p>
</div>

<div class="testimonial">
<h3>Ankit Verma</h3>
<p>
"The practical training and real projects helped me crack interviews easily. Highly recommended institute."
</p>
</div>

<div class="testimonial">
<h3>Priya Yadav</h3>
<p>
"Best DevOps institute in Faridabad. The CI/CD and Kubernetes training was amazing."
</p>
</div>

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
