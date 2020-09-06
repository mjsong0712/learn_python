def ox(result):
	score = [0 for i in range(len(result))]
	if result[0] == "O":
		score[0] = 1
	for i in range(1,len(result)):
		if result[i] == "O":
			score[i] = score[i-1] + 1
	return sum(score)


n = int(raw_input())
for i in range(n):
	m = raw_input()
	print ox(m)