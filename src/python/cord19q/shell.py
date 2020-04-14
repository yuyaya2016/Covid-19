"""
cord19 query shell module.
"""

import sys

from cmd import Cmd

from .models import Models
from .query import Query

class Shell(Cmd):
    """
    cord19 query shell.
    """

    def __init__(self, path):
        super(Shell, self).__init__()

        self.intro = "cord19 query shell"
        self.prompt = "(c19q) "

        self.embeddings = None
        self.db = None
        self.path = path

    def preloop(self):
        # Load embeddings and questions.db
        self.embeddings, self.db = Models.load(self.path)

    def postloop(self):
        Models.close(self.db)

    def default(self, line):
        Query.query(self.embeddings, self.db, line, None)

def main(path):
    """
    Shell execution loop.

    Args:
        path: model path
    """

    Shell(path).cmdloop()

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
