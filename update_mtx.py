import os,sys
boolEdge = {}
fp=open(sys.argv[1],"r")
fp.readline()
line = map(int, fp.readline().split())
numOfNodes = line[0]
numOfEdges = line[2]
deg=[0] * (numOfNodes + 1)
for i in range(0,numOfEdges):
	line = map(int, fp.readline().split())
	deg[line[0]] += 1
	deg[line[1]] += 1
fp.close()
fp=open(sys.argv[1],"r")
fp.readline()
fp.readline()
print numOfNodes
for i in range(0,numOfEdges):
	line = map(int, fp.readline().split())
	if (deg[line[0]] > 2) and (deg[line[1]] > 2):
		try:
			if(boolEdge[tuple([line[0], line[1]])]):
				pass
		except:
			boolEdge[tuple([line[0], line[1]])] = True
			boolEdge[tuple([line[1], line[0]])] = True
			print line[0],line[1]

fp.close()

chainsFile = sys.argv[1] + ".chains"
fp=open(chainsFile,"r")
numOfChains = int(fp.readline())
line = map(int, fp.readline().split())
chian_rowOffset = line
line = map(int, fp.readline().split())
chian_labelOffset = line
columnOffsetLength = int(fp.readline())
line = map(int, fp.readline().split())
chian_columnOffset = line
for i in range(0,(numOfChains)):
	start = chian_rowOffset[i]
	if i == (numOfChains - 1):
		end = columnOffsetLength+1
	else:
		end = chian_rowOffset[i+1]

	try:
		if(boolEdge[tuple([chian_columnOffset[start-1],chian_columnOffset[end-1-1]])]):
			pass
	except:
		boolEdge[tuple([chian_columnOffset[start-1],chian_columnOffset[end-1-1]])] = True
		boolEdge[tuple([chian_columnOffset[end-1-1],chian_columnOffset[start-1]])] = True
		print chian_columnOffset[start-1],chian_columnOffset[end-1-1]

fp.close()