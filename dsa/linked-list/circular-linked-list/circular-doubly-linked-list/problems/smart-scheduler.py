class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None
        self.prev = None


class SmartScheduler:
    def __init__(self):
        self.current = None
        self.tail = None


    def add_task(self, name, priority):
        new_task = Task(name, priority)
        if self.current is None:
            new_task.next = new_task.prev = new_task
            self.current = self.tail = new_task
        else:
            new_task.prev = self.tail
            new_task.next = self.tail.next
            self.tail.next.prev = new_task
            self.tail.next = new_task
            self.tail = new_task


    def run_next(self):
        print(f"Running {self.current.name} (priority {self.current.priority})")
        if self.current.priority < self.current.prev.priority:
            print(f"  -> Low priority detected, double-checking previous task: {self.current.prev.name}")
        self.current = self.current.next


scheduler = SmartScheduler()
scheduler.add_task("Backup", 5)
scheduler.add_task("Cleanup", 1)
scheduler.add_task("Report", 3)

for _ in range(3):
    scheduler.run_next()


