from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from panda3d.core import AudioSound, Point3

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        # Метод который отвечает за загрузку карты с файла
        x, y = self.land.loadLand("labyrinth.txt")
        # музыка
        
        self.background_music = loader.loadMusic("Jeremy Soule Secunda.mp3")
        self.background_music.setLoop(True)
        self.background_music.setTime(0)  # Начальное время воспроизведения
        self.background_music.play()
        self.music_time = 0.0
        self.accept('i', self.start_music)
        self.accept('o', self.stop_music)
        self.accept('p', self.resume_music)
        
        # создаем игрока с позицией на карте
        self.hero = Hero((2, 1, 2), self.land)
        # 41, 25, 2 - конец лабиринта
        # устанавливаем угол обзора 90 градусов
        self.camLens.setFov(90)
        # закрывание игры
        self.accept("escape", self.exit_app)
        
    # музыка
        
    def start_music(self):
        # Начинаем воспроизведение музыки с самого начала
        self.background_music.setTime(self.music_time)
        self.background_music.play()

    def stop_music(self):
        # Останавливаем воспроизведение музыки
        self.background_music.stop()
        self.music_time = self.background_music.getTime()
        
    def resume_music(self):
        # Продолжаем воспроизведение музыки с сохраненного времени
        self.background_music.setTime(self.music_time)
        self.background_music.play()
   
    # выход из игры
    
    def exit_app(self):
        # Выход из приложения
        self.userExit()
      
    
   
game = Game()
game.run()