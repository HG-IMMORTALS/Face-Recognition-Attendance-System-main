import numpy


def toggle(n):
    return ''.join(['1' if bit == '0' else '0' for bit in n])


def gtt_max(a, m):
    max_v = max(a)
    max_i = a.index(max_v)
    l = max(0, max_i - m)
    r = min(len(a) - 1, max_i + m)

    # Use slicing instead of list concatenation
    s = a[l:r + 1]
    a = [y for y in a if y not in s]

    return sum(s), a


a = list(map(int, input().split()))

# Convert input directly to integers
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
m = int(input())

s1, s2 = 0, 0
while a:
    s3, a = gtt_max(a, m)
    s1 += s3

    if not a:
        break

    s4, a = gtt_max(a, m)
    s2 += s4

if s1 > s2:
    A1 = toggle(bin(A1)[2:])  # Use bin() function for binary conversion
    B2 = toggle(bin(B2)[2:])
else:
    A2 = toggle(bin(A2)[2:])
    B1 = toggle(bin(B1)[2:])

xorr1 = A1 ^ B1
xorr2 = A2 ^ B2

if xorr1 > xorr2:
    print("Rahul", end="")
elif xorr2 > xorr1:
    print("Rupesh", end="")
else:
    print("both", end="")
