from collections import deque

class SupportQueue:
    def __init__(self):
        self.tickets = deque()

    def new_ticket(self, customer_name, issue):
        self.tickets.append({"customer": customer_name, "issue": issue})

    def handle_next_ticket(self):
        if not self.tickets:
            print("No tickets left.")
            return
        ticket = self.tickets.popleft()
        print(f"Helping {ticket['customer']} with {ticket['issue']}")


support = SupportQueue()
support.new_ticket("Alice", "Can't reset password")
support.new_ticket("Bob", "App keeps crashing")
support.new_ticket("Kennedy", "PC runs slowly")
support.handle_next_ticket()
support.handle_next_ticket()