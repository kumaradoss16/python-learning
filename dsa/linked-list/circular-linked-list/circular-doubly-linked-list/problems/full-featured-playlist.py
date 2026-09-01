class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class FullFeaturedPlaylist:
    def __init__(self):
        self.current = None
        self.tail = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.current is None:
            new_song.next = new_song.prev = new_song
            self.current = self.tail = new_song
        else:
            new_song.prev = self.tail
            new_song.next = self.tail.next
            self.tail.next.prev = new_song
            self.tail.next = new_song
            self.tail = new_song


    def play_next(self):
        self.current = self.current.next
        print(f"Now playing: {self.current.title}")

    def play_previous(self):
        self.current = self.current.prev
        print(f"Now Playing: {self.current.title}")


playlist = FullFeaturedPlaylist()
playlist.add_song("Track 1")
playlist.add_song("Track 2")
playlist.add_song("Track 3")
playlist.play_next()
playlist.play_next()
playlist.play_next()
playlist.play_previous()