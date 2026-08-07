This is a great example because it combines **strings**, **linked lists**, and **reversing a linked list**.

Let's go through it **one step at a time** as Python executes it.

---

# What is the purpose of this program?

Suppose you have a sentence:

```text
I am learning linked lists
```

The program:

1. Splits the sentence into words.
2. Stores each word in a singly linked list.
3. Reverses the linked list.
4. Prints the reversed sentence.

---

# Step 1: WordNode Class

```python
class WordNode:
```

This class represents **one word**.

Each node contains:

* the word
* a pointer to the next word

Memory layout:

```text
+----------------------+
| word | next          |
+----------------------+
```

---

## Constructor

```python
def __init__(self, word):
```

Whenever Python executes

```python
WordNode("I")
```

Python creates an object.

Then executes

```python
self.word = word
```

Memory becomes

```text
+----------------------+
| word = "I"           |
| next = ?             |
+----------------------+
```

Next

```python
self.next = None
```

Memory becomes

```text
+----------------------+
| word = "I"           |
| next = None          |
+----------------------+
```

---

# Step 2: Build the Linked List

```python
def build_word_list(sentence):
```

Suppose Python calls

```python
build_word_list("I am learning linked lists")
```

The parameter becomes

```text
sentence

"I am learning linked lists"
```

---

## Split the Sentence

```python
words = sentence.split()
```

`split()` divides the sentence wherever there is a space.

Output

```python
words = ["I", "am", "learning", "linked", "lists"]
```

Memory

```text
Index      Value

0          I
1          am
2          learning
3          linked
4          lists
```

---

## Create the First Node

```python
head = WordNode(words[0])
```

`words[0]`

```text
"I"
```

Python executes

```python
head = WordNode("I")
```

Memory

```text
Head
 │
 ▼
+------------------+
| I | None         |
+------------------+
```

---

## Current Pointer

```python
current = head
```

Now both variables point to the same node.

```text
Head
 │
 ▼
+---------+
|    I    |
+---------+
 ▲
 │
Current
```

---

# Step 3: Loop

```python
for word in words[1:]:
```

What is

```python
words[1:]
```

It means

```python
["am", "learning", "linked", "lists"]
```

Python ignores the first word because it already created the head node.

---

# First Iteration

Current word

```text
am
```

Execute

```python
current.next = WordNode(word)
```

Equivalent to

```python
current.next = WordNode("am")
```

Before

```text
Head

I → None
```

After

```text
Head

I → am → None
```

---

Move current

```python
current = current.next
```

Now

```text
Head

I → am
     ▲
     │
  Current
```

---

# Second Iteration

Current word

```text
learning
```

Execute

```python
current.next = WordNode("learning")
```

List

```text
I → am → learning
```

Move current

```text
I → am → learning
          ▲
          │
       Current
```

---

# Third Iteration

Word

```text
linked
```

List becomes

```text
I → am → learning → linked
```

---

# Fourth Iteration

Word

```text
lists
```

Final linked list

```text
Head
 │
 ▼
I → am → learning → linked → lists → None
```

The loop finishes.

---

Return

```python
return head
```

The head node is returned.

---

# Step 4: Print the Linked List

```python
print_word_list(sentence_list)
```

Parameter

```text
head

↓

I
```

---

Create

```python
words = []
```

Memory

```python
[]
```

---

Current

```python
current = head
```

```text
current

↓

I
```

---

## Loop

```python
while current:
```

---

### Iteration 1

Current

```text
I
```

Execute

```python
words.append(current.word)
```

Output

```python
["I"]
```

Move

```python
current = current.next
```

Now

```text
am
```

---

### Iteration 2

```python
["I","am"]
```

Move

```text
learning
```

---

### Iteration 3

```python
["I","am","learning"]
```

---

### Iteration 4

```python
["I","am","learning","linked"]
```

---

### Iteration 5

```python
["I","am","learning","linked","lists"]
```

Move

```text
None
```

Loop stops.

---

Print

```python
print(" ".join(words))
```

`join()` combines all words using spaces.

Output

```text
I am learning linked lists
```

---

# Step 5: Reverse the Linked List

Python executes

```python
reversed_list = reverse_word_list(sentence_list)
```

Current list

```text
Head

I → am → learning → linked → lists → None
```

---

## Initialize

```python
previous = None
```

```text
previous

None
```

---

```python
current = head
```

```text
current

↓

I
```

---

# While Loop

```python
while current is not None:
```

---

## Iteration 1

Current

```text
I
```

---

Save next node

```python
next_node = current.next
```

```text
next_node

↓

am
```

---

Reverse pointer

```python
current.next = previous
```

Before

```text
I → am
```

After

```text
I → None
```

---

Move previous

```python
previous = current
```

```text
previous

↓

I
```

---

Move current

```python
current = next_node
```

```text
current

↓

am
```

---

Current situation

```text
previous

I → None

current

am → learning → linked → lists
```

---

# Iteration 2

Current

```text
am
```

Save

```text
learning
```

Reverse

```text
am → I
```

Move pointers

```text
previous

↓

am → I
```

Current

```text
learning
```

---

# Iteration 3

After reversing

```text
learning → am → I
```

---

# Iteration 4

```text
linked → learning → am → I
```

---

# Iteration 5

```text
lists → linked → learning → am → I
```

Current becomes

```text
None
```

Loop stops.

Return

```python
return previous
```

`previous` now points to the new head.

---

# Final Linked List

```text
Head

lists
   │
   ▼
linked
   │
   ▼
learning
   │
   ▼
am
   │
   ▼
I
   │
   ▼
None
```

---

# Print Again

The same printing function runs.

It visits

```text
lists
↓

linked
↓

learning
↓

am
↓

I
```

The list becomes

```python
["lists","linked","learning","am","I"]
```

`join()` produces

```text
lists linked learning am I
```

---

# Complete Execution Flow

### Original Sentence

```text
I am learning linked lists
```

↓

### Split

```python
["I", "am", "learning", "linked", "lists"]
```

↓

### Build Linked List

```text
Head

I → am → learning → linked → lists
```

↓

### Print

```text
I am learning linked lists
```

↓

### Reverse

```text
lists → linked → learning → am → I
```

↓

### Print

```text
lists linked learning am I
```

---

# Final Output

```text
I am learning linked lists
lists linked learning am I
```

---

# Time Complexity

| Function              | Time Complexity |
| --------------------- | --------------- |
| `build_word_list()`   | **O(n)**        |
| `reverse_word_list()` | **O(n)**        |
| `print_word_list()`   | **O(n)**        |

Here, **n** is the number of words in the sentence. Each function traverses the linked list once, so they all run in linear time.
