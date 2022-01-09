T = int(input())
for i in range(T):
	mn = 100000000
	K = int(input())
	DP = [[0 for _ in range(K)] for k in range(K)]
	L = input().split(' ')
	L = list(map(int,L))

	for n in range(1,K):
		for l in range(K-n):
			for k in range(n):
				tmp = DP[l][l+k] + DP[l+k+1][l+n]
				if mn > tmp:
					mn = tmp
				DP[l][l+n] = mn + sum(L[l:l+n+1])
					
	print(DP[0][K-1])
					
				
		
