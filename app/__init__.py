from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config, initialize, generate_peers
from app.node import Node
from threading import Thread
from flask import g


apps = []
chord_node = None
nodes = dict()
app = Flask(__name__)
for port in initialize():
    chord_node = Node(port, None, None)
    nodes[ str(port) ] = chord_node
    # print(f"Here is app before import: {app}")
    # Config.update_port(port)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    login.login_view = "login"
    login.login_message = "Please log in to access this page."
    bootstrap = Bootstrap(str(port), app)
    app.chord_node = chord_node
    from app import routes, models
    # Thread(target=app.run, kwargs={"port":port}).start()
    apps.append([app, chord_node])  
