names = []

for _ in range(10):
    entered_name = input("Enter a name: ")
    names.append(entered_name)

print("Names in the queue:")
for name in names:
    print(name)

print("Dequeuing names:")
for _ in range(len(names)):
    print(names.pop(0))

print("Names in the queue after dequeue:")
for name in names:
    print(name)
