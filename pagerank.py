import numpy as np
import numpy.linalg as la

#power iteration method
def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + (1-d) / n * np.ones([n,n])
    r = 100 * np.ones(n) / n
    lastR = r
    r = M @ r
    while la.norm(lastR - r) > 0.01:
        lastR = r
        r = M @ r

    return r

if __name__ == "__main__":
    #construct L from the links of the webpages, read the description
    websites = ['A','B','C','D','E','F'] #websites
    L = np.array([[0,   1/2, 1/3, 0, 0,   0 ],
              [1/3, 0,   0,   0, 1/2, 0 ],
              [1/3, 1/2, 0,   1, 0,   1/2 ],
              [1/3, 0,   1/3, 0, 1/2, 1/2 ],
              [0,   0,   0,   0, 0,   0 ],
              [0,   0,   1/3, 0, 0,   0 ]])

    r = pageRank(L,1)
    i = 0
    dict = {}
    for site in websites:
        dict[site] = r[i]
        i += 1

    # sorted returns list of tuples
    sortedValue = sorted(dict.items(), key = lambda x: x[1], reverse = True)
    for k, p in sortedValue:
        print("Site:", k ,"Rank: ", p)
