class MusicPlayer:
    def __init__(self, implementation):
        self.implementation = implementation

    def play_song(self, song):
        self.implementation.play_song(song)

    def set_volume(self, volume):
        self.implementation.set_volume(volume)


class SpeakerSystem:
    def play_song(self, song):
        print(f"Playing {song} on speakers")

    def set_volume(self, volume):
        print(f"Setting speakers volume to {volume}")


class Headphones:
    def play_song(self, song):
        print(f"Playing {song} on headphones")

    def set_volume(self, volume):
        print(f"Setting headphones volume to {volume}")


speaker_system = SpeakerSystem()
music_player1 = MusicPlayer(speaker_system)
music_player1.play_song("Bohemian Rhapsody")
music_player1.set_volume(10)

headphones = Headphones()
music_player2 = MusicPlayer(headphones)
music_player2.play_song("Stairway to Heaven")
music_player2.set_volume(5)