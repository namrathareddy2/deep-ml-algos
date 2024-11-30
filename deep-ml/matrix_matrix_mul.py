def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	row_a = len(a)
	col_a = len(a[0])
	row_b = len(b)
	col_b = len(b[0])
	c = []
	if col_a == row_b:
		for i in range(row_a):
			res = []
			for j in range(col_b):
				s = 0
				for k in range(row_b):
					s = s + a[i][k] * b[k][j]
				res.append(s)
            #if len(res) == col_b:
			c.append(res)
		return c
	else:
		return -1