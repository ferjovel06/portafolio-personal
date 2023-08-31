from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Create a route / that renders home.html template
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)