from PyQt5 import QtWidgets
from app import App
import sys



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()