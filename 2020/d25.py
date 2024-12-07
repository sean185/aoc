card_pk, door_pk = (5764801, 17807724) # eg
card_pk, door_pk = (15628416, 11161639) # actual

def count_loops(pk):
    n = 1
    s = 7
    i = 0
    while n != pk:
        n = (n * s) % 20201227
        i += 1
    return i

def loop(s, c):
    n = 1
    for _ in range(c):
        n = (n * s) % 20201227
    return n

card_secret = count_loops(card_pk)
door_secret = count_loops(door_pk)
print(card_secret, door_secret)
print(loop(card_pk, door_secret))
print(loop(door_pk, card_secret))
