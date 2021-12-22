from flask import Flask, request
from flask.json import jsonify
from  models import *
from command_handler import command_handler
from query_handler import query_handler

app = Flask(__name__)
app.register_blueprint(command_handler)
app.register_blueprint(query_handler)
app.config['SQLALCHEMY_BINDS'] = {
    'event_store': 'sqlite:///event_store.sqlite3',
    'prescriptions': 'sqlite:///prescriptions.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def setup_db():
    db.init_app(app)
    db.create_all()


@app.route('/prescriptions/log_audit', methods=['GET'])
def show_transactions():
    query = EventStore.query
    return jsonify([event.to_dict() for event in query.all()])


if __name__ == '__main__':
    app.run(port=5002, debug=True, host="0.0.0.0")
