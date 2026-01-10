def hamming_distance(p, q):
    "calculates the hamming distance between two sequences p and q"
    dist = 0
    n = len(p)
    for i in range(n):
        if p[i] != q[i]:
            dist += 1
    return dist

def genotypes(geno_one, geno_two):
    "calculates recombination of two alleles, at the moment only for 2 alleles (16 genotypes)"
    geno_one = sorted(geno_one, key=lambda L: (L.lower(), L))
    geno_two = sorted(geno_two, key=lambda L: (L.lower(), L))
    sorted_geno_one = []
    sorted_geno_two = []
    for i in range(0, len(geno_one), 2):
        sorted_geno_one.append(geno_one[i:i+2])
        sorted_geno_two.append(geno_two[i:i+2])
    result_one = []
    for i in range(len(sorted_geno_one[0])):
        for j in range(len(sorted_geno_one[0])):
            for k in range(len(sorted_geno_one[0])):
                temp = ''
                for l in range(len(sorted_geno_one[0])):
                    if l == i:
                        temp += sorted_geno_one[l][j]
                    else:
                        temp += sorted_geno_one[l][k]
                result_one.append(temp)
    result_two = []
    for i in range(len(sorted_geno_two[0])):
        for j in range(len(sorted_geno_two[0])):
            for k in range(len(sorted_geno_two[0])):
                temp = ''
                for l in range(len(sorted_geno_two[0])):
                    if l == i:
                        temp += sorted_geno_two[l][j]
                    else:
                        temp += sorted_geno_two[l][k]
                result_two.append(temp)
    result_one = result_one[:len(result_one)//2]
    result_two = result_two[:len(result_two)//2]
    list_of_genotypes = []
    for i in range(len(result_one)):
        for j in range(len(result_two)):
            list_of_genotypes.append(''.join(sorted(result_one[i] + result_two[j], key=lambda L: (L.lower(), L))))
    return list_of_genotypes

def genotypic_frequency(particular, list_of_genotypes):
    "calculates the frequency of occurance in a list of genotype"
    particular = ''.join(sorted(particular, key=lambda L: (L.lower(), L)))
    number_of_occurances = list_of_genotypes.count(particular)
    frequency = number_of_occurances*100/len(list_of_genotypes)
    return frequency
