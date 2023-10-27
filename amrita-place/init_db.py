from models import *
from database import init_db

# in models.py, change "from amrita_place.database import Base" to "from database import Base" when executing this. Revert afterwards.
init_db()