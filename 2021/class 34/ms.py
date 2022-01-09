def solution(L):
	ML = []
	if len(L) == 2:
		return 0
	for i in range(1,len(L)-1):
		ML.append(solution(L[:i]+L[i+1:])+L[i-1]*L[i]*L[i+1])

	return max(ML)

k = input().split(' ')

k = list(map(int,k))

print(solution(k))