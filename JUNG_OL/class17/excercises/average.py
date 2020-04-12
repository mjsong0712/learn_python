n = int(raw_input())
for i in range(n):
	score = raw_input().split()[1:]
	score = map(int,score)
	avg = float(sum(score))/len(score)
	cnt = 0
	for s in score:
		if s > avg:
			cnt += 1
	
	print format(float(cnt)/len(score)*100,".3f") + "%"