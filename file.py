import sys
import os


class File:
    def __init__(self, name):
        self.name = name

    def resource_path(self):
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, os.path.abspath(self.name))
