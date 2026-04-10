#A8-Sprite-Previewer
import math,sys

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
        self.num_frames = 20
        self.frames = load_sprite('images',self.num_frames)

        self.current_frame = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_frame)
        # Make the GUI in the setupUI method
        self.setupUI()

    def setupUI(self):
        application_frame = QFrame()
        application_layout = QVBoxLayout()
        image_frame = QFrame()
        image_layout = QHBoxLayout(image_frame)

        #starting image
        self.label = QLabel()
        pixmap = self.frames[1]
        self.label.setPixmap(pixmap)

        #slider
        self.slider = QSlider()
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(20)
        self.slider.valueChanged.connect(self.update_fps_label)

        #frames per second label
        self.fps_label = QLabel("Frames per second: 1")

        #menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        pause_action = QAction('&Pause',self)
        pause_action.triggered.connect(self.pause_program)
        exit_action = QAction('&Exit',self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(pause_action)
        file_menu.addAction(exit_action)

        #button
        self.start_button = QPushButton("Start")
        self.start_button.setCheckable(True)
        self.start_button.setChecked(False)
        self.start_button.clicked.connect(self.start_or_stop)

        #add widgets to image layout
        image_layout.addWidget(self.label)
        image_layout.addWidget(self.slider)
        image_frame.setLayout(image_layout)

        #add widgets to application layout
        application_layout.addWidget(image_frame)
        application_layout.addWidget(self.fps_label)
        application_layout.addWidget(self.start_button)
        application_frame.setLayout(application_layout)

        self.setCentralWidget(application_frame)

    def update_fps_label(self):
        value = self.slider.value()
        self.fps_label.setText(f"Frames per second: {value}")

    def start_or_stop(self):
        if self.start_button.isChecked():
            self.timer.start(int(1000/(self.slider.value())))
            self.start_button.setText("Stop")
        else:
            self.start_button.setText("Start")
            self.timer.stop()

    def change_frame(self):
        self.current_frame +=1
        if self.current_frame >= self.num_frames:
            self.current_frame = 0
        self.label.setPixmap(self.frames[self.current_frame])

    def quit_program(self):
        sys.exit()

    def pause_program(self):
        self.timer.stop()
        self.start_button.setText("Start")
        self.start_button.setChecked(False)

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
