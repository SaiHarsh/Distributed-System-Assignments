"""
Case (i) almost completed
Remaining 2 cases are pending.
Find closeness centrality.
"""
import queue, time, random
class data:
	def __init__(self):
		self.vertices = set()
		self.non_artic = set()
		# Later it will become dict of dict.
		self.distance = {}
		self.check = {}
		self.numSampleNodes = 0
		self.numAllVertice = 0

class functions:
	def __init__(self):
		self.g = True
		self.treeVertices = True
		self.reverseTreeVertices = {}
		self.T = True
		self.parent = True
	
	def calculateLCA(self,i,j):
		ans  = False
		tmp = self.treeVertices[i]
		list1 = []
		while(tmp!=-1):
			list1.append(tmp)
			tmp = self.parent[tmp]

		tmp = self.treeVertices[j]
		list2 = []
		while(tmp!=-1):
			list2.append(tmp)
			tmp = self.parent[tmp]

		# Find the match i.e LCA
		len1 = len(list1) - 1
		len2 = len(list2) - 1
		while(len1>=0 and len2>=0):
			if(list1[len1]!=list2[len2]):
				# print "LCA ", list1[len1+1]
				ans = list1[len1+1]
				break
			len1 -= 1
			len2 -= 1

		if ans==False:
			ans = list1[len1+1]
		del list1
		del list2
		del len1
		del len2

		return ans

if __name__ == '__main__':
	f = open(sys.argv[1])
	#f = open('/home/harsh/Desktop/Try/id2010_connected.mtx')
	print("Reading..")
	lenRowOffset = int(f.readline()) #input()
	rowOffset = ["Dummy"]
	rowOffset += map(int, f.readline().split())#map(int,raw_input().split())
	# print rowOffset
	lenColumnOffset = int(f.readline()) #input()
	columnOffset = ["Dummy"]
	columnOffset += map(int, f.readline().split())#map(int,raw_input().split())
	print("completed reading")
	# print columnOffset
	G = {}
	for i in range(1, lenRowOffset):
		G[i] = []
		#print i,":",
		for j in range(int(rowOffset[i]), int(rowOffset[i+1])):
			#print columnOffset[j],
			G[i].append(columnOffset[j])
		#print
	#print int(rowOffset[lenRowOffset])
	G[lenRowOffset] = []
	for j in range(int(rowOffset[lenRowOffset]), lenColumnOffset+1):
		G[lenRowOffset].append(columnOffset[j])
	#print G
	print("Making Graph")
	function = functions()
	function.g = Graph(G)
	function.T = function.g.blocks_and_cuts_tree()
	function.treeVertices = function.T.vertices()
	for i in range(len(function.treeVertices)):
		function.reverseTreeVertices[function.treeVertices[i]] = i
	print("Completed Making Graph")
	del rowOffset
	del columnOffset
	del lenColumnOffset

	print("Make Parent array")
	# Create a parent tree format
	visited = {}
	for v in function.treeVertices:
		visited[v] = False
	nonSampleDistance = [0 for i in range(lenRowOffset+1)]
	nearest = [False for i in range(lenRowOffset+1)]
	nearest_distance = [False for i in range(lenRowOffset+1)]
	parent = {}
	q = queue.Queue()
	q.put(function.treeVertices[0])
	parent[function.treeVertices[0]] = -1
	visited[function.treeVertices[0]] = True
	while not q.empty():
		v = q.get()
		for u in function.T.neighbor_iterator(v):
			if not visited[u]:
				parent[u] = v
				visited[u] = True
				q.put(u)
	#print parent
	function.parent = parent
	del parent
	# Delete the not reusable variables
	del visited
	del q
	print("Completed Making Parent array")

	# Creating mapping between blocks and vertices.
	print("Create Mapping List")
	numBlocks = 0
	map_list = {i:0 for i in range(lenRowOffset+1)}
	init_check = {}
	for label, v_list in function.treeVertices:
		if label=='C':
			map_list[v_list] = v_list
			init_check[v_list] = False
		else:
			numBlocks += 1
	map_list['s1'] = -1
	map_list['s2'] = -1
	print("Completed Create Mapping List")

	Data = []
	visited = {}
	init_visited = {}
	print("Run Individual BFS")
	start_time = time.time()
	percentage = 20.0
	num_sample = 0
	for b in range(numBlocks):
		Data.append(data())
		block_set = set()
		needed = ceil((len(function.treeVertices[b][1])*percentage)/100)
		for v in function.treeVertices[b][1]:
			if map_list[v]:
				Data[b].vertices.add(v)
				Data[b].distance[v] = {}
				Data[b].check[v] = copy(init_check)
			block_set.add(v)
			init_visited[v] = False

		# sampled nodes are less than needed, append more.
		# Exclude the running time.
		current = len(Data[b].vertices)
		if(needed>current):
			tVertices = list(function.treeVertices[b][1])
			random.shuffle(tVertices)
			for v in tVertices:
				if(current>=needed):
					break
				if v not in Data[b].vertices:
					Data[b].non_artic.add(v)
					Data[b].distance[v] = {}
					current += 1			
		num_sample += current
		
		Data[b].numSampleNodes += current
		Data[b].numAllVertice = len(block_set)

		# Data[b].vertices = set(Data[b].vertices)
		# print("Assigned memory for ",b)
		# Run Bfs
		partial_sum = 0 #It store the sum of distances of one block.
		count = 0
		l = list(Data[b].vertices)
		l += list(Data[b].non_artic)
		for s in l:
			count += 1
			print("Running for ", s, "Remaining", len(function.treeVertices[b][1]) - count)
			partial_sum = 0
			visited = copy(init_visited)
			q = queue.Queue()
			q.put(s)
			visited[s] = True
			Data[b].distance[s][s] = 0
			while not q.empty():
				v = q.get()
				for u in function.g.neighbor_iterator(v):
					if (u in block_set and not visited[u]):
						visited[u] = True
						Data[b].distance[s][u] = Data[b].distance[s][v] + 1
						q.put(u)
						partial_sum += Data[b].distance[s][u]

						# Updating
						nonSampleDistance[u] += Data[b].distance[s][u]
			del q
			Data[b].distance[s]['s1'] = partial_sum 
			Data[b].distance[s]['s2'] = 0

		# Size should not increase
		visited = {}
		init_visited = {}

		# include the remaining nodes distances
		for v in Data[b].non_artic:
			d = {}
			d[s1] = Data[b].distance[v]['s1']
			d[s2] = Data[b].distance[v]['s1']
			Data[b].distance[v] = copy(d)
			
	print("======================================================================")
	print(len(Data))
	print("Completed Running Individual BFS")
	# Delete the not reusable variables
	del visited
	del init_visited
	connectionDistance = 0
	flag = True
	print("Finding connectionDistance...")
	for bi in range(numBlocks):
		for bj in range(bi, numBlocks):
			if bi==bj:
				continue
			#print(bi,bj)
			LCA = function.calculateLCA(bi,bj)
			#print(len(LCA))
			if(function.treeVertices[bi]==LCA or function.treeVertices[bj]==LCA):
				if(function.treeVertices[bj]==LCA):
					i = bj
					j = bi
				else:
					i = bi
					j = bj
				# Find Minimum
				start = function.parent[function.treeVertices[j]]
				connectionDistance = 0
				while(start!=LCA and function.parent[start]!=LCA):
					# start is a cut vertex as j is as block 
					blockIndex = function.reverseTreeVertices[function.parent[start]]
					connectionDistance += Data[blockIndex].distance[start[1]][function.parent[function.parent[start]][1]]
					start = function.parent[function.parent[start]]
				# Update the distances in both the blocks
				# Updating for block i
				# It will be a cut vertex and [1] means it's node.
				reference_i = start[1]
				reference_j = function.parent[function.treeVertices[j]][1]
				#Data[i].distance[start[1]]['s2'] += Data[j].distance[reference_j]['s1']
				for v in Data[i].distance:
					#Data[i].distance[v]['s2'] = Data[i].distance[v]['s2'] + Data[i].distance[v][reference_i]*len(Data[j].distance[reference_j]) + connectionDistance*len(Data[j].distance[reference_j]) + Data[j].distance[reference_j]['s1']
					for u in Data[j].distance[reference_j]:
						add_var = Data[j].distance[reference_j][u] + Data[i].distance[v][reference_i] + connectionDistance
						
						if(map_list[u] == 0):
							Data[i].distance[v]['s2'] += add_var
						elif(map_list[u]>0):
							if(u in Data[i].vertices):
								pass
							elif(not Data[i].check[reference_i][u]):
								Data[i].distance[v]['s2'] += add_var
								Data[i].check[reference_i][u] = add_var

							elif(add_var < Data[i].check[reference_i][u]):
								Data[i].distance[v]['s2'] = Data[i].distance[v]['s2'] + add_var - Data[i].check[reference_i][u]
								Data[i].check[reference_i][u] = add_var

				# Update for block 2
				# reference_i will give me reference node 
				for v in Data[j].distance:
					#Data[j].distance[v]['s2'] = Data[j].distance[v]['s2'] + Data[j].distance[v][reference_j]*len(Data[i].distance[reference_i]) + connectionDistance*len(Data[i].distance[reference_i]) + Data[i].distance[reference_i]['s1']
					#Data[j].distance[v]['s2'] = Data[j].distance[v]['s2'] + Data[j].distance[v][reference_j]*len(Data[i].distance[reference_i]) + connectionDistance*len(Data[i].distance[reference_i])
					for u in Data[i].distance[reference_i]:
						add_var = Data[i].distance[reference_i][u] + Data[j].distance[v][reference_j] + connectionDistance
						if(map_list[u] == 0):
							Data[j].distance[v]['s2'] += add_var
						elif(map_list[u]>0):
							if(u in Data[j].vertices):
								pass
							elif(not Data[j].check[reference_j][u]):
								Data[j].distance[v]['s2'] += add_var
								Data[j].check[reference_j][u] = add_var
							elif(add_var < Data[j].check[reference_j][u]):
								Data[j].distance[v]['s2'] = Data[j].distance[v]['s2'] + add_var - Data[j].check[reference_j][u]
								Data[j].check[reference_j][u] = add_var
			else:
				# Contribution of block bi
				start = function.parent[function.treeVertices[bi]]
				connectionDistance = 0
				while(start!=LCA and function.parent[start]!=LCA):
					blockIndex = function.reverseTreeVertices[function.parent[start]]
					connectionDistance += Data[blockIndex].distance[start[1]][function.parent[function.parent[start]][1]]
					start = function.parent[function.parent[start]]
				# One block can have many cut nodes.
				stopAt = start[1]

				start = function.parent[function.treeVertices[bj]]
				while(start!=LCA and function.parent[start]!=LCA):
					blockIndex = function.reverseTreeVertices[function.parent[start]]
					connectionDistance += Data[blockIndex].distance[start[1]][function.parent[function.parent[start]][1]]
					start = function.parent[function.parent[start]]
				blockIndex = function.reverseTreeVertices[LCA]
				if(stopAt != start[1]):
					connectionDistance += Data[blockIndex].distance[start[1]][stopAt]

				# function.Parent is a cut vertex, [1] will give the node value.
				reference_i = function.parent[function.treeVertices[bi]][1]
				reference_j = function.parent[function.treeVertices[bj]][1]
				# Update the distances of block bi
				for v in Data[bi].distance:
					#Data[bi].distance[v]['s2'] = Data[bi].distance[v]['s2'] + Data[bi].distance[v][reference_i]*len(Data[bj].distance[reference_j]) + connectionDistance*len(Data[bj].distance[reference_j]) + Data[bj].distance[reference_j]['s1']
					for u in Data[bj].distance[reference_j]:
						add_var = Data[bj].distance[reference_j][u] + Data[bi].distance[v][reference_i] + connectionDistance
						if(map_list[u] == 0):
							Data[bi].distance[v]['s2'] += add_var
						elif(map_list[u]>0):
							if(u in Data[bi].vertices):
								pass
							if(not Data[bi].check[reference_i][u]):
								Data[bi].distance[v]['s2'] += add_var
								Data[bi].check[reference_i][u] = add_var

							elif(add_var < Data[bi].check[reference_i][u]):
								Data[bi].distance[v]['s2'] = Data[bi].distance[v]['s2'] + add_var - Data[bi].check[reference_i][u]
								Data[bi].check[reference_i][u] = add_var

				# Update for block bj
				# reference_i will give me reference node 
				for v in Data[bj].distance:
					#Data[bj].distance[v]['s2'] = Data[bj].distance[v]['s2'] + Data[bj].distance[v][reference_j]*len(Data[bi].distance[reference_i]) + connectionDistance*len(Data[bi].distance[reference_i]) + Data[bi].distance[reference_i]['s1']
					for u in Data[bi].distance[reference_i]:
						add_var = Data[bi].distance[reference_i][u] + Data[bj].distance[v][reference_j] + connectionDistance
						if(map_list[u] == 0):
							Data[bj].distance[v]['s2'] += add_var
						elif(map_list[u]>0):
							if(u in Data[bj].vertices):
								pass
							if(not Data[bj].check[reference_j][u]):
								Data[bj].distance[v]['s2'] += add_var
								Data[bj].check[reference_j][u] = add_var
							elif(add_var < Data[bj].check[reference_j][u]):
								Data[bj].distance[v]['s2'] = Data[bj].distance[v]['s2'] + add_var - Data[bj].check[reference_j][u]
								Data[bj].check[reference_j][u] = add_var
			#print("Done")
			#print function.treeVertices[bi], function.treeVertices[bj], LCA, connectionDistance
			# print(bi,bj)
			# print(function.treeVertices[bi], function.treeVertices[bj])
			# print(Data[i].distance)
			# print(Data[j].distance)
			# print("===========================================================================")
	# Update s2 with s1

	for i in Data:
		for v in i.vertices:
			i.distance[v]['s2'] += i.distance[v]['s1']

	# for i in Data:
	# 	print i.vertices
	# 	print i.distance
	# 	print
	print("Centrality..")
	Centrality = {}
	# Calculate Centrality for cut vertices
	check = [False]*(lenRowOffset+1)
	for i in Data:
		for v in i.vertices:
			if not check[v]:
				Centrality[v] = round(float(lenRowOffset-1)/i.distance[v]['s2'],4)
				check[v] = True
			else:
				tmp = float(lenRowOffset-1)/i.distance[v]['s2']
				#print v, tmp, Centrality[v]
				if round(tmp,4) > Centrality[v]:
					Centrality[v] = round(tmp,4)

	# Updating for non-artic
	tmp_distance = []
	for i in Data:
		for v in i.non_artic:
			no_remaining_nodes = lenRowOffset-1-len(i.numAllVertice)
			firstNode = i.vertices.pop()
			tmp_distance = i.distance[firstNode][v]*(no_remaining_nodes) + i.distance[firstNode]['s2']
			i.vertices.add(firstNode)
			for u in i.vertices:
				if tmp_distance > i.distance[u][v]*(no_remaining_nodes) + i.distance[u]['s2']:
					tmp_distance = i.distance[u][v]*(no_remaining_nodes) + i.distance[u]['s2']
			i.distance[v]['s2'] = tmp_distance
			Centrality[v] = round(float(lenRowOffset-1)/i.distance[v]['s2'],4)

	# Calculate Centrality for remaining nodes
	tmp_distance = []
	for i in Data:
		for u in i.vertices:
			for v in i.distance[u]:
				# v is a remaining vertex
				if(map_list[v]==0):
					for w in i.vertices:
						#print w
						tmp_distance.append(i.distance[w][v]*(lenRowOffset-1-i.numAllVertice) + i.distance[w]['s2'])
					#print(v,(tmp_distance))
					#print(min(tmp_distance))
					Centrality[v] = round(float(lenRowOffset-1-i.numAllVertice + i.numSampleNodes)/(min(tmp_distance) + nonSampleDistance[v]),4)
					tmp_distance = []
			break
	#print Centrality
	end_time = time.time()
	print("Time taken in msec: ", round((end_time - start_time)*1000,2))
	print("Number of Sample Nodes:", num_sample)
	print("Writing...")
	fname = sys.argv[2]
	fileName = open(fname, "w+")
	lineText = []
	for v in Centrality:
		lineText.append(str(Centrality[v])+' ')
	fileName.writelines(lineText)
	fileName.close()
	print("Completed Please see ", fname)