my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"The appended values result: {my_list}")
my_list.insert(2, 15)
print(f"After inserting 15 at index 2: {my_list}")
my_list.extend([50, 60, 70])
print(f"List after extending another array to it: {my_list}")
my_list.pop()
print(f"Removing the last element: {my_list}")
my_list.sort()

print(f"Sorted array: {my_list}")

for i in range(len(my_list)):
    if my_list[i] == 30:
        print(f"The index of 30 is: {i}")


