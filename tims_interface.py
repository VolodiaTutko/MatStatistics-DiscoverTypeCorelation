from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
import pygame
import icons
import sys
from main import *
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.main = Main()
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(679, 528)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.Table = QTableWidget(Dialog)
        if (self.Table.columnCount() < 3):
            self.Table.setColumnCount(3)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(90, 255, 178));
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(208, 208, 208));
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(208, 208, 208));
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.Table.rowCount() < 7):
            self.Table.setRowCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(6, __qtablewidgetitem9)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        self.populateTable()




        self.Table.setObjectName(u"Table")
        self.Table.setGeometry(QRect(0, 0, 301, 271))
        self.Table.setFont(font)
        self.Table.setLayoutDirection(Qt.LeftToRight)
        self.Table.setAutoFillBackground(False)
        self.Table.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"color:rgb(255, 255, 255)\n"
"\n"
"")
        self.Table.horizontalHeader().setVisible(False)
        self.Table.horizontalHeader().setCascadingSectionResizes(False)
        self.Table.verticalHeader().setVisible(False)
        self.equation_label = QLabel(Dialog)
        self.equation_label.setObjectName(u"equation_label")
        self.equation_label.setGeometry(QRect(350, 10, 271, 31))
        self.equation_label.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 10pt \"Script MT Bold\";\n"
"\n"
"\n"
"")
        self.equations = QLabel(Dialog)
        self.equations.setObjectName(u"equations")
        self.equations.setGeometry(QRect(350, 50, 271, 91))
        self.equations.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 10pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.A_ = QLabel(Dialog)
        self.A_.setObjectName(u"A_")
        self.A_.setGeometry(QRect(380, 170, 61, 31))
        self.A_.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.A_value = QLabel(Dialog)
        self.A_value.setObjectName(u"A_value")
        self.A_value.setGeometry(QRect(470, 170, 91, 31))
        self.A_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")

        self.B_value = QLabel(Dialog)
        self.B_value.setObjectName(u"B_value")
        self.B_value.setGeometry(QRect(470, 210, 91, 31))
        self.B_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.B_ = QLabel(Dialog)
        self.B_.setObjectName(u"B_")
        self.B_.setGeometry(QRect(380, 210, 61, 31))
        self.B_.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.fx = QLabel(Dialog)
        self.fx.setObjectName(u"fx")
        self.fx.setGeometry(QRect(310, 300, 51, 31))
        self.fx.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.fx_value = QLabel(Dialog)
        self.fx_value.setObjectName(u"fx_value")
        self.fx_value.setGeometry(QRect(380, 300, 261, 31))
        self.fx_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.sigma = QLabel(Dialog)
        self.sigma.setObjectName(u"sigma")
        self.sigma.setGeometry(QRect(380, 400, 71, 31))
        self.sigma.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.delta = QLabel(Dialog)
        self.delta.setObjectName(u"delta")
        self.delta.setGeometry(QRect(380, 450, 71, 31))
        self.delta.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.sigma_value = QLabel(Dialog)
        self.sigma_value.setObjectName(u"sigma_value")
        self.sigma_value.setGeometry(QRect(490, 400, 91, 31))
        self.sigma_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.delta_value = QLabel(Dialog)
        self.delta_value.setObjectName(u"delta_value")
        self.delta_value.setGeometry(QRect(490, 450, 91, 31))
        self.delta_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.Graphic1 = QPushButton(Dialog)
        self.Graphic1.setObjectName(u"Graphic1")
        self.Graphic1.setGeometry(QRect(20, 300, 221, 51))
        self.Graphic1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"font: 700 8pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.Graphic2 = QPushButton(Dialog)
        self.Graphic2.setObjectName(u"Graphic2")
        self.Graphic2.setGeometry(QRect(380, 350, 181, 41))
        self.Graphic2.setStyleSheet(u"border-radius: 4px;\n"
"font: 700 8pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 400, 221, 51))
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 italic 10pt \"Segoe UI\";")
        self.Calculate= QPushButton(Dialog)
        self.Calculate.setObjectName(u"pushButton")
        self.Calculate.setGeometry(QRect(250, 400, 121, 51))
        self.Calculate.setStyleSheet(u"/*background-color: rgba(255, 255, 255,200);*/\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "font: 700 8pt \"Georgia\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color:qlineargradient(spread:pad, x1:0.682, y1:0.284, x2:1, y2:0.0454545, stop:0.613636 rgba(4, 1, 106, 240))")

        self.EditMatrix = QPushButton(Dialog)
        self.EditMatrix.setObjectName(u"Graphic2_2")
        self.EditMatrix.setGeometry(QRect(-10, 490, 691, 41))
        self.EditMatrix.setStyleSheet(u"/*border-radius: 20px;*/\n"
                                      "font: 700 10pt \"Script MT Bold\";\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
                                      "color: rgb(9, 13, 1);\n"
                                      "border:none")

        # self.Restart = QPushButton(Dialog)
        # self.Restart.setObjectName(u"pushButton_2")
        # self.Restart.setGeometry(QRect(305, 11, 41, 31))
        # icon = QIcon()
        # icon.addFile(u":/icon/images/icons8-restart.svg", QSize(), QIcon.Normal, QIcon.Off)
        # self.Restart.setIcon(icon)


        self.labelC = QLabel(Dialog)
        self.labelC.setObjectName(u"B_1")
        self.labelC.setGeometry(QRect(380, 250, 61, 31))
        self.labelC.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
                                  "font: 700 11pt \"Segoe UI\";\n")
        self.C_value = QLabel(Dialog)
        self.C_value.setObjectName(u"B_value_2")
        self.C_value.setGeometry(QRect(470, 250, 91, 31))
        self.C_value.setStyleSheet(u"background-color: rgba(255, 255, 255,155);\n"
                                     "font: 700 11pt \"Segoe UI\";\n")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def populateTable(self):

        table_data = self.main.Table()


        table_widget = self.Table


        table_widget.setRowCount(table_data.shape[0])
        table_widget.setColumnCount(table_data.shape[1])



        for i, row in enumerate(table_data.values, start =-1):
            if i == 0:
                item1 = QTableWidgetItem("   X")
                table_widget.setItem(0, 0, item1)

                item1 = QTableWidgetItem("   Y-")
                table_widget.setItem(0, 1, item1)

                item1 = QTableWidgetItem("   Ni")
                table_widget.setItem(0, 2, item1)


            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(i+1, j, item)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))


        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)

        self.Table.setSortingEnabled(__sortingEnabled)

        self.equation_label.setText(QCoreApplication.translate("Dialog", u"         \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0440\u0456\u0432\u043d\u044f\u043d\u044c ", None))
        self.equations.setText(QCoreApplication.translate("Dialog", u"{}".format(""), None))
        self.A_.setText(QCoreApplication.translate("Dialog", u" A   =", None))
        self.A_value.setText(QCoreApplication.translate("Dialog", u"  {}".format(0), None))
        self.B_value.setText(QCoreApplication.translate("Dialog", u"  {}".format(0), None))
        self.B_.setText(QCoreApplication.translate("Dialog", u" B   =", None))
        self.fx.setText(QCoreApplication.translate("Dialog", u" f(x) =", None))
        self.fx_value.setText(QCoreApplication.translate("Dialog", u" {}".format(0),None))
        self.sigma.setText(QCoreApplication.translate("Dialog", u"  \u03c3^2  =", None))
        self.delta.setText(QCoreApplication.translate("Dialog", u"   \u03b4^2  =", None))
        self.sigma_value.setText(QCoreApplication.translate("Dialog", u"   {}".format(0), None))
        self.delta_value.setText(QCoreApplication.translate("Dialog", u"   {}".format(0), None))
        self.Graphic1.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0431\u0443\u0434\u0443\u0432\u0430\u0442\u0438 \u0433\u0440\u0430\u0444\u0456\u043a \u0442\u043e\u0447\u043e\u043a M(x;y)", None))
        self.Graphic2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0431\u0443\u0434\u0443\u0432\u0430\u0442\u0438 \u0433\u0440\u0430\u0444\u0456\u043a f(x)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0430\u0431\u043e\u043b\u0456\u0447\u043d\u0430 \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0456\u044f", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0413\u0456\u043f\u0435\u0440\u0431\u043e\u043b\u0456\u0447\u043d\u0430 \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0456\u044f", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0430\u0437\u043d\u0438\u043a\u043e\u0432\u0430 \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0456\u044f", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u041a\u043e\u0440\u0435\u043d\u0435\u0432\u0430 \u043a\u043e\u0440\u0435\u043b\u044f\u0446\u0456\u044f", None))
        self.Calculate.setText(QCoreApplication.translate("Dialog", u"\u041e\u0411\u0427\u0418\u0421\u041b\u0418\u0422\u0418", None))
        self.labelC.setText(QCoreApplication.translate("Dialog", u" C   =", None))
        self.C_value.setText(QCoreApplication.translate("Dialog", u"  0", None))
        self.EditMatrix.setText(QCoreApplication.translate("Dialog",
                                                           u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438 \u0432\u0445\u0456\u0434\u043d\u0443 \u043c\u0430\u0442\u0440\u0438\u0446\u044e",
                                                           None))
        self.Calculate.clicked.connect(self.handle_calculate)
        self.EditMatrix.clicked.connect(self.NewMatrix_Calculate)
        self.Graphic1.clicked.connect(self.main.GraphicM3)
        # self.Restart.setText("")
        # self.Restart.clicked.connect(self.populateTable)

    def Type_corelation(self):
        index = self.comboBox.currentIndex()
        if index == 2:
            return self.main.system_eq3(), self.main.A_value3(),self.main.B_value3(), self.main.fx_value3(),self.main.Sigma_value3(),self.main.Delta_value3(),self.main.GraphicM3, self.main.Graphic_fx3,0
        elif index == 3:
            return self.main.system_eq4(), self.main.A_value4(), self.main.B_value4(), self.main.fx_value4(), self.main.Sigma_value4(), self.main.Delta_value4(),self.main.GraphicM4, self.main.Graphic_fx4,0

        elif index == 1:
            return self.main.system_eq2(), self.main.A_value2(), self.main.B_value2(), self.main.fx_value2(), self.main.Sigma_value2(), self.main.Delta_value2(),self.main.GraphicM2, self.main.Graphic_fx2,0
        elif index == 0:
            return self.main.system_eq(), self.main.A_value(), self.main.B_value(), self.main.fx_value(), self.main.Sigma_value(), self.main.Delta_value(), self.main.GraphicM, self.main.Graphic_fx,self.main.C_value()
    def handle_calculate(self):
        data = self.Type_corelation()

        # Update the UI with the returned data
        self.equations.setText(QCoreApplication.translate("Dialog", u"{}".format(data[0]), None))
        self.A_value.setText(QCoreApplication.translate("Dialog", u"  {}".format(data[1]), None))
        self.B_value.setText(QCoreApplication.translate("Dialog", u"  {}".format(data[2]), None))
        self.fx_value.setText(QCoreApplication.translate("Dialog", u" {}".format(data[3]), None))
        self.sigma_value.setText(QCoreApplication.translate("Dialog", u"   {}".format(data[4]), None))
        self.delta_value.setText(QCoreApplication.translate("Dialog", u"   {}".format(data[5]), None))
        # self.Graphic1.clicked.connect(data[6])
        self.Graphic2.clicked.connect(data[7])
        self.C_value.setText(QCoreApplication.translate("Dialog", u"  {}".format(data[8]), None))
        self.populateTable()

    def NewMatrix_Calculate(self):
        self.main.EditFile()
        self.handle_calculate()






class Interface:
    def __init__(self):
        self.dialog = QDialog()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self.dialog)

if not QApplication.instance():
    app =QApplication(sys.argv)
else:
    app = QApplication.instance()

pygame.mixer.init()
pygame.mixer.music.load("David Guetta and Bebe Rexha - I'm Good (Blue) (minus 2).mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
sound2 = pygame.mixer.Sound('вступ.mp3')
sound2.play()
program = Interface()
program.dialog.show()

sys.exit(app.exec())
