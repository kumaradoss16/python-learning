class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class GameTurnManager:
    def __init__(self):
        self.current_player = None
        self.tail = None

    def add_player(self, name):
        new_player = Node(name)
        if self.current_player is None:
            new_player.next = new_player
            self.current_player = self.tail = new_player
        else:
            new_player.next = self.tail.next
            self.tail.next = new_player
            self.tail = new_player


    def next_turn(self):
        player = self.current_player.value
        self.current_player = self.current_player.next
        return player



game = GameTurnManager()
game.add_player("Alice")
game.add_player("Bob")
game.add_player("Carol")

for _ in range(4):
    print(f"{game.next_turn()}'s turn")

