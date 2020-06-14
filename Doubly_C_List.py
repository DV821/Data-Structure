class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("No Nodes")
            return
        ptr = self.head
        count = 0
        while (True):
            print(ptr.data, end="\t")
            count += 1
            if (ptr.next == self.head):
                break
            ptr = ptr.next
        print("\nNo. of Nodes :", count)

    def printRevList(self):
        if self.head is None:
            print("No Nodes")
            return
        ptr = self.head.prev
        count = 0
        while (True):
            print(ptr.data, end = "\t")
            count += 1
            if(ptr.prev == self.head.prev):
                break
            ptr = ptr.prev
        print("\nNo. of Nodes :",count)


    def append(self,data):
        new = Node(data)
        if self.head is None:
            new.next = new
            new.prev = new
            self.head = new
            return
        ptr = self.head
        while(ptr.next != self.head):
            ptr = ptr.next
        new.prev = ptr
        ptr.next = new
        new.next = self.head
        self.head.prev = new

    def prepend(self,data):
        new = Node(data)
        if self.head is None:
            new.next = new
            new.prev = new
            self.head = new
            return
        ptr = self.head
        while(ptr.next != self.head):
            ptr = ptr.next
        ptr.next = new
        new.prev = ptr
        self.head.prev = new
        new.next = self.head
        self.head = new

    def node_at_ind(self,data,i):
        new = Node(data)
        if self.head is None:
            new.next = new
            new.prev = new
            self.head = new
            return
        ptr = self.head
        ptr1 = ptr
        j=0
        while j < i:
            ptr1 = ptr
            ptr = ptr.next
            j+=1
            if(ptr.next == self.head):
                break
        new.prev = ptr1
        new.next = ptr
        ptr1.next = new
        ptr.prev = new

    def data_at_ind(self,i):
        if self.head is None:
            print("No Nodes")
            return
        ptr = self.head
        j = 0
        while j < i:
            if (ptr.next == self.head):
                print("Not Enough Nodes")
                return
            ptr = ptr.next
            j += 1
        print(ptr.data)

if __name__ == '__main__':
    dl = DList()
    dl.data_at_ind(5)
    l = [1,2,3,4]
    for i in l:
        dl.append(i)
    dl.printList()
    dl.prepend(l)
    dl.prepend("hey")
    dl.printList()
    dl.printRevList()
    dl.data_at_ind(3)
    dl.node_at_ind("hi",2)
    dl.printList()