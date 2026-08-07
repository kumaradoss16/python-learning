Excellent example. This program demonstrates a **real-world application of a singly linked list** by implementing a grocery shopping list. I'll explain it exactly as Python executes it.

---

# Step 1: Purpose of the Program

This program creates a grocery list where you can:

* Add items
* Remove items
* Display all items

Internally it uses a **Singly Linked List**.

Instead of storing items in a Python list like

```python
["Milk", "Eggs", "Bread"]
```

it stores them as nodes.

```
Head
 │
 ▼
Milk → Eggs → Bread → Cucumber → None
                               ▲
                               │
                              Tail
```

---

# Step 2: ItemNode Class

```python
class ItemNode:
```

This class represents **one grocery item**.

Think of one node as one box.

```
+----------------------+
| item_name | next     |
+----------------------+
```

---

## Constructor

```python
def __init__(self, item_name):
```

Called whenever you write

```python
ItemNode("Milk")
```

Suppose

```python
node = ItemNode("Milk")
```

Python passes

```
self = newly created ItemNode object

item_name = "Milk"
```

---

### Line

```python
self.item_name = item_name
```

Memory becomes

```
+-------------------------+
| item_name = "Milk"      |
| next = ?                |
+-------------------------+
```

---

### Line

```python
self.next = None
```

Now

```
+-------------------------+
| item_name = "Milk"      |
| next = None             |
+-------------------------+
```

This means this node isn't connected to another node yet.

---

# GroceryList Class

```python
class GroceryList:
```

This class manages the entire linked list.

---

## Constructor

```python
def __init__(self):
```

When Python executes

```python
shopping_list = GroceryList()
```

Memory

```
shopping_list

Head → None

Tail → None
```

Initially there are no grocery items.

---

# add_item()

---

## Function Header

```python
def add_item(self, item_name):
```

Suppose

```python
shopping_list.add_item("Milk")
```

Python passes

```
self = shopping_list

item_name = "Milk"
```

---

## Line

```python
new_item = ItemNode(item_name)
```

Equivalent to

```python
new_item = ItemNode("Milk")
```

Memory

```
new_item

+------------------+
| Milk             |
| next = None      |
+------------------+
```

---

## Check Empty List

```python
if self.head is None:
```

Current list

```
Head → None
```

Condition

```
True
```

---

### First Item

```python
self.head = new_item
```

Now

```
Head
 │
 ▼
Milk → None
```

---

### Tail

```python
self.tail = new_item
```

Now

```
Head
 │
 ▼
Milk → None
 ▲
 │
Tail
```

---

## Add Second Item

```python
shopping_list.add_item("Eggs")
```

Creates

```
Eggs → None
```

Current list

```
Head
 │
 ▼
Milk → None
 ▲
 │
Tail
```

---

Condition

```python
if self.head is None
```

False.

---

Execute

```python
self.tail.next = new_item
```

Before

```
Milk → None
```

After

```
Milk → Eggs
```

---

Update tail

```python
self.tail = new_item
```

Now

```
Head
 │
 ▼
Milk → Eggs → None
         ▲
         │
       Tail
```

---

Exactly the same happens for

```python
shopping_list.add_item("Bread")
```

```
Milk → Eggs → Bread
```

---

Then

```python
shopping_list.add_item("Cucumber")
```

```
Milk → Eggs → Bread → Cucumber
```

Final list

```
Head
 │
 ▼
Milk → Eggs → Bread → Cucumber → None
                           ▲
                           │
                          Tail
```

---

# show_list()

---

## Line

```python
current = self.head
```

```
current
   │
   ▼
Milk
```

---

## Empty List Check

```python
if current is None:
```

Current

```
Milk
```

Condition

False.

---

## Line

```python
items = []
```

Creates

```
items = []
```

---

# Loop

```python
while current_item is not None:
```

---

## Iteration 1

Current

```
Milk
```

Execute

```python
items.append(current_item.item_name)
```

```
items

["Milk"]
```

Move

```python
current_item = current_item.next
```

Now

```
Eggs
```

---

## Iteration 2

```
items

["Milk","Eggs"]
```

Move

```
Bread
```

---

## Iteration 3

```
["Milk","Eggs","Bread"]
```

Move

```
Cucumber
```

---

## Iteration 4

```
["Milk","Eggs","Bread","Cucumber"]
```

Move

```
None
```

Loop stops.

---

Print

```python
print(" -> ".join(items))
```

Output

```
Milk -> Eggs -> Bread -> Cucumber
```

---

# remove_item("Eggs")

Current list

```
Milk → Eggs → Bread → Cucumber
```

---

## Empty?

```python
if self.head is None
```

False.

---

## Head?

```python
if self.head.item_name == item_name
```

```
Milk == Eggs
```

False.

---

## Line

```python
current = self.head
```

```
current

Milk
```

---

# Loop

```python
while current.next is not None:
```

Notice

We check

```python
current.next.item_name
```

NOT

```python
current.item_name
```

Why?

Because we need the **previous node**.

---

## Iteration 1

Current

```
Milk
```

Check

```python
current.next.item_name
```

means

```
Eggs
```

Condition

```
Eggs == Eggs
```

True.

---

Execute

```python
current.next = current.next.next
```

Before

```
Milk
  │
  ▼
Eggs
  │
  ▼
Bread
```

After

```
Milk
  │
  ▼
Bread
```

Eggs is skipped.

Entire list

```
Milk → Bread → Cucumber
```

---

Tail check

```python
if current.next is None
```

Current.next

```
Bread
```

Not None.

Tail remains

```
Cucumber
```

Return

```
True
```

---

# show_list() Again

Loop visits

```
Milk
```

↓

```
Bread
```

↓

```
Cucumber
```

Output

```
Milk -> Bread -> Cucumber
```

---

# Complete Execution Diagram

### Initially

```
Head → None
Tail → None
```

---

### After Milk

```
Head
 │
 ▼
Milk → None
 ▲
 │
Tail
```

---

### After Eggs

```
Head
 │
 ▼
Milk → Eggs → None
         ▲
         │
       Tail
```

---

### After Bread

```
Head
 │
 ▼
Milk → Eggs → Bread → None
                 ▲
                 │
               Tail
```

---

### After Cucumber

```
Head
 │
 ▼
Milk → Eggs → Bread → Cucumber → None
                           ▲
                           │
                          Tail
```

---

### Remove Eggs

```
Before

Milk → Eggs → Bread → Cucumber

After

Milk ─────────► Bread → Cucumber
```

---

### Final List

```
Head
 │
 ▼
Milk → Bread → Cucumber → None
                    ▲
                    │
                   Tail
```

# Final Output

```text
Grocery List: Milk -> Eggs -> Bread -> Cucumber
Grocery List: Milk -> Bread -> Cucumber
```

### Time Complexity

| Operation                  | Complexity |
| -------------------------- | ---------- |
| `add_item()` (with `tail`) | **O(1)**   |
| `remove_item()`            | **O(n)**   |
| `show_list()`              | **O(n)**   |

This implementation is efficient because it maintains both a **`head`** pointer (for accessing the first node) and a **`tail`** pointer (for appending new items in constant time). Without the `tail` pointer, `add_item()` would need to traverse the entire list and would take **O(n)** time instead of **O(1)**.
