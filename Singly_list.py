# SINGLY LINKED LIST

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LList:
	def __init__(self):
		self.first = None

	def printList(self):
		if self.first is None:
			print("No Nodes")
			return
		curr = self.first
		count = 0
		while curr:
			print(curr.data,end = "\t")
			curr = curr.next
			count += 1
		print("\nNo. of Nodes :",count)

	def append(self,data):
		new = Node(data)
		if self.first is None:
			self.first = new
			return
		ptr = self.first
		while ptr.next:
			ptr = ptr.next
		ptr.next = new

	def prepend(self,data):
		new = Node(data)
		new.next = self.first
		self.first = new

	def node_at_ind(self,i,data):
		new = Node(data)
		ptr = self.first
		j = 0
		while j <= i-1:
			ptr = ptr.next
			j += 1
			if ptr.next is  None:
				break
		new.next = ptr.next
		ptr.next = new


	def data_at_ind(self,i):
		ptr = self.first
		j = 0
		while j<i:
			ptr = ptr.next
			j+=1
		print(ptr.data)

if __name__ == '__main__':
	ll = LList()
	ll.printList()
	list = [1,2,3,4,5,6,7,8,9,0]
	for item in list:
		ll.append(item)
	ll.prepend(list)
	ll.printList()
	ll.node_at_ind(15,list)
	ll.printList()
	ll.data_at_ind(5)
