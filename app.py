from PyQt5 import QtWidgets
from layout import Ui_MainWindow
import serial.tools.list_ports

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        # UI Setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Variables
        self.list_of_comports = []
        self.list_of_removed = []

        # Init
        self.init()

        # Buttons
        self.ui.RefreshButton.clicked.connect(self.upldate_list_of_comports)
        self.ui.ExitButton.clicked.connect(self.exit)

    def init(self)->None:
        self.list_of_comports = self.get_list_of_comport()
        for port in self.list_of_comports:
            self.ui.addPort(port)

    def exit(self)->None:
        """
        Exit
        """
        self.close()

    def get_list_of_comport(self)->list:
        """
        Get a list of comports
        """
        list_ports_string = list()
        for port in serial.tools.list_ports.comports():
            list_ports_string.append(str(port))
        return list_ports_string

    def upldate_list_of_comports(self):
        current_list = self.get_list_of_comport()
        # Add new comports to list
        for port in current_list:
            if port in self.list_of_removed:
                self.ui.removeStyle(port)
                self.list_of_removed.remove(port)
            if port not in self.list_of_comports and port not in self.list_of_removed:
                self.list_of_comports.append(port)
                self.ui.addPort(port)
        # Remove comports removed from list and add to new list
        for port in self.list_of_comports:
            if port not in current_list:
                self.list_of_comports.remove(port)
                self.list_of_removed.append(port)
                self.ui.removePort(port)
        