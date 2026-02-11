
def create_app(env=None):
    from flask import Flask, jsonify
    from flask_cors import CORS
    from flask_restx import Api
    from app.api.routes import ns as person_ns
    from app.config import config_by_name
    from app.extensions import db, ma
    from sqlalchemy import text
    import logging

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect Person API", version="0.0.1")

    CORS(app)  # Set CORS for development

    api.add_namespace(person_ns)
    db.init_app(app)

    ma.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    @app.route("/db")
    def db_status():
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("*** DB STATUS ERMITTELN ***")
        result_schema = db.session.execute(text("SELECT current_schema()")).first()
        if result_schema is not None:
            schema = result_schema[0]
            logging.debug("db schema: %s", schema)
        result_db = db.session.execute(text("SELECT current_database()")).first()
        if result_db is not None:
            dbname = result_db[0]
            logging.debug("db name: %s", dbname)
        result_table = db.session.execute(text("SELECT schemaname, tablename FROM pg_tables WHERE tablename = 'person'")).first()
        if result_table is not None:
            schema_name = result_table[0]
            table_name = result_table[1]
            logging.debug("schema: %s , table: %s", schema_name, table_name)

        return jsonify("db status OK")

    return app
