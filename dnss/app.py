from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

courses = {
    "1": {
        "title": "Digital Marketing Basics",
        "price": 100,
        "includes": [
            "Digital Marketing Introduction",
            "How Online Business Works",
            "Beginner Guide PDF"
        ],
        "best_for": "Absolute Beginners"
    },
    "2": {
        "title": "Social Media Marketing",
        "price": 200,
        "includes": [
            "Instagram Growth Strategy",
            "Facebook Page Setup",
            "10 Content Ideas"
        ]
    },
    "3": {
        "title": "Content Creation Mastery",
        "price": 300,
        "includes": [
            "Reels & Short Video Strategy",
            "Hashtag Research Method",
            "Viral Post Hooks"
        ]
    },
    "4": {
        "title": "Graphic Designing Mastery",
        "price": 500,
        "includes": [
            "Learn Design with Canva & Photoshop",
            "Reel Thumbnail Design",
            "Branding Basics",
            "50 Content Templates"
        ],
        "best_for": "Freelancers / Creatives"
    },
    "5": {
        "title": "Digital Product Selling Mastery",
        "price": 700,
        "includes": [
            "How to Create Digital Products",
            "Setting up Mocks & Stores",
            "Marketing Digital Goods",
            "Sales Psychology"
        ]
    },
    "6": {
        "title": "SEO & Google Ads Course",
        "price": 800,
        "includes": [
            "Search Engine Optimization basics",
            "Google Keyword Layouts",
            "Running your first Ad Campaign",
            "Local Business SEO"
        ]
    },
    "7": {
        "title": "WordPress Mastery Course",
        "price": 1000,
        "includes": [
            "Build Any Website Without Coding",
            "Domain & Hosting Setup",
            "Theme Customization",
            "E-commerce Store Creation"
        ],
        "best_for": "Entrepreneurs / Agencies"
    },
    "8": {
        "title": "Lead Generation Mastery",
        "price": 1200,
        "includes": [
            "High-Converting Landing Pages",
            "WhatsApp Marketing",
            "Funnel Introduction",
            "50 B2B Lead Ideas"
        ]
    },
    "9": {
        "title": "Facebook & Instagram Ads",
        "price": 1500,
        "includes": [
            "Facebook Ads Manager Setup",
            "Campaign Creation",
            "Audience Targeting",
            "Ad Copywriting",
            "Budget Optimization"
        ]
    },
    "10": {
        "title": "All-in-One Digital Marketing Mastery",
        "price": 2000,
        "includes": [
            "100% Practical Training",
            "Social Media Marketing",
            "Facebook & Google Ads",
            "SEO & Lead Generation",
            "Affiliate Marketing",
            "Freelancing Cashflow Methods"
        ],
        "bonus": [
            "1000 Content Ideas",
            "Client Proposal Templates",
            "Certificate of Completion",
            "Lifetime Access to Material"
        ],
        "best_for": "Serious Professionals"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def course_page():
    return render_template("courses.html",courses=courses)

@app.route("/course/<id>")
def detail(id):
    return render_template("course_detail.html",
                           course=courses[id],
                           id=id)

@app.route("/payment/<id>")
def payment(id):
    return render_template("payment.html",
                           course=courses[id])

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/refund")
def refund():
    return render_template("refund.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/shipping")
def shipping():
    return render_template("shipping.html")

app.run(debug=True)