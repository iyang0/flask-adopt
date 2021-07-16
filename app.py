"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet, PetEditForm

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
    
    # if user submitted the form, add it to database, otherwise just render the form
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(
            name=name, 
            species=species, 
            photo_url=photo_url, 
            age=age, 
            notes=notes
            )
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect("/") 

    else:
        return render_template("pet-new-form.html", form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Show form to edit pet details and process form"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetEditForm(obj = pet)

    #if form is submitted, edit the database, otherwise just render page.
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f'/{pet_id}')

    else:
        return render_template("pet-detail.html", pet=pet, form=form)