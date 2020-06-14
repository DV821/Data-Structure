#CIRCULAR LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("No Nodes")
            return
        ptr = self.head
        count = 0
        while(True):
            print(ptr.data,end="\t")
            count += 1
            if (ptr.next == self.head):
                break
            ptr = ptr.next
        print("\nNo. of Nodes :",count)

    def append(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
            return
        ptr = self.head
        while(ptr.next!=self.head):
            ptr = ptr.next
        ptr.next = new
        new.next = self.head

    def prepend(self,data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        ptr = self.head
        while(ptr.next != self.head):
            ptr = ptr.next
        new.next = self.head
        ptr.next = new
        self.head = new

    def add_at_ind(self,data,i):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        ptr = self.head
        j = 0
        while j<i-1:
            ptr = ptr.next
            j += 1
            if(ptr.next==self.head):
                break
        new.next = ptr.next
        ptr.next = new

    def data_at_ind(self, i):
        if self.head is None:
            print("No Nodes")
            return
        ptr = self.head
        j = 0
        while j < i:
            if(ptr.next == self.head):
                print("Not Enough Nodes")
                return
            ptr = ptr.next
            j += 1
        print(ptr.data)

if __name__ == '__main__':
    cl = CList()
    cl.data_at_ind(5)
    cl.printList()
    list = [1,2,3,4]
    for item in list:
        cl.append(item)
    cl.prepend(list)
    cl.printList()
    cl.add_at_ind("hello",2)
    cl.add_at_ind("hey",7)
    cl.printList()
    cl.data_at_ind(5)
    cl.data_at_ind(7)