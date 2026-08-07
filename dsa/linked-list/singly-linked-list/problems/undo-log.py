class ActionNode:
    def __init__(self, action):
        self.action = action
        self.next = None


class ActionLog:
    def __init__(self):
        self.head = None
        self.tail = None

    def log_action(self, action):
        new_node = ActionNode(action)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def replay_all(self):
        current = self.head
        while current is not None:
            print(f"Replaying: {current.action}")
            current = current.next

log = ActionLog()
log.log_action("Creating file")
log.log_action("Renamed file")
log.log_action("Moved file to folder")
log.replay_all()