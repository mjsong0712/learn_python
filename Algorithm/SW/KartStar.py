t1 = raw_input().split(":")
t2 = raw_input().split(":")
t3 = raw_input().split(":")
t1 = list(map(int,t1))
t2 = list(map(int,t2))
t3 = list(map(int,t3))
n = int(raw_input())

for i in range(n):
	T = raw_input().split(":")
	if int(T[0])*60 + int(T[1]) + int(T[2])*(1/100) <int(t3[0])*60 + int(t3[1]) + int(t3[2])*(1/100) < int(t2[0])*60 + int(t2[1]) + int(t2[2])*(1/100)< int(t1[0])*60 + int(t1[1]) + int(t1[2])*(1/100):
		print("***")
	elif int(t3[0])*60 + int(t3[1]) + int(t3[2])*(1/100)< (T[0])*60 + int(T[1]) + int(T[2])*(1/100) < int(t2[0])*60 + int(t2[1]) + int(t2[2])*(1/100)< int(t1[0])*60 + int(t1[1]) + int(t1[2])*(1/100):
		print("**")
	elif int(t3[0])*60 + int(t3[1]) + int(t3[2])*(1/100) < int(t2[0])*60 + int(t2[1]) + int(t2[2])*(1/100)< (T[0])*60 + int(T[1]) + int(T[2])*(1/100)< int(t1[0])*60 + int(t1[1]) + int(t1[2])*(1/100):
		print("*")
	elif int(t3[0])*60 + int(t3[1]) + int(t3[2])*(1/100) < int(t2[0])*60 + int(t2[1]) + int(t2[2])*(1/100)<  int(t1[0])*60 + int(t1[1]) + int(t1[2])*(1/100)< (T[0])*60 + int(T[1]) + int(T[2])*(1/100):
		print(":(")