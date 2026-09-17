import pythonds3

s = pythonds3.Stack()

s.push("Hello")
s.push("World")

item = s.pop()
print(item)
item = s.pop()
print(item)
if not s.is_empty():
    item = s.pop()
    
print(item)