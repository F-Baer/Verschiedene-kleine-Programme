from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir

class Hauptfenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bildbetrachter")
        self.resize(500, 280)
        
        self.eingabe_feld = QLineEdit(self)
        self.eingabe_feld.setGeometry(10, 200, 200, 30)
        
        self.eingabe_label = QLabel("Bitte geben sie den Dateinamen ein:", self)
        self.eingabe_label.setGeometry(10, 180 ,230, 30)
        
        self.bild_label = QLabel(self)
        self.bild_label.setGeometry(10, 10 ,10, 10)
        
        self.oeffnen_button = QPushButton(self)
        self.oeffnen_button.setGeometry(250, 200, 70, 30)
        self.oeffnen_button.setText("Öffnen")
        self.oeffnen_button.clicked.connect(self.oeffne_bilddatei)
        
        self.auswaehlen_button = QPushButton(self)
        self.auswaehlen_button.setGeometry(250, 170, 70, 30)
        self.auswaehlen_button.setText("Auswählen")
        self.auswaehlen_button.clicked.connect(self.wahle_datei_aus)
                
        self.beenden_button = QPushButton(self)
        self.beenden_button.setGeometry(350, 200, 70, 30)
        self.beenden_button.setText("Beenden")
        self.beenden_button.clicked.connect(self.close)    
        
        self.bild = QPixmap()
        
        self.show()
        
    def oeffne_bilddatei(self):
        if self.bild.load(self.eingabe_feld.text()):
            self.bild = self.bild.scaledToWidth(150)
            self.bild_label.setPixmap(self.bild)
            self.bild_label.resize(self.bild.size())
        else:
            QMessageBox.warning(self,
                    "Fehler beim Öffnen der Datei.",
                    "Die Grafikdatei konnte nicht geöffnet werden."
                    "\nBitte geben Sie den Dateinamen mit Pfad in das Textfeld ein.")
    
    def wahle_datei_aus(self):
        self.datei = QFileDialog.getOpenFileName(self, "Datei öffnen", QDir.currentPath(), "Grafikdateien (*.jpg *.bmp *.gif *.png)")
        if self.datei[0] != "":
            self.eingabe_feld.setText(self.datei[0])
            self.oeffne_bilddatei()
        

app = QApplication([])
fenster = Hauptfenster()
app.exec()


            
    