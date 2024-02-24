def hamming_distance(p, q):
    dist = 0
    n = len(p)
    for i in range(n):
        if p[i] != q[i]:
            dist += 1
    return dist