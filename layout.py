# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LayOut.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 142)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.ComportLabel = QtWidgets.QLabel(self.centralwidget)
        #self.ComportLabel.setObjectName("ComportLabel")
        #self.horizontalLayout.addWidget(self.ComportLabel)
        #self.Description = QtWidgets.QLineEdit(self.centralwidget)
        #self.Description.setObjectName("Description")
        #self.horizontalLayout.addWidget(self.Description)
        self.list_of_comports = list()
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.horizontalLayout_2.addWidget(self.RefreshButton)
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout_2.addWidget(self.ExitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.ComportLabel.setText(_translate("MainWindow", "ComPort"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh ComPort List"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))

    def addPort(self,label):
        label = label
        _translate = QtCore.QCoreApplication.translate
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ComportLabel = QtWidgets.QLabel(self.centralwidget)
        self.ComportLabel.setObjectName(label)
        self.horizontalLayout.addWidget(self.ComportLabel)
        self.Description = QtWidgets.QLineEdit(self.centralwidget)
        self.Description.setObjectName("Description"+label)
        self.horizontalLayout.addWidget(self.Description)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ComportLabel.setText(_translate("MainWindow", label))
        self.list_of_comports.append(self.ComportLabel)
        
        
    def removePort(self,rp):
        for p in self.list_of_comports:
            if p.text() in rp:
                p.setStyleSheet("background-color: red")
    
    def removeStyle(self,rp):
        for p in self.list_of_comports:
            if p.text() in rp:
                p.setStyleSheet("")