class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class ForwardOnlyPlaylist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
            self.current = new_song
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_song


    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
        print(f"Now Playing: {self.current.title}")


playlist = ForwardOnlyPlaylist()
playlist.add_song("Tracks 1")
playlist.add_song("Tracks 2")
playlist.add_song("Tracks 3")

playlist.play_next()
playlist.play_next()