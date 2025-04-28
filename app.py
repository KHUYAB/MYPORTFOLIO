from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '188a4ba320e79190bdf7'  # Still needed for CSRF protection in forms

# Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects Page Route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Skills Page Route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Run the Flask Application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # para gumana sa Vercel
    app.run(host='0.0.0.0', port=port)
