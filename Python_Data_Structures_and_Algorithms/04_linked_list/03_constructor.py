class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value: any) -> None:
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value: any) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self) -> None:
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None

    def __repr__(self) -> str:
        val = ""
        temp = self.head
        while temp:
            val += str(temp.value) + " -> "
            temp = temp.next
        return val + "None"


ll = Linkedlist(4)
ll.append(3)
ll.append(23)
print(ll)
ll.pop()
print(ll)
ll.pop()
print(ll)
ll.pop()
print(ll)
