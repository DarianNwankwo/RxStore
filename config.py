import argparse
import os


from hashlib import sha1
from math import log


PORT_BEGIN = 10000
RING_SCALE_CONSTANT = 2


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = basedir + "/databases"


class Config:
    PORT = None
    SECRET_KEY = os.environ.get("SECRET_KEY") or "rxstore-like-no-other-baby-but-seriously-set-a-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @classmethod
    def update_port(cls, port):
        cls.PORT = port
        cls.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, f"app{cls.PORT}.db")


def initialize():
    """Sets up each flask app to follow the chord protocol."""
    parser = argparse.ArgumentParser(
        description="Creates an m = (log N) + {} bit identifier circle for N nodes.".format(RING_SCALE_CONSTANT)
        )
    parser.add_argument("--numnodes", help="the number of nodes for the identifier circle", required=True)
    num_of_nodes = int(parser.parse_args().numnodes)
    ports = generate_peers(num_of_nodes)
    return ports


def generate_peers(n):
    """Generates port (nodes) values evenly-ish separated amongst the identifier circle."""
    m = log(n, 2) + RING_SCALE_CONSTANT # m-bit value
    ports = [PORT_BEGIN + (pow(2, RING_SCALE_CONSTANT) * p) for p in range(n)]
    return ports


