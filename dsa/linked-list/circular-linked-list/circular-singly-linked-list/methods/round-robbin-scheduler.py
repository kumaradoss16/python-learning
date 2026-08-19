class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RoundRobbinScheduler:
    def __init__(self):
        self.current = None

    def add_process(self, name):
        new_node = Node(name)
        if self.current is None:
            new_node.next = new_node
            self.current = new_node
        else:
            temp = self.current
            while temp.next is not self.current:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.current

    def next_turn(self):
        process_name = self.current.value
        self.current = self.current.next
        return process_name


scheduler = RoundRobbinScheduler()
scheduler.add_process("Process A")
scheduler.add_process("Process B")
scheduler.add_process("Process C")

for _ in range(5):
    print(scheduler.next_turn())

