# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'functionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_functionWindow(object):
    def setupUi(self, functionWindow):
        functionWindow.setObjectName("functionWindow")
        functionWindow.resize(1000, 720)
        functionWindow.setMaximumSize(QtCore.QSize(1000, 720))
        functionWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(functionWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_packlist = QtWidgets.QFrame(self.centralwidget)
        self.frame_packlist.setGeometry(QtCore.QRect(0, 0, 1000, 720))
        self.frame_packlist.setMaximumSize(QtCore.QSize(1000, 720))
        self.frame_packlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_packlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_packlist.setObjectName("frame_packlist")
        self.listWidget_packs = QtWidgets.QListWidget(self.frame_packlist)
        self.listWidget_packs.setGeometry(QtCore.QRect(0, 0, 750, 600))
        self.listWidget_packs.setObjectName("listWidget_packs")
        self.pushButton_pack_OK = QtWidgets.QPushButton(self.frame_packlist)
        self.pushButton_pack_OK.setGeometry(QtCore.QRect(810, 240, 113, 32))
        self.pushButton_pack_OK.setObjectName("pushButton_pack_OK")
        self.pushButton_next = QtWidgets.QPushButton(self.frame_packlist)
        self.pushButton_next.setGeometry(QtCore.QRect(810, 330, 113, 32))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_last = QtWidgets.QPushButton(self.frame_packlist)
        self.pushButton_last.setGeometry(QtCore.QRect(810, 420, 113, 32))
        self.pushButton_last.setObjectName("pushButton_last")
        self.frame_questionlist = QtWidgets.QFrame(self.centralwidget)
        self.frame_questionlist.setGeometry(QtCore.QRect(0, 0, 1000, 720))
        self.frame_questionlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_questionlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionlist.setObjectName("frame_questionlist")
        self.pushButton_questionlist_OK = QtWidgets.QPushButton(self.frame_questionlist)
        self.pushButton_questionlist_OK.setGeometry(QtCore.QRect(810, 240, 113, 32))
        self.pushButton_questionlist_OK.setObjectName("pushButton_questionlist_OK")
        self.pushButton_questionlist_Back = QtWidgets.QPushButton(self.frame_questionlist)
        self.pushButton_questionlist_Back.setGeometry(QtCore.QRect(810, 420, 113, 32))
        self.pushButton_questionlist_Back.setObjectName("pushButton_questionlist_Back")
        self.listWidget_questions = QtWidgets.QListWidget(self.frame_questionlist)
        self.listWidget_questions.setGeometry(QtCore.QRect(0, 0, 750, 600))
        self.listWidget_questions.setObjectName("listWidget_questions")
        self.pushButton_Beginpack = QtWidgets.QPushButton(self.frame_questionlist)
        self.pushButton_Beginpack.setGeometry(QtCore.QRect(810, 150, 113, 32))
        self.pushButton_Beginpack.setObjectName("pushButton_Beginpack")
        functionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(functionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        functionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(functionWindow)
        self.statusbar.setObjectName("statusbar")
        functionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(functionWindow)
        QtCore.QMetaObject.connectSlotsByName(functionWindow)

    def retranslateUi(self, functionWindow):
        _translate = QtCore.QCoreApplication.translate
        functionWindow.setWindowTitle(_translate("functionWindow", "题包列表"))
        self.pushButton_pack_OK.setText(_translate("functionWindow", "确认"))
        self.pushButton_next.setText(_translate("functionWindow", "下一页"))
        self.pushButton_last.setText(_translate("functionWindow", "上一页"))
        self.pushButton_questionlist_OK.setText(_translate("functionWindow", "确认"))
        self.pushButton_questionlist_Back.setText(_translate("functionWindow", "返回"))
        self.pushButton_Beginpack.setText(_translate("functionWindow", "开始题包"))
