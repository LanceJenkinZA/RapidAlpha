import logging

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from RapidDelegate import RapidDelegate

def main():
    logger = logging.getLogger("Alpha")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(filename)s - "
                                  "%(levelname)s - %(message)s")
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    app = QApplication([])
    alpha = RapidDelegate()

    app.exec_()

if __name__ == "__main__":
    main()
