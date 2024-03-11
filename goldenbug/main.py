def hamming_distance(p, q):
    "calculates the hamming distance between two sequences p and q"
    dist = 0
    n = len(p)
    for i in range(n):
        if p[i] != q[i]:
            dist += 1
    return dist

def genotype(geno_one, geno_two):
    "calculates recombination of two alleles"
    geno_one = sorted(geno_one, key=lambda L: (L.lower(), L))
    geno_two = sorted(geno_two, key=lambda L: (L.lower(), L))

    sorted_geno_one = []
    sorted_geno_two = []
    for i in range(0, len(geno_one), 2):
        sorted_geno_one.append(geno_one[i:i+2])
        sorted_geno_two.append(geno_two[i:i+2])
    print(sorted_geno_one)
    print(sorted_geno_two)

    for i in range(len(sorted_geno_one)):
        for j in range(len(sorted_geno_one[0])):
            for k in range(len(sorted_geno_one[0])):
                print(sorted_geno_one[i][k] + sorted_geno_two[i][j])
