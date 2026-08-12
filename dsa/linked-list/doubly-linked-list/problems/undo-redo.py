class EditState:
    def __init__(self, text):
        self.text = text
        self.next = None
        self.prev = None


class UndoableEditor:
    def __init__(self):
        self.current = EditState("")

    def type_text(self, new_text):
        new_state = EditState(self.current.text + new_text)
        new_state.prev = self.current
        self.current.next = new_state
        self.current = new_state

    def undo(self):
        if self.current.prev:
            self.current = self.current.prev
        return self.current.text

    def redo(self):
        if self.current.next:
            self.current = self.current.next
        return self.current.text

editor = UndoableEditor()
editor.type_text("Hello")
editor.type_text(" world!")
print(editor.current.text)
print(editor.undo())
print(editor.redo())
