import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QWidget, QMainWindow


class Add_Film(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Добавить элемент')
        self.add.clicked.connect(self.new_coffee)

    def new_coffee(self):
        ID = self.ID.text()
        Sort = self.Sort.text()
        Power = self.Power.text()
        Grains = self.Grains.text()
        Taste = self.Taste.text()
        Price = self.Price.text()
        Volume = self.Volume.text()
        con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        cur.execute("INSERT INTO coffee VALUES (?,?,?,?,?,?,?)",
                    (int(ID), Sort, float(Power), Grains, Taste, int(Price), int(Volume)))
        con.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.show_btn.clicked.connect(self.show)
        self.add_btn.clicked.connect(self.add)

    def show(self):
        con = sqlite3.connect("coffee")
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM Coffee""").fetchall()
        con.close()
        self.Vuvod.setColumnCount(8)
        self.Vuvod.setRowCount(len(res))
        self.Vuvod.setHorizontalHeaderLabels(
            ["№", "ID", "Название сорта", "Степень обжарки", "Молотый", "Вкус", "Цена", "Объем"])
        for x in range(1, len(res) + 1):
            self.Vuvod.setItem(x - 1, 0, QTableWidgetItem(str(x)))
            self.Vuvod.setItem(x - 1, 1, QTableWidgetItem(res[x - 1][0]))
            self.Vuvod.setItem(x - 1, 2, QTableWidgetItem(res[x - 1][1]))
            self.Vuvod.setItem(x - 1, 3, QTableWidgetItem(res[x - 1][2]))
            self.Vuvod.setItem(x - 1, 4, QTableWidgetItem(res[x - 1][3]))
            self.Vuvod.setItem(x - 1, 5, QTableWidgetItem(res[x - 1][4]))
            self.Vuvod.setItem(x - 1, 5, QTableWidgetItem(res[x - 1][5]))
            self.Vuvod.setItem(x - 1, 5, QTableWidgetItem(res[x - 1][6]))
            self.Vuvod.setItem(x - 1, 5, QTableWidgetItem(res[x - 1][7]))

    def add(self):
        self.new_wid = Add_Film()
        self.new_wid.show()
        self.show()

def exception_hook(cls, exception, traceback):
    sys.__exception_hook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
