import fileinput

card_pub, door_pub = map(int, fileinput.input())

print(card_pub, door_pub)
# card_pub = 5764801
# door_pub = 17807724

subject = 7

card_loop = 0
val = 1
while val != card_pub:
    val *= subject
    val %= 20201227
    card_loop += 1
    
door_loop = 0
val = 1
while val != door_pub:
    val *= subject
    val %= 20201227
    door_loop += 1

print(card_loop, door_loop)

key = 1
for _ in range(card_loop):
    key *= door_pub
    key %= 20201227

print(key)