class Node:
    """Represents a node in the chord protocol."""


    def __init__(self, port, id, finger_table):
        self.port = port
        self.id = id
        self.finger_table = finger_table