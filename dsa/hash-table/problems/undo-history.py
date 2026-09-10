from idlelib import history


class UndoHistory:
    def __init__(self):
        self.stack = []
        self.seen_states = set()

    def push_state(self, state):
        if state in self.seen_states:
            return False
        self.stack.append(state)
        self.seen_states.add(state)
        return True

    def undo(self):
        if not self.stack:
            return None
        state = self.stack.pop()
        self.seen_states.discard(state)
        return state

history = UndoHistory()

history.push_state("Home")
history.push_state("About")
history.push_state("Contact")

print("Stack:", history.stack)
print("Stack:", history.seen_states)

print("Undo:", history.undo())
print("Stack after undo:", history.stack)

print("Undo:", history.undo())
print("Stack after undo:", history.stack)

print("Undo:", history.undo())
print("Stack after undo:", history.stack)

print("Undo:", history.undo())


