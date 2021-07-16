"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


@app.route("/")
def root():
    """homepage, will list the pets as well as name, photo, and avaliability"""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

    
@app.route("/add", methods=["GET", "POST"])
def pet_new_form():
    """create a form to add a new pet to database"""
    form = AddPet()
    # breakpoint()
    
    if form.validate_on_submit():
        
        print("AAAAAAAAAAAAAAAAAAAA THE FORM IS ", form.name.data)
        name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        
        # new_pet = Pet(name=name, 
            # species=species, 
            # photo_url=photo_url, 
            # age=age, 
            # notes=notes)
        # db.session.add(new_pet)
        # db.session.commit()
        
       return redirect("/") 
    else:
        return render_template("pet-new-form.html", form=form)