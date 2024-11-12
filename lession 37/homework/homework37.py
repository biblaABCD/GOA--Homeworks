def list():
    list = ["apple", "banana", "cherry", "date", "elderberry"]
    print(list)
    print(list[0], list[4])
    list.append("fig")
    list.remove("banana")
    list.insert(2, "blueberry")
    print(list)
    print(len(list))

list()
