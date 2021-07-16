from app import app
from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()

geary = Pet(name="Geary", species="cat", age='adult', available=False )
john = Pet(name="John", species="dog", age='young', available=True )
sonic = Pet(name="Sonic", species="hedgehog", age='senior', notes="goes fast", available=True )
tails = Pet(name="Tails", species="fox", age='baby', notes="has two tails" )

db.session.add_all([geary, john, sonic, tails])
db.session.commit()