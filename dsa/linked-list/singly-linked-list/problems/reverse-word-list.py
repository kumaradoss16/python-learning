class WordNode:
    def __init__(self, word):
        self.word = word
        self.next = None


def build_world_list(sentence):
    words = sentence.split()
    head = WordNode(words[0])
    current = head
    for word in words[1:]:
        current.next = WordNode(word)
        current = current.next
    return head

def reverse_word_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def print_word_list(head):
    words = []
    current = head
    while current:
        words.append(current.word)
        current = current.next
    print(" ".join(words))


sentence_list = build_world_list("I am learning linked lists")
print_word_list(sentence_list)
reversed_list = reverse_word_list(sentence_list)
print_word_list(reversed_list)