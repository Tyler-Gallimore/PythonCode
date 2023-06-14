N = int(input())

list_test = []

for i in range(N):
    extra = input().split()
    if extra[0] == "insert":
        list_test.insert(int(extra[1]), int(extra[2]))
    elif extra[0] == "print":
        print(list_test)
    elif extra[0] == "remove":
        list_test.remove(int(extra[1]))
    elif extra[0] == "append":
        list_test.append(int(extra[1]))
    elif extra[0] == "sort":
        list_test.sort()
    elif extra[0] == "pop":
        list_test.pop()
    elif extra[0] == "reverse":
        list_test.reverse()