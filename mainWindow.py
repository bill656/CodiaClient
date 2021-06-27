# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowMain(object):
    def setupUi(self, windowMain):
        windowMain.setObjectName("windowMain")
        windowMain.resize(1080, 740)
        windowMain.setMinimumSize(QtCore.QSize(1080, 740))
        windowMain.setMaximumSize(QtCore.QSize(1280, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowMain.setWindowIcon(icon)
        windowMain.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(windowMain)
        self.centralwidget.setObjectName("centralwidget")
        self.framePack = QtWidgets.QFrame(self.centralwidget)
        self.framePack.setGeometry(QtCore.QRect(0, 0, 1080, 768))
        self.framePack.setMinimumSize(QtCore.QSize(1080, 768))
        self.framePack.setMaximumSize(QtCore.QSize(1280, 768))
        self.framePack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framePack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePack.setObjectName("framePack")
        self.listWidgetPack = QtWidgets.QListWidget(self.framePack)
        self.listWidgetPack.setGeometry(QtCore.QRect(28, 30, 1024, 531))
        self.listWidgetPack.setMaximumSize(QtCore.QSize(1280, 768))
        self.listWidgetPack.setObjectName("listWidgetPack")
        self.pushButtonPackOK = NewPushButton(self.framePack)
        self.pushButtonPackOK.setGeometry(QtCore.QRect(480, 630, 120, 32))
        self.pushButtonPackOK.setObjectName("pushButtonPackOK")
        self.pushButtonPackNext = NewPushButton(self.framePack)
        self.pushButtonPackNext.setGeometry(QtCore.QRect(730, 630, 120, 32))
        self.pushButtonPackNext.setObjectName("pushButtonPackNext")
        self.pushButtonPackPrevious = NewPushButton(self.framePack)
        self.pushButtonPackPrevious.setGeometry(QtCore.QRect(230, 630, 120, 32))
        self.pushButtonPackPrevious.setObjectName("pushButtonPackPrevious")
        self.labelPackPage = QtWidgets.QLabel(self.framePack)
        self.labelPackPage.setGeometry(QtCore.QRect(50, 630, 120, 32))
        self.labelPackPage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPackPage.setObjectName("labelPackPage")
        self.progressBarPack = NewProgressBar(self.framePack)
        self.progressBarPack.setGeometry(QtCore.QRect(180, 9, 720, 12))
        self.progressBarPack.setProperty("value", 0)
        self.progressBarPack.setTextVisible(False)
        self.progressBarPack.setObjectName("progressBarPack")
        self.frameExercise = QtWidgets.QFrame(self.centralwidget)
        self.frameExercise.setGeometry(QtCore.QRect(0, 0, 1080, 768))
        self.frameExercise.setMinimumSize(QtCore.QSize(1080, 768))
        self.frameExercise.setMaximumSize(QtCore.QSize(1280, 768))
        self.frameExercise.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameExercise.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameExercise.setObjectName("frameExercise")
        self.pushButtonExerciseOK = NewPushButton(self.frameExercise)
        self.pushButtonExerciseOK.setGeometry(QtCore.QRect(480, 630, 120, 32))
        self.pushButtonExerciseOK.setObjectName("pushButtonExerciseOK")
        self.pushButtonExerciseReturn = NewPushButton(self.frameExercise)
        self.pushButtonExerciseReturn.setGeometry(QtCore.QRect(890, 630, 120, 32))
        self.pushButtonExerciseReturn.setObjectName("pushButtonExerciseReturn")
        self.listWidgetExercise = QtWidgets.QListWidget(self.frameExercise)
        self.listWidgetExercise.setGeometry(QtCore.QRect(28, 170, 1024, 391))
        self.listWidgetExercise.setObjectName("listWidgetExercise")
        self.pushButtonExerciseBegin = NewPushButton(self.frameExercise)
        self.pushButtonExerciseBegin.setGeometry(QtCore.QRect(50, 630, 120, 32))
        self.pushButtonExerciseBegin.setObjectName("pushButtonExerciseBegin")
        self.labelDeadline = QtWidgets.QLabel(self.frameExercise)
        self.labelDeadline.setGeometry(QtCore.QRect(780, 580, 280, 32))
        self.labelDeadline.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDeadline.setIndent(10)
        self.labelDeadline.setObjectName("labelDeadline")
        self.progressBarExercise = NewProgressBar(self.frameExercise)
        self.progressBarExercise.setGeometry(QtCore.QRect(180, 9, 720, 12))
        self.progressBarExercise.setProperty("value", 0)
        self.progressBarExercise.setTextVisible(False)
        self.progressBarExercise.setObjectName("progressBarExercise")
        self.textEditExerciseDiscription = QtWidgets.QTextEdit(self.frameExercise)
        self.textEditExerciseDiscription.setGeometry(QtCore.QRect(28, 30, 1024, 141))
        self.textEditExerciseDiscription.setReadOnly(True)
        self.textEditExerciseDiscription.setObjectName("textEditExerciseDiscription")
        self.pushButtonExerciseOK.raise_()
        self.pushButtonExerciseReturn.raise_()
        self.listWidgetExercise.raise_()
        self.pushButtonExerciseBegin.raise_()
        self.labelDeadline.raise_()
        self.textEditExerciseDiscription.raise_()
        self.progressBarExercise.raise_()
        self.frameQuestion = QtWidgets.QFrame(self.centralwidget)
        self.frameQuestion.setGeometry(QtCore.QRect(0, 0, 1080, 768))
        self.frameQuestion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameQuestion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameQuestion.setObjectName("frameQuestion")
        self.textEditQuestionDiscription = QtWidgets.QTextEdit(self.frameQuestion)
        self.textEditQuestionDiscription.setGeometry(QtCore.QRect(28, 30, 1024, 531))
        self.textEditQuestionDiscription.setReadOnly(True)
        self.textEditQuestionDiscription.setObjectName("textEditQuestionDiscription")
        self.pushButtonSubmit = NewPushButton(self.frameQuestion)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(563, 630, 120, 32))
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        self.pushButtonHistory = NewPushButton(self.frameQuestion)
        self.pushButtonHistory.setGeometry(QtCore.QRect(50, 630, 120, 32))
        self.pushButtonHistory.setObjectName("pushButtonHistory")
        self.pushButtonQuestionReturn = NewPushButton(self.frameQuestion)
        self.pushButtonQuestionReturn.setGeometry(QtCore.QRect(890, 630, 120, 32))
        self.pushButtonQuestionReturn.setObjectName("pushButtonQuestionReturn")
        self.labelQuestionStatus = QtWidgets.QLabel(self.frameQuestion)
        self.labelQuestionStatus.setGeometry(QtCore.QRect(30, 0, 150, 30))
        self.labelQuestionStatus.setObjectName("labelQuestionStatus")
        self.pushButtonSubmitFile = NewPushButton(self.frameQuestion)
        self.pushButtonSubmitFile.setGeometry(QtCore.QRect(397, 630, 120, 32))
        self.pushButtonSubmitFile.setObjectName("pushButtonSubmitFile")
        self.comboBoxLanguage = QtWidgets.QComboBox(self.frameQuestion)
        self.comboBoxLanguage.setGeometry(QtCore.QRect(920, 0, 132, 30))
        self.comboBoxLanguage.setObjectName("comboBoxLanguage")
        self.comboBoxLanguage.addItem("")
        self.frameSubmit = QtWidgets.QFrame(self.centralwidget)
        self.frameSubmit.setGeometry(QtCore.QRect(0, 0, 1080, 768))
        self.frameSubmit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameSubmit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSubmit.setObjectName("frameSubmit")
        self.comboBoxLanguageSubmit = QtWidgets.QComboBox(self.frameSubmit)
        self.comboBoxLanguageSubmit.setGeometry(QtCore.QRect(920, 0, 132, 30))
        self.comboBoxLanguageSubmit.setObjectName("comboBoxLanguageSubmit")
        self.comboBoxLanguageSubmit.addItem("")
        self.labelSubmitStatus = QtWidgets.QLabel(self.frameSubmit)
        self.labelSubmitStatus.setGeometry(QtCore.QRect(30, 0, 150, 30))
        self.labelSubmitStatus.setObjectName("labelSubmitStatus")
        self.textEditSubmit = QtWidgets.QTextEdit(self.frameSubmit)
        self.textEditSubmit.setGeometry(QtCore.QRect(28, 30, 1024, 531))
        self.textEditSubmit.setTabStopWidth(40)
        self.textEditSubmit.setObjectName("textEditSubmit")
        self.pushButtonSubmitCode = NewPushButton(self.frameSubmit)
        self.pushButtonSubmitCode.setGeometry(QtCore.QRect(480, 630, 120, 32))
        self.pushButtonSubmitCode.setObjectName("pushButtonSubmitCode")
        self.pushButtonSubmitBack = NewPushButton(self.frameSubmit)
        self.pushButtonSubmitBack.setGeometry(QtCore.QRect(890, 630, 120, 32))
        self.pushButtonSubmitBack.setObjectName("pushButtonSubmitBack")
        self.pushButtonReadFromFile = QtWidgets.QPushButton(self.frameSubmit)
        self.pushButtonReadFromFile.setGeometry(QtCore.QRect(690, 630, 120, 32))
        self.pushButtonReadFromFile.setObjectName("pushButtonReadFromFile")
        self.frameHistory = QtWidgets.QFrame(self.centralwidget)
        self.frameHistory.setGeometry(QtCore.QRect(0, 0, 1080, 768))
        self.frameHistory.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameHistory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHistory.setObjectName("frameHistory")
        self.listWidgetPackHistory = QtWidgets.QListWidget(self.frameHistory)
        self.listWidgetPackHistory.setGeometry(QtCore.QRect(28, 30, 1024, 531))
        self.listWidgetPackHistory.setMaximumSize(QtCore.QSize(1280, 768))
        self.listWidgetPackHistory.setObjectName("listWidgetPackHistory")
        self.pushButtonSubmitCodeDetails = NewPushButton(self.frameHistory)
        self.pushButtonSubmitCodeDetails.setGeometry(QtCore.QRect(480, 630, 120, 32))
        self.pushButtonSubmitCodeDetails.setObjectName("pushButtonSubmitCodeDetails")
        self.pushButtonHistoryBack = NewPushButton(self.frameHistory)
        self.pushButtonHistoryBack.setGeometry(QtCore.QRect(890, 630, 120, 32))
        self.pushButtonHistoryBack.setObjectName("pushButtonHistoryBack")
        self.framePack.raise_()
        self.frameExercise.raise_()
        self.frameSubmit.raise_()
        self.frameQuestion.raise_()
        self.frameHistory.raise_()
        windowMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 24))
        self.menubar.setObjectName("menubar")
        windowMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowMain)
        self.statusbar.setObjectName("statusbar")
        windowMain.setStatusBar(self.statusbar)

        self.retranslateUi(windowMain)
        QtCore.QMetaObject.connectSlotsByName(windowMain)

    def retranslateUi(self, windowMain):
        _translate = QtCore.QCoreApplication.translate
        windowMain.setWindowTitle(_translate("windowMain", "题包列表"))
        self.pushButtonPackOK.setText(_translate("windowMain", "确认"))
        self.pushButtonPackNext.setText(_translate("windowMain", "下一页"))
        self.pushButtonPackPrevious.setText(_translate("windowMain", "上一页"))
        self.labelPackPage.setText(_translate("windowMain", "第 1 页"))
        self.pushButtonExerciseOK.setText(_translate("windowMain", "确认"))
        self.pushButtonExerciseReturn.setText(_translate("windowMain", "返回"))
        self.pushButtonExerciseBegin.setText(_translate("windowMain", "开始题包"))
        self.labelDeadline.setText(_translate("windowMain", "截止日期：无限制"))
        self.pushButtonSubmit.setText(_translate("windowMain", "提交代码"))
        self.pushButtonHistory.setText(_translate("windowMain", "历史记录"))
        self.pushButtonQuestionReturn.setText(_translate("windowMain", "返回"))
        self.labelQuestionStatus.setText(_translate("windowMain", "通过/尝试："))
        self.pushButtonSubmitFile.setText(_translate("windowMain", "提交文件"))
        self.comboBoxLanguage.setItemText(0, _translate("windowMain", "请选择提交语言"))
        self.comboBoxLanguageSubmit.setItemText(0, _translate("windowMain", "请选择提交语言"))
        self.labelSubmitStatus.setText(_translate("windowMain", "通过/尝试"))
        self.pushButtonSubmitCode.setText(_translate("windowMain", "提交"))
        self.pushButtonSubmitBack.setText(_translate("windowMain", "返回"))
        self.pushButtonReadFromFile.setText(_translate("windowMain", "从文件中读取"))
        self.pushButtonSubmitCodeDetails.setText(_translate("windowMain", "详细信息"))
        self.pushButtonHistoryBack.setText(_translate("windowMain", "返回"))
from codiaclientgui.utils import NewProgressBar, NewPushButton
