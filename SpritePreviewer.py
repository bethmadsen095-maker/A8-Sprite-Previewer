#A8-Sprite-Previewer
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        application_frame = QFrame()
        application_layout = QVBoxLayout()
        image_frame = QFrame()
        image_layout = QHBoxLayout(image_frame)

        #load image
        #label displaying current sprite image
        # self.sprite_name = QLabel(sprite_00.png)

        self.label = QLabel()
        pixmap = QPixmap('sprite_00.png')
        self.label.setPixmap(pixmap)
        # self.label.setPixmap(QPixmap.fromImage("sprite_00.png"))

        lcd = QLCDNumber()
        lcd.setMinimumHeight(60)
        #load slider
        self.slider = QSlider()
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(lcd.display)
        # self.slider.setTickPosition()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.
        #text label
        # self.label =
        self.button_test = QPushButton("Start")
        self.button_test.setCheckable(True)
        self.button_test.setChecked(True)
        self.button_test.clicked.connect(self.start_or_stop)


        image_layout.addWidget(self.label)
        image_layout.addWidget(self.slider)
        application_layout.addWidget(lcd)

        image_frame.setLayout(image_layout)
        application_layout.addWidget(image_frame)
        application_layout.addWidget(self.button_test)
        application_frame.setLayout(application_layout)


        self.setCentralWidget(application_frame)


    # You will need methods in the class to act as slots to connect to signals
    def start_or_stop(self):
        if self.button_test.isChecked():
            self.button_test.setText("Stop")
        else:
            self.button_test.setText("Start")
        #put code here for what happens when the start/stop button is pushed

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
