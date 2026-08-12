class PhotoNode:
    def __init__(self, filename):
        self.filename = filename
        self.next = None
        self.prev = None


class PhotoGallery:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None


    def add_photo(self, filename):
        new_photo = PhotoNode(filename)
        if self.head is None:
            self.head = new_photo
            self.tail = new_photo
            self.current = new_photo
        else:
            new_photo.prev = self.tail
            self.tail.next = new_photo
            self.tail = new_photo

    def swipe_right(self):
        if self.current.next:
            self.current = self.current.next
        print(f"Viewing: {self.current.filename}")

    def swipe_left(self):
        if self.current.prev:
            self.current = self.current.prev
        print(f"Viewing: {self.current.filename}")

gallery = PhotoGallery()
gallery.add_photo("beach.jpg")
gallery.add_photo("mountain.jpg")
gallery.add_photo("sunset.png")
gallery.swipe_right()
gallery.swipe_right()
gallery.swipe_left()