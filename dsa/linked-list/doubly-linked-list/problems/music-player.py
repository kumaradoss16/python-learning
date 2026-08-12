"""Music Player with Next / Previous Track
Any music or video app where you can skip forward AND backward through a playlist."""

class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class MusicPlayer:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

    def play_next(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        if self.current.next is not None:
            self.current = self.current.next
            print(f"Now Playing: {self.current.title}")
        else:
            print("Already at the last song.")
            print(f"Now Playing: {self.current.title}")

    def play_previous(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        if self.current.prev is not None:
            self.current = self.current.prev
            print(f"Now Playing: {self.current.title}")
        else:
            print("Already at the last song.")
            print(f"Now Playing: {self.current.title}")

    def display_songs(self):
        current = self.head
        print("Playlist:")
        if current is None:
            print("Playlist is empty.")
            return
        while current:
            print(current.title, end=" <-> ")
            current = current.next
        print("None")


    def remove_song(self, title):
        current = self.head
        while current:
            if current.title == title:
                # Only one song
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                    self.current = None

                # Delete the head
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                    # If the deleted song was currently playing
                    if self.current == current:
                        self.current = self.head

                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                    # If the deleted song was currently playing
                    if self.current == current:
                        self.current = self.tail

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    # If the deleted song was currently playing
                    if self.current == current:
                        self.current = current.next

                # Disconnect deleted node
                current.next = None
                current.prev = None
                return True
            current = current.next

        return False



player = MusicPlayer()
player.add_song("Song A")
player.add_song("Song B")
player.add_song("Song C")
player.display_songs()
player.play_next()
player.play_next()
player.play_previous()
player.remove_song("Song B")
player.display_songs()