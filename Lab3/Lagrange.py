def Lagrange(nodes: list, inter_point) -> float:
	f_inter_point = 0
	mult = 1

	for i in range(len(nodes)):
		for j in range(len(nodes)):
			if j == i:
				continue
			mult *= (inter_point-nodes[j].x)/(nodes[i].x-nodes[j].x)
		f_inter_point += nodes[i].f * mult
		mult = 1

	return f_inter_point

