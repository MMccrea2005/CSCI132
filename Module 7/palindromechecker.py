from pythonds3.basic import Deque


def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        if ch == " ":
            continue
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
print(pal_checker("I PREFER PI"))