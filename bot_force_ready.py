import time
import pyautogui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# dimensions du macbook M1 en réference : 2 560 x 1 600 pixels
def main():
    pyautogui.click(1542, 257)

    pyautogui.click(1542, 339)

    pyautogui.click(1542, 410)

    pyautogui.click(1542, 482)

    pyautogui.click(1542, 558)

    pyautogui.click(1542, 640)

    pyautogui.click(1542, 698)

    pyautogui.click(1542, 778)

    pyautogui.click(1542,855 )

    pyautogui.click(1542, 940)

    pyautogui.click(1420, 261)

    pyautogui.click(1420, 341)

    pyautogui.click(1420, 413)

    pyautogui.click(1420, 486)

    pyautogui.click(1420, 559)

    pyautogui.click(1420, 635)

    pyautogui.click(1420, 710)

    pyautogui.click(1420, 783)

    pyautogui.click(1420, 854)

    pyautogui.click(1420, 935)

    pyautogui.click(184,105)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Bouton cliquable")

        button = QPushButton("Cliquez-moi !", self)
        button.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        # Fonction à exécuter lorsque le bouton est cliqué
        print("Bouton cliqué !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
