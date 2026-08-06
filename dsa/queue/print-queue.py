from collections import deque

class PrintQueue:
    def __init__(self):
        self.jobs = deque()

    def submit_job(self, document_name):
        self.jobs.append(document_name)
        print(f"{document_name} added to queue")

    def print_next(self):
        if not self.jobs:
            print("No jobs queued")
            return
        job = self.jobs.popleft()
        print(f"Printing: {job}")

printer = PrintQueue()
printer.submit_job("Report.pdf")
printer.submit_job("Invoice.docx")
printer.submit_job("Sales.xlsx")
printer.print_next()
printer.print_next()




