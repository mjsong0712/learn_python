def Finder(S, L):
	mx = L[0]
	index = 0
	for i in range(len(L)):
		if (S-mx)**2 == (S-L[i])**2:
			if L[i] < mx:
				mx = L[i]
				index = i
		elif (S-mx)**2 < (S-L[i])**2:
			index = i
			mx = L[i]
	return index





N = int(raw_input())
S, K = raw_input().split()
S, K = int(S), int(K)

P = raw_input().split()
P = list(map(int, P))

L = P[:K]


# 1. 처음에 finder로 초기 제일 실력차 큰 애 index 뽑고
# 2. 이후 원소들 걔랑 비교해서 새 원소가 더 실력차 작을때
# 1번의 걔랑 새 원소랑 바꾸고, finder 다시 돌려서
# 1번부터 반복


