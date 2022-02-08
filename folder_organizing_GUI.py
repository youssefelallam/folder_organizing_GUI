import os
import shutil
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 152)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked=lambda:self.Brows())
        self.pushButton.setGeometry(QtCore.QRect(320, 50, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked=lambda:self.start())
        self.pushButton_2.setGeometry(QtCore.QRect(130, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.label.setText(_translate("Dialog", "Folder Organizing"))
        self.pushButton_2.setText(_translate("Dialog", "Start"))
    
    def Brows(self):
        save_place = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(save_place)
    
    def start(self):
        current_dir = self.lineEdit.text()

        for filename in os.listdir(current_dir):
            if filename.endswith(("png","jpg","jpeg","gif")):
                if not os.path.exists(current_dir+"/Images"):
                    os.mkdir(current_dir+"/Images")
                shutil.move(current_dir+"/"+filename, current_dir+"/Images")

            if filename.endswith(("deb","exe","dmg")):
                if not os.path.exists(current_dir+"/Apps"):
                    os.mkdir(current_dir+"/Apps")
                shutil.move(current_dir+"/"+filename, current_dir+"/Apps")
            
            if filename.endswith(("pdf")):
                if not os.path.exists(current_dir+"/PDF"):
                    os.mkdir(current_dir+"/PDF")
                shutil.move(current_dir+"/"+filename, current_dir+"/PDF")
            
            if filename.endswith(("doc","docx","xlsx","xls","pptx","ppt")):
                if not os.path.exists(current_dir+"/Documents"):
                    os.mkdir(current_dir+"/Documents")
                shutil.move(current_dir+"/"+filename, current_dir+"/Documents")

            if filename.endswith(("zip","tar","gz","rar")):
                if not os.path.exists(current_dir+"/Archives"):
                    os.mkdir(current_dir+"/Archives")
                shutil.move(current_dir+"/"+filename, current_dir+"/Archives")
        print("Done")
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
