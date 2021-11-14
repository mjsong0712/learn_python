def mergeSort(L):
	R = []
	if len(L) < 2:
		return L
	L1 = mergeSort(L[:len(L)//2])
	L2 = mergeSort(L[len(L)//2:])
	
	i = 0
	j = 0

	while len(R) != len(L):
		if i == len(L1) and j != len(L2):
			R.append(L2[j])
			j +=1
		elif i != len(L1) and j == len(L2):
			R.append(L1[i])
			i +=1

		elif L1[i][1] < L2[j][1]:
			R.append(L1[i])
			i +=1
		else:
			if L1[i][1] == L2[j][1]:
				if L1[i][0] == L1[i][1]:
					R.append(L2[j])
					j+=1
				else:
					R.append(L1[i])
					i+=1
			else:		
				R.append(L2[j])
				j +=1



	return R




n = int(input())
L = []

for i in range(n):
	T = input().split(' ')

	start = int(T[0])
	end = int(T[1])

	L.append((start,end))	

S = mergeSort(L)
mL = []
# ans = [S[0]]

# for i in range(1,len(S)):
# 	if ans[-1][1] <= S[i][0]:
# 		ans.append(S[i])


# print(len(ans))
end = 0
cnt = 0
for i in range(0,len(S)):
	if end <= S[i][0]:
		cnt += 1
		end = S[i][1]

print(cnt)