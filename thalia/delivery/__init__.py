from flask import Flask
from delivery.orderCont import order
from delivery.reportCont import report
from delivery.searchCont import search
from delivery.seatingCont import seating
from delivery.showCont import show_main
from delivery.ticketCont import ticket

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

"""Header of Blueprints used in flask"""

# other requests
app.register_blueprint(show_main, url_prefix='/thalia/shows')
app.register_blueprint(order, url_prefix='/thalia')
app.register_blueprint(seating, url_prefix='/thalia')
app.register_blueprint(ticket, url_prefix='/thalia/tickets')
app.register_blueprint(report, url_prefix='/thalia/reports')
app.register_blueprint(search, url_prefix='/thalia')
