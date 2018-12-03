# """
# Author: Darian Osahar Nwankwo
# Date: November 08, 2018
# Description: Web application for patient prescription management based on the Chord protocol
# """
# import argparse


# from flask import Flask, render_template
# from hashlib import sha1
# from math import log
# from multiprocessing import Process


# app = Flask(__name__)


# PORT_BEGIN = 10000
# RING_SCALE_CONSTANT = 2


# ########################################################################################################################
# # Chord setup below
# ########################################################################################################################
# def initialize():
#     """Sets up each flask app to follow the chord protocol."""
#     parser = argparse.ArgumentParser(
#         description="Creates an m = (log N) + {} bit identifier circle for N nodes.".format(RING_SCALE_CONSTANT)
#         )
#     parser.add_argument("--numnodes", help="the number of nodes for the identifier circle", required=True)
#     num_of_nodes = int(parser.parse_args().numnodes)
#     ports = generatePeers(num_of_nodes)
#     return ports


# def generatePeers(n):
#     """Generates port (nodes) values evenly-ish separated amongst the identifier circle."""
#     m = log(n, 2) + RING_SCALE_CONSTANT # m-bit value
#     ports = [PORT_BEGIN + (pow(2, RING_SCALE_CONSTANT) * p) for p in range(n)]
#     return ports


# ########################################################################################################################
# # Web server setup below
# ########################################################################################################################
# def launch(port):
#     """Spawns a separate process for each instance of RxStore running the Chord protocol."""
#     app = Flask( __name__ + str(port) )
#     @app.route("/")
#     def index():
#         return render_template("index.html")


#     @app.route("/contact")
#     def contact():
#         return render_template("contact.html")

#     app.run(host="0.0.0.0", port=port, debug=False)


# if __name__ == "__main__":
#     ports = initialize()
#     nodes = []
#     for i in range(len(ports)):
#         # print(str(ports[i]))

#         rxstore = Process(target=launch, args=(ports[i],) )
#         nodes.append(rxstore)
#         rxstore.start()
from app import apps, db
from app.models import Prescription, Patient, Doctor, Pharmacist
# from app.node import Node
# from config import initialize

# ports = initialize()
# for p in ports:
#     pass


from threading import Thread


for app, node in apps:
    # app.debug = True
    # app.use_reloader= False
    # from app import routes, models
    Thread(target=app.run, kwargs={"port": node.port}).start()
    # pass
    
    
    # app.run(port=node.port)

# print(apps)
# Thread(target=apps[0][0].run, kwargs={"port": 5000}).start()
# Thread(target=apps[1][0].run, kwargs={"port": 5050}).start()


# Thread(target=app.run, kwargs={"port":5000}).start()
# Thread(target=app.run, kwargs={"port":5010}).start()
# app.run()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Patient": Patient, "Prescription": Prescription, "Doctor": Doctor, "Pharmacist": Pharmacist}