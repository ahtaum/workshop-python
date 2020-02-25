from collections import deque
antrian = deque(["eriq", "john", "Michael"])
antrian.append("Terry")
antrian.append("Graham")

print (antrian.popleft())
print (antrian.popleft())

print (antrian)
