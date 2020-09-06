
def main():
	inp = raw_input().split()
	A = int(inp[0])
	B = int(inp[1])
	C = int(inp[2])

	if C<=B:
		print -1
		return

	#float(A)/float(C-B)
	#if A%(C-B) == 0:
	print A/(C-B) + 1


main()