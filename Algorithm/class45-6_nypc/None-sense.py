def calc(x,y,op):
	if op == 0:
		return x+y
	if op == 1:
		return x-y
	if op == 2:
		return x*y
	if op == 3:
		return x/float(y)
	if op == 4:
		return x+y*0.1




def None_Sense(A, B, C, D):
	def strMaker(i, j):
		D1 = {
			0:"+",
			1:"-",
			2:"*",
			3:"/",
			4:"."
		}
		return str(A)+D1[i]+str(B)+D1[j]+str(C)+"="+str(D)


	for i in range(5): # 0:+, 1:-, 2: x, 3:/, 4:.
		for j in range(5):
			if i == j:
				continue
			if i in (0,1):
				if j in (0,1):
					if calc( calc(A,B,i), C, j) == D:
						return strMaker(i,j)
				elif j in (2,3,4):
					if  calc(A, calc(B,C,j), i) == D:
						return strMaker(i,j)
			elif i in (2,3):
				if j in (0,1,2,3):
					if calc( calc(A,B,i), C, j) == D:
						return strMaker(i,j)
				elif j == 4:
					if  calc(A, calc(B,C,j), i) == D:
						return strMaker(i,j)
			elif i == 4:
				if calc( calc(A,B,i), C, j) == D:
						return strMaker(i,j)




n = int(raw_input())

for i in range(n):
	p = raw_input().split()
	print(None_Sense(int(p[0]),int(p[1]),int(p[2]),int(p[3])))

