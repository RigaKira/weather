import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>680</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QCalendarWidget" name="calendarWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>30</y>
     <width>312</width>
     <height>183</height>
    </rect>
   </property>
  </widget>
  <widget class="QTimeEdit" name="timeEdit">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>301</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>230</y>
     <width>281</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QListWidget" name="eventList">
   <property name="geometry">
    <rect>
     <x>350</x>
     <y>20</y>
     <width>281</width>
     <height>251</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="addEventBtn">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>260</y>
     <width>281</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавить событие</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.stonesInGame = 0
        self.addEventBtn.clicked.connect(self.f)

    def f(self):
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        s = f"{date.toString(format('yyyy-MM-dd'))} {time.toString(format("HH:mm:ss"))} - {self.lineEdit.text()}"
        self.eventList.addItem(s)
        self.eventList.setSortingEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SimplePlanner()
    ex.show()

    sys.exit(app.exec())