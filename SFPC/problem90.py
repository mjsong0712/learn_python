def kaycha(n,m,d):
	return (n*m)+d



a, m, d, n = input().split()

a, m, d, n = int(a),int(m),int(d),int(n)

tmp = a
cnt = 0

for i in range(n):
	tmp = kaycha(tmp,m,d)

print(tmp)