from marshmallow_sqlalchemy import auto_field

from app.model.person import Person
from app.extensions import db, ma

class PersonSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    company_name = auto_field()

    class Meta:
        model = Person
#        sqla_session = db.session
#        load_instance = True

