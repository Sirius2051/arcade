import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout
import sqlite3

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.audio_file = None
        self.initUI()
        self.window = pygame.display.set_mode((500, 500))
        self.con = sqlite3.connect('music.db')
        self.cursor = self.con.cursor()
    
    def initUI(self):
        layout = QVBoxLayout()

        self.select_button = QPushButton("Selecciona la cancion")
        self.select_button.clicked.connect(self.select_music)
        layout.addWidget(self.select_button)

        self.select_button_image = QPushButton("Selecciona la imagen")
        self.select_button_image.clicked.connect(self.show_image)
        layout.addWidget(self.select_button_image)

        self.play_button = QPushButton("Reproducir")
        self.play_button.clicked.connect(self.play_music)
        layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Pausar")
        self.pause_button.clicked.connect(self.pause_music)
        layout.addWidget(self.pause_button)

        self.stop_button = QPushButton("Detener")
        self.stop_button.clicked.connect(self.stop_music)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
        self.setWindowTitle("Mi Spotify")
        self.setGeometry(200, 200, 300, 200)


    def select_music(self):
        file_dialg = QFileDialog()
        file_path, _ = file_dialg.getOpenFileName(self, "Seleciona un archivo de audio")
        if file_path:
            self.cursor.execute("INSERT INTO canciones (Nombre, Ruta) VALUES (?, ?)", (file_path, file_path))
            self.con.commit()
            self.audio_file = file_path
    def show_image(self):
        file_dialg = QFileDialog()
        file_path, _ = file_dialg.getOpenFileName(self, "Seleciona una imagen")
        if file_path:
            self.cursor.execute("INSERT INTO canciones (Nombre, Ruta) VALUES (?, ?)", (file_path, file_path))
            self.con.commit()
            img = pygame.image.load(file_path)
            self.window.blit(img, (0, 0))
            pygame.display.update()
    
    def play_music(self):
        if self.audio_file:
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        

def main():
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    app.exec_()

if __name__ == "__main__":
    main()
