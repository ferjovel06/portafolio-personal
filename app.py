from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__)

# Create a route / that renders home.html template
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)