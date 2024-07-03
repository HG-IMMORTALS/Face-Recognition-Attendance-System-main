def ans(n):
    n.sort()
    num = len(n)
    p= 0

    for i in range(num):
        e = 0
        prior= 1

        for j in range(i, num):
            e+= n[j] * prior
            prior += 1

            if e > p:
                p= e

    return p

n = list(map(int, input().split()))

res= ans(n)
if(res>0):
    print(res, end="")
else:
    print(0, end="")