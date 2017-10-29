for _ in range (input()) :
	s = raw_input().strip();
	r = "abcdefghijklmnopqrstuvwxyz"
	flag = 0
	for i in r :
		if s.count(i) >= 2 :
			flag = 1
			break
	if flag == 0:
		print "no"
	else :
		print "yes"
