class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class RepeatAllPlaylist:
    def __init__(self):
        self.current = None
        self.tail = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.current is None:
            new_song.next = new_song
            self.current = new_song
            self.tail = new_song
        else:
            new_song.next = self.current
            self.tail.next = new_song
            self.tail = new_song

    def play_next(self):
        self.current = self.current.next
        print(f"Now Playing: {self.current.title}")


playlist = RepeatAllPlaylist()
playlist.add_song("Track 1")
playlist.add_song("Track 2")
playlist.add_song("Track 3")
playlist.add_song("Track 4")

for _ in range(7):
    playlist.play_next()