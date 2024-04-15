# Pet Adoption Agency App

from flask import Flask, redirect, render_template, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm, EditPetForm

def create_app(database_name, testing=False):

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = "secret"
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # connect_db(app)
    # db.create_all() 

    debug = DebugToolbarExtension(app)
        
    @app.route('/')
    def show_home():
        """ Show homepage of available pets """
        pets = Pet.query.order_by(Pet.name).all()
        return render_template('home.html', pets=pets)
    
    @app.route('/add', methods=['GET', 'POST'])
    def add_new_pet():
        """ Handle form to add new pet """
        form = AddPetForm()
        
        if form.validate_on_submit():
            name = form.name.data
            species = form.species.data
            url = form.photo_url.data or None
            age = form.age.data or None
            notes = form.notes.data
            pet = Pet(name=name, species=species, photo_url=url, age=age, notes=notes)
            db.session.add(pet)
            db.session.commit()
            flash(f"{name} was added to the list!")
            return redirect("/")

        else:
            return render_template(
                "add_pet.html", form=form)
    
    @app.route('/<int:pid>', methods=['GET', 'POST'])
    def pet_details(pid):
        """ Show and edit details about pet """
        pet = Pet.query.get_or_404(pid)
        form = EditPetForm(obj=pet)
        
        if form.validate_on_submit():
            pet.photo_url = form.photo_url.data
            pet.notes = form.notes.data
            pet.available = form.available.data
            db.session.commit()
            flash(f"{pet.name}'s profile was updated!")
            return redirect('/')
        else:
            return render_template('pet_info.html', pet=pet, form=form)
    
    return app

if __name__ == 'app':
    app = create_app('adoptions')   # Here we are creating an instance of "app"
    connect_db(app)                # We call "connect_db(app)" here
    app.run(debug=True)