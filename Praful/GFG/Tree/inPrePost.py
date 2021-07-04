class node :
	def __init__ (self, key) :
		self.l = None
		self.r = None
		self.v = key

def printPre(root) :
	if root :
		print (root.v),
		printPre (root.l)
		printPre (root.r)

def printPost (root) :
	if root :
		printPost (root.l)
		print (root.v),
		printPost (root.r)

def printIn (root) :
	if root :
		printIn (root.l)
		printIn (root.r)
		print (root.v)

if __name__ == '__main__' :
	root = node(1) 
	root.l = node(2)
	root.r = node(3)
	root.l.l = node(4)
	root.l.r = node(5)
	printPre (root)

