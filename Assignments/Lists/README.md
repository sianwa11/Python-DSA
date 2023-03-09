# 1. To implement the length method, we counted the number of nodes in the list. An alternative strategy would be to store the number of nodes in the list as an additional piece of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the length method.

# 2. Implement the remove method so that it works correctly in the case where the item is not in the list.

# 3. Modify the list classes to allow duplicates. Which methods will be impacted by this change?

# 4. Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).

# 5. Implement a slice method for the UnorderedList class. It should take two parameters, start and stop, and return a copy of the list starting at the start position and going up to but not including the stop position.

**Answers(unordered_list.py)**

---

# 1. Modify the list classes to allow duplicates. Which methods will be impacted by this change?

# 2. Implement the remaining operations defined in the OrderedList ADT.

**Answers(unordered_list.py)**

---

# 1. Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.

**Answers(perfomance_comparison.py)**
**Result(perfomance_comparison.png)**

---

# 1. The linked list implementation given above is called a singly linked list because each node has a single reference to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python.

**Answers(doubly_linkedlist.py)**
