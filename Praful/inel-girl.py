s = map(int, raw_input().strip())
c = 0
r = ''
for i in s :
	if i%2 == 0 :
		c += 1
for i in s :
	if i%2 == 0 :
		r += str(c) + " "
		c -= 1
	else :
		r += str(c) + " "
print r
	
