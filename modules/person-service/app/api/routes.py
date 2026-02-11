# REST controller

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List
from app.model.person import Person
from app.schema.person_schema import PersonSchema
from app.service.person_service import PersonService

ns = Namespace("UdaConnectPerson", description="Connections via geolocation.", path="/api")  # noqa

@ns.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema(many=True))
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@ns.route("/persons/<person_id>")
@ns.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person

