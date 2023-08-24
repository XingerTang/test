import numpy as np

true = np.loadtxt("src/test/trueGenotypes.txt")
nind = true.shape[0]
nLoci = true.shape[1] - 1
maf = np.full((nLoci), 0.5)
for locus in range(nLoci):
    geno = true[:, (1 + locus)]
    n_aA_Aa = nLoci - np.count_nonzero(geno - 1)
    n_AA = nLoci - np.count_nonzero(geno - 2)
    maf[locus] = (1 /(2 * nind)) * (n_aA_Aa + 2 * n_AA)


est_maf = np.loadtxt("src/test/peeling.single.estmaf.maf")
print(np.corrcoef(maf, est_maf)[0, 1])