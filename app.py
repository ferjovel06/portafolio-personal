from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create an instance of Flask
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
# Initialize the database
db = SQLAlchemy(app)


# Create db model
class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image = db.Column(db.LargeBinary)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a function to return a string when we add something
    def formatted_content(self):
        return self.content.replace("\n", "<br>")

    def __repr__(self):
        return '<Name %r>' % self.id


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    image = db.Column(db.LargeBinary)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a function to return a string when we add something
    def formatted_content(self):
        return self.content.replace("\n", "<br>")

    def __repr__(self):
        return '<Name %r>' % self.id


def get_skills_image_path(image_id):
    image = Skills.query.filter_by(id=image_id).first()
    return image.image


def get_projects_image_path(image_id):
    image = Skills.query.filter_by(id=image_id).first()
    return image.image


# Create the database tables
with app.app_context():
    result = db.create_all()


# Create a route / that renders home.html template
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
