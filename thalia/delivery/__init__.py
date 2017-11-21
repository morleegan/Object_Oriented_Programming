from flask import Flask
from delivery.blueprints import show_main, seating, ticket, search, report, order

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

"""Header of Blueprints used in flask"""

# other requests
app.register_blueprint(show_main, url_prefix='/thalia')
app.register_blueprint(order, url_prefix='/thalia')
app.register_blueprint(seating, url_prefix='/thalia')
app.register_blueprint(ticket, url_prefix='/thalia')
app.register_blueprint(report, url_prefix='/thalia')
app.register_blueprint(search, url_prefix='/thalia')
