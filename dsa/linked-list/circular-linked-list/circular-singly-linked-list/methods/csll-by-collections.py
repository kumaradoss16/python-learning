from collections import deque

turn_order = deque(["Player1", "Player2", "PLayer3"])

def take_turn():
    current_player = turn_order[0]
    print(f"{current_player}'s turn")
    turn_order.rotate(-1)


take_turn()
take_turn()
take_turn()
take_turn()
take_turn()

