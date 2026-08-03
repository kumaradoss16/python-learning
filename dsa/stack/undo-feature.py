class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def type(self, chars):
        self.history.append(self.text)
        self.text += chars

    def undo(self):
        if self.history:
            self.text = self.history.pop()
        else:
            print("Nothing to Undo")


editor = TextEditor()
editor.type("Hello")
editor.type(" World")
print(editor.text)
editor.undo()
print(editor.text)