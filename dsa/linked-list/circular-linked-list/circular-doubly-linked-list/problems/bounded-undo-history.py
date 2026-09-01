from threading import current_thread


class HistoryState:
    def __init__(self, text):
        self.text = text
        self.next = None
        self.prev = None


class BoundedUndiHistory:
    def __init__(self, max_states):
        self.max_states = max_states
        self.current = None
        self.tail = None
        self.count = 0


    def record(self, text):
        new_state = HistoryState(text)
        if self.current is None:
            new_state.prev = new_state.next = new_state
            self.current = self.tail = new_state
            self.count = 1
            return

        new_state.prev = self.current
        new_state.next = self.current.next
        self.current.next.prev = new_state
        self.current.next = new_state
        self.current = new_state
        self.count += 1

        if self.count > self.max_states:
            oldest = self.tail
            self.tail = oldest.next
            oldest.prev.next = oldest.next
            oldest.next.prev = oldest.prev
            self.count -= 1
        else:
            self.tail = new_state.next if self.tail is None else self.tail


history = BoundedUndiHistory(max_states=3)
history.record("Hello")
history.record("Hello World")
history.record("Hello World!")
history.record("Hello World! Extra")
