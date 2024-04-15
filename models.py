# Models for pet adoption agency 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()
        

class Pet(db.Model):
    """ Pet model """
    
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)    
    photo_url = db.Column(db.Text,
                          nullable=True,
                          default="https://cdn-icons-png.freepik.com/512/7104/7104446.png")
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True) 
    
    def __repr__(self):
        """ Show pet name, species and availability """
        return f'<{self.name} the {self.species} is available: {self.available}>'
        