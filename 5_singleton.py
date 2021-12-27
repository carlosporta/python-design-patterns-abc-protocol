from typing import Any, Dict


class Singleton(type):
    _instances: Dict[type, "Singleton"] = {}

    def __call__(cls: "Singleton", *args: Any, **kwargs: Any) -> type:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AudioPlayer(metaclass=Singleton):
    _instance = None

    def __init__(self) -> None:
        self.current_song = ""

    def play(self, song_name: str) -> None:
        self.current_song = song_name


audio_player = AudioPlayer()
print("Audio player from current file")
print(f'Current song: {audio_player.current_song or "Not playing"}')
print("Play: foo")
audio_player.play("1 - foo")
print(f'Current song: {audio_player.current_song or "Not playing"}')

# another_file.py
print()
print("Simulating an audio player from another file")
foreign_audio_player = AudioPlayer()
print(f'Current song: {foreign_audio_player.current_song or "Not playing"}')
print("Play: bar")
foreign_audio_player.play("2 - bar")
print(f'Current song: {foreign_audio_player.current_song or "Not playing"}')

# 5_singleton.py
print()
print("Audio player from current file")
print(f'Current song: {audio_player.current_song or "Not playing"}')
