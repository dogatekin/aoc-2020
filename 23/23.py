import fileinput

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f'{self.val}'

cups = [int(cup) for cup in next(fileinput.input()).strip()]
head = Node(cups[0])
mapping = {cups[0]: head}

cur = head
for cup in cups[1:]:
    node = Node(cup)
    mapping[cup] = node
    cur.next = node
    cur = node
cur.next = head

cur_cup = mapping[cups[0]]
for _ in range(100):
    pickup = cur_cup.next
    cur_cup.next = pickup.next.next.next
    
    dest_label = cur_cup.val - 1
    if dest_label == 0:
        dest_label = 9
    while dest_label in {pickup.val, pickup.next.val, pickup.next.next.val}:
        dest_label -= 1
        if dest_label == 0:
            dest_label = 9
    dest = mapping[dest_label]
    
    tmp = dest.next
    dest.next = pickup
    pickup.next.next.next = tmp
    
    cur_cup = cur_cup.next

cur = mapping[1]
for _ in range(8):
    cur = cur.next
    print(cur.val, end='')
print()

head = Node(cups[0])
mapping = {cups[0]: head}

cur = head
for cup in cups[1:]:
    node = Node(cup)
    mapping[cup] = node
    cur.next = node
    cur = node  
for i in range(10, 1000001):    
    node = Node(i)
    mapping[i] = node
    cur.next = node
    cur = node
cur.next = head

cur_cup = mapping[cups[0]]
for _ in range(10000000):
    pickup = cur_cup.next
    cur_cup.next = pickup.next.next.next
    
    dest_label = cur_cup.val - 1
    if dest_label == 0:
        dest_label = 1000000
    while dest_label in {pickup.val, pickup.next.val, pickup.next.next.val}:
        dest_label -= 1
        if dest_label == 0:
            dest_label = 1000000
    dest = mapping[dest_label]
    
    tmp = dest.next
    dest.next = pickup
    pickup.next.next.next = tmp
    
    cur_cup = cur_cup.next

cur = mapping[1]
print(cur.next.val * cur.next.next.val)