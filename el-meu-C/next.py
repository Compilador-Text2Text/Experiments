def next_b (v):
	t = list(v)
	for i in range (len(t)):
		if t[-i-1] == '0':
			t[-i-1] = '1'
			return ''.join(t)
		else:
			t[-i-1] = '0'
	return '1' + ''.join(t)



t = '0'
for i in range (20):
	print (i, t)
	t = next_b (t)
