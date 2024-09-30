from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel
from PyQt5.QtCore import QTime, QTimer, QDate, Qt

class Hauptfenster(QLCDNumber):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digitaluhr")
        self.resize(300, 130)
                
        self.setSegmentStyle(QLCDNumber.Filled)
        self.doppelpunkt = False
        
        self.datum_label = QLabel(self)
        self.datum_label.setText("Leftclick for Date")
        
        self.timer_datum = QTimer(self)
        self.timer_datum.timeout.connect(self.timer_datum_slot)

        self.timer_zeit = QTimer(self)
        self.timer_zeit.timeout.connect(self.timer_zeit_slot)
        self.timer_zeit.start(1000)
        
        self.zeige_uhrzeit()
        
        self.show()
    
    def timer_zeit_slot(self):
        self.zeige_uhrzeit()
    
    def timer_datum_slot(self):
        self.stop_datum()
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.zeige_datum()
        
    def zeige_uhrzeit(self):
        self.zeit_anzeige = QTime.currentTime().toString("hh:mm:ss")
        
        if self.doppelpunkt == False:
            self.doppelpunkt = True
        else:
            self.doppelpunkt = False
        if self.doppelpunkt == False:
            self.zeit_anzeige = self.zeit_anzeige.replace(":", " ")   
            
        self.setDigitCount(8)
        self.display(self.zeit_anzeige)
    
    def zeige_datum (self):
        if self.timer_datum.isActive() == True:
            return
        self.datum_anzeige = QDate.currentDate().toString("dd.MM.yyyy")
        self.setDigitCount(10)
        self.display(self.datum_anzeige)
        self.timer_zeit.stop()
        self.timer_datum.start(2000)
    
    def stop_datum(self):
        self.timer_datum.stop()
        self.timer_zeit.start(1000)
        self.zeige_uhrzeit()
        
    
app = QApplication([])
fenster = Hauptfenster()
app.exec()
        