class Node:
    def __init__(self, name, admission, units):
        self.data = {
            "name": name,
            "admission": admission,
            "units": units
        }
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, name, admission, units):
        new_node = Node(name, admission, units)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print("Name:", current.data["name"])
            print("Admission:", current.data["admission"])
            print("Units:", current.data["units"])
            print()
            current = current.next

ll = LinkedList()

for i in range(3):
    name = input("Name: ")
    admission = input("Admission number: ")
    units = [
        input("Unit 1: "),
        input("Unit 2: "),
        input("Unit 3: ")
    ]

    ll.add(name, admission, units)

ll.display()