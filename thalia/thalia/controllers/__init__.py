from flask import Flask

from thalia.controllers.controller import main
from thalia.controllers.showCont import show_main
from thalia.controllers.seatingCont import seating
from thalia.controllers.ticketCont import ticket
from thalia.controllers.orderCont import order
from thalia.controllers.reportCont import report
from thalia.controllers.searchCont import search

app = Flask(__name__)

"""Header of Blueprints used in flask"""

# reusable requests
app.register_blueprint(main, url_prefix='/thalia/shows')
app.register_blueprint(main, url_prefix='/thalia/seating')
app.register_blueprint(main, url_prefix='/thalia/orders')

# other requests
app.register_blueprint(show_main, url_prefix='/thalia/shows')
app.register_blueprint(order, url_prefix='/thalia')
app.register_blueprint(seating, url_prefix='/thalia')
app.register_blueprint(ticket, url_prefix='/thalia/tickets')
app.register_blueprint(report, url_prefix='/thalia/reports')
app.register_blueprint(search, url_prefix='/thalia')
