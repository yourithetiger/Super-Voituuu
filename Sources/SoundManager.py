from pygame import mixer

class SoundManger:
    def __init__(self, volume, path):
        self.volume = volume
        self.soundPath = path
        self.shouldPlay = False

        mixer.init()
        mixer.music.set_volume(self.volume)
        mixer.music.load(self.soundPath)

    def play(self):
        mixer.music.play()

    def stop(self):
        mixer.music.stop()
