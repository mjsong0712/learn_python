class Node:
	def __init__(self,value):
		self.lc = None
		self.rc = None 
		self.value = value


def inorder(N):
	if N.lc != None:
		inorder(N.lc)
	print N.value
	if N.rc != None:
		inorder(N.rc) 
	


root = Node(15)
root.lc = Node(13)
root.rc = Node(14)

root.lc.lc = Node(9)
root.lc.rc = Node(10)
root.rc.lc = Node(11)
root.rc.rc = Node(12)

root.lc.lc.lc = Node(1)
root.lc.lc.rc = Node(2)
root.lc.rc.lc = Node(3)
root.lc.rc.rc = Node(4)
root.rc.lc.lc = Node(5)
root.rc.lc.rc = Node(6)
root.rc.rc.lc = Node(7)
root.rc.rc.rc = Node(8)


inorder(root)