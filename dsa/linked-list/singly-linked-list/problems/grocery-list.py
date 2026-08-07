class ItemNode:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next = None


class GroceryList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_item(self, item_name):
        new_item = ItemNode(item_name)

        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item

    def remove_item(self, item_name):
        if self.head is None:
            return False

        if self.head.item_name == item_name:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        current = self.head
        while current.next is not None:
            if current.next.item_name == item_name:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return True
            current = current.next

        return False

    def show_list(self):
        current = self.head
        if current is None:
            print("Grocery list is empty!")
            return
        current_item = current
        items = []
        while current_item is not None:
            items.append(current_item.item_name)
            current_item = current_item.next
        print("Grocery List:", " -> ".join(items))


shopping_list = GroceryList()
shopping_list.add_item("Milk")
shopping_list.add_item("Eggs")
shopping_list.add_item("Bread")
shopping_list.add_item("Cucumber")
shopping_list.show_list()

shopping_list.remove_item("Eggs")
shopping_list.show_list()