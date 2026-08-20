class TaskNode:
    def __init__(self, task_name, remaining_time):
        self.task_name = task_name
        self.remaining_time = remaining_time
        self.next = None

class RoundRobinCPUScheduler:
    def __init__(self, time_slice=2):
        self.current = None
        self.time_slice = time_slice


    def add_task(self, task_name, burst_time):
        new_task = TaskNode(task_name, burst_time)
        if self.current is None:
            new_task.next = new_task
            self.current = new_task
        else:
            temp = self.current
            while temp.next is not self.current:
                temp = temp.next
            temp.next = new_task
            new_task.next = self.current

    def run(self):
        while self.current is not None:
            task = self.current
            run_time = min(self.time_slice, task.remaining_time)
            task.remaining_time -= run_time
            print(f"Running {task.task_name} for {run_time}s (remaining: {task.remaining_time})s")

            if task.remaining_time <= 0:
                print(f"{task.task_name} finished")
                if task.next is task:
                    self.current = None  # Last taskd done
                else:
                    # Remove the finished task from the circle
                    temp = task.next
                    while temp.next is not task:
                        temp = temp.next
                    temp.next = task.next
                    self.current = task.next
            else:
                self.current = task.next  # Move to next task

scheduler = RoundRobinCPUScheduler(time_slice=2)
scheduler.add_task("Task A", 7)
scheduler.add_task("Task B", 4)
scheduler.add_task("Task C", 5)
scheduler.run()




