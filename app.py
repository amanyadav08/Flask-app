from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Pathnex - DevOps Training & Placement Center</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    background:#0f172a;
    color:white;
}

/* Navbar */

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:25px 8%;
    background:rgba(15,23,42,0.95);
    position:sticky;
    top:0;
    z-index:1000;
}

.logo{
    font-size:32px;
    font-weight:700;
    color:#38bdf8;
}

nav ul{
    display:flex;
    list-style:none;
    gap:30px;
}

nav ul li a{
    color:white;
    text-decoration:none;
    transition:0.3s;
}

nav ul li a:hover{
    color:#38bdf8;
}

/* Hero Section */

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    background:
    linear-gradient(rgba(15,23,42,0.8),rgba(15,23,42,0.9)),
    url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop') center/cover;
    padding:50px;
}

.hero-content{
    max-width:900px;
}

.hero h1{
    font-size:70px;
    margin-bottom:20px;
    color:#38bdf8;
}

.hero p{
    font-size:24px;
    line-height:1.7;
    color:#e2e8f0;
    margin-bottom:40px;
}

.btn{
    display:inline-block;
    padding:16px 40px;
    background:#06b6d4;
    color:white;
    text-decoration:none;
    border-radius:12px;
    font-size:20px;
    transition:0.3s;
    font-weight:600;
}

.btn:hover{
    background:#0891b2;
    transform:scale(1.05);
}

/* About */

.section{
    padding:100px 8%;
}

.section-title{
    text-align:center;
    font-size:50px;
    margin-bottom:60px;
    color:#38bdf8;
}

.about{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:50px;
    align-items:center;
}

.about img{
    width:100%;
    border-radius:20px;
}

.about-text{
    font-size:20px;
    line-height:1.9;
    color:#cbd5e1;
}

/* Courses */

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:30px;
}

.card{
    background:#1e293b;
    padding:40px 30px;
    border-radius:20px;
    transition:0.3s;
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

.card:hover{
    transform:translateY(-10px);
    background:#334155;
}

.card h3{
    font-size:28px;
    margin-bottom:20px;
    color:#22d3ee;
}

.card p{
    color:#cbd5e1;
    line-height:1.7;
}

/* Placement */

.placement{
    background:#111827;
    border-radius:25px;
    padding:60px;
    text-align:center;
}

.placement h2{
    font-size:45px;
    margin-bottom:25px;
    color:#38bdf8;
}

.placement p{
    font-size:22px;
    color:#e2e8f0;
    line-height:1.8;
}

/* Contact */

.contact-box{
    background:#1e293b;
    padding:50px;
    border-radius:25px;
    text-align:center;
}

.contact-box h2{
    font-size:40px;
    margin-bottom:30px;
    color:#38bdf8;
}

.contact-box p{
    font-size:22px;
    margin-bottom:15px;
    color:#cbd5e1;
}

/* Footer */

footer{
    background:#020617;
    padding:30px;
    text-align:center;
    color:#94a3b8;
    margin-top:50px;
}

@media(max-width:900px){

    .hero h1{
        font-size:45px;
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

}

</style>

</head>

<body>

<nav>
    <div class="logo">Pathnex</div>

    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Courses</a></li>
        <li><a href="#">Placements</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

<section class="hero">

    <div class="hero-content">

        <h1>Pathnex DevOps Training & Placement Center</h1>

        <p>
            Learn Real-Time DevOps Technologies with Industry Experts and
            Get 100% Placement Assistance in Top IT Companies.
            Located in Faridabad, Haryana.
        </p>

        <a href="#" class="btn">Start Your Career</a>

    </div>

</section>

<section class="section">

    <h2 class="section-title">About Pathnex</h2>

    <div class="about">

        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop">

        <div class="about-text">

            Pathnex is a professional DevOps Training and Placement Institute
            in Faridabad where students learn practical industry-level skills.

            We provide real-time projects, interview preparation,
            resume building, mock interviews, and placement support.

            Our mission is to transform beginners into highly skilled
            DevOps Engineers.

        </div>

    </div>

</section>

<section class="section">

    <h2 class="section-title">Our Courses</h2>

    <div class="cards">

        <div class="card">
            <h3>Linux</h3>
            <p>Master Linux administration and shell scripting from beginner to advanced level.</p>
        </div>

        <div class="card">
            <h3>AWS Cloud</h3>
            <p>Learn EC2, VPC, IAM, S3, Load Balancer, Auto Scaling and complete cloud infrastructure.</p>
        </div>

        <div class="card">
            <h3>Docker & Kubernetes</h3>
            <p>Containerization and orchestration with real-time deployment projects.</p>
        </div>

        <div class="card">
            <h3>CI/CD Pipeline</h3>
            <p>Build complete automation pipelines using Jenkins, GitHub and Docker.</p>
        </div>

        <div class="card">
            <h3>Terraform</h3>
            <p>Infrastructure as Code using Terraform with AWS cloud automation.</p>
        </div>

        <div class="card">
            <h3>Monitoring</h3>
            <p>Prometheus, Grafana and monitoring tools used in production environments.</p>
        </div>

    </div>

</section>

<section class="section">

    <div class="placement">

        <h2>Placement Assistance</h2>

        <p>
            We help students prepare for interviews with mock sessions,
            real DevOps projects, resume preparation and company referrals.
            Our students are working in top IT companies as DevOps Engineers,
            Cloud Engineers and Site Reliability Engineers.
        </p>

    </div>

</section>

<section class="section">

    <div class="contact-box">

        <h2>Contact Us</h2>

        <p>📍 Pathnex Training Center, Faridabad, Haryana</p>
        <p>📞 +91 XXXXX XXXXX</p>
        <p>📧 support@pathnex.com</p>

    </div>

</section>

<footer>

    © 2026 Pathnex | DevOps Training & Placement Center

</footer>

</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
