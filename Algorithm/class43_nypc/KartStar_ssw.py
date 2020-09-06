t1 = raw_input().split(":")
t2 = raw_input().split(":")
t3 = raw_input().split(":")
t1 = list(map(int,t1))
t2 = list(map(int,t2))
t3 = list(map(int,t3))
n = int(raw_input())


def cutLine(T, cut):
	if int(T[0]) < int(cut[0]):
		return True
	if int(T[0]) > int(cut[0]):
		return False
	if int(T[1]) < int(cut[1]):
		return True
	if int(T[1]) > int(cut[1]):
		return False
	if int(T[2]) <= int(cut[2]):
		return True
	return False


for i in range(n):
	T = raw_input().split(":")
	if cutLine(T, t3):
		print("***")
	elif cutLine(T, t2):
		print("**")
	elif cutLine(T, t1):
		print("*")
	else:
		print(":(")

