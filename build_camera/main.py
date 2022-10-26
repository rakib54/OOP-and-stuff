"""
    My camera Application
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2
from PyQt5.QtCore import QTimer


class Window(QWidget):
    # Main App Window
    def __init__(self):
        super().__init__()

        # window variable
        self.window_width = 640
        self.window_height = 400

        # image variable
        self.img_width = 640
        self.img_height = 400

        # setup the main window

        self.setWindowTitle("My Camera")
        self.setGeometry(110,110, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        # setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """" contains all ui things  """
        # Image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.img_width, self.img_height)
        
        if not self.timer.isActive():
          self.cap = cv2.VideoCapture(0)
          self.timer.start(20)

        self.show()

    def update(self):
        # update frames
        _,self.frame = self.cap.read()

        frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)

        height,width,channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data,width,height,step,QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap,fromImage(q_frame))

    def save_img(self):
        # save image from camera
        pass

    def record(self):
        # record video
        pass


# run
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
