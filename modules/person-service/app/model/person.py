from app.extensions import db  # noqa

class Person(db.Model):
    __tablename__ = "person"
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)

