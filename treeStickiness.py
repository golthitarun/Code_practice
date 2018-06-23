
import sys
class Solution:
	class Node:
		def __init__(self,id):
			self.id = id
			self.children = []
	class Edge:
		def __init__(self,stickiness):
			self.stickiness = stickiness
			self.child = None

	def dfs(self,node):
		if(not node):
			return 0
		else:
			max_val = -sys.maxsize-1
			for edge in node.children:
				max_val = max(max_val, edge.stichiness+self.dfs(edge.child))
			return max_val


	def timeToSoak(self,root):
		return self.dfs(root)