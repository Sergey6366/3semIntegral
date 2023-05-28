import numpy as np


# COMPUTING the integral of xsin(x) on (a, b) by cutting on n equal intervals
# xsin(x)

def f(x):
    return x * np.sin(x)


def fn(x, arrxx, n, newtcc):
    s = 0
    for i in range(n + 1):
        nn = newtcc[i]
        for j in range(i):
            nn *= (x - arrxx[j])
        s += nn
    return s


a = 0
b = 2
n1 = int(input("n (even): "))
n = n1
inres = np.sin(b) - b*np.cos(b)

k = int(input("times: "))
outres = np.empty(k)
m = 0
h1 = (b - a) / n1

# SIMPSON
while n <= n1 * 2**(k-1):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s1 = 0
    s2 = 0
    for j in range(1, int(n / 2)):  # j goes [1, n/2-1]
        s1 += f(x[2 * j])
    s1 *= 2
    s1 += f(x[0])

    for j in range(1, int(n / 2 + 1)):  # j goes [1, n/2]
        s2 += f(x[2 * j - 1])
    s2 *= 4
    s2 += f(x[n])
    outres[m] = (h * (s1 + s2)) / 3

    print(inres, outres[m], outres[m] - inres, outres[m] / inres * 100)
    m += 1
    n *= 2
if k >= 3:
    print("\n\nKOTES(SIMPSON)")
    print("\n2^p:\nExpect:", 2 ** n1)
    val = (outres[1] - outres[0]) / (outres[2] - outres[1])
    print("Real:", val)  # Real
    p = np.log2(val)
    C = (outres[1] - outres[0]) / (h1 ** p * (1 - 0.5 ** p))
    print("\nAFFECT\nRunge:", C , "\nReal:", inres - outres[0], "\np expect and real:", 3, p)
print("\n\n\n")

# GAUSS WITH 2 KNOTS
outres1 = np.empty(k)
n = n1
m = 0
while n <= n1 * 2**(k-1):
    h = (b - a) / n
    a1 = a
    b1 = a + h
    s1 = 0
    for j in range(0, n):
        s1 += h * (f(((np.sqrt(3) + 1) * a1 + (np.sqrt(3) - 1) * b1) / (2 * np.sqrt(3))) +
                           f(((np.sqrt(3) - 1) * a1 + (np.sqrt(3) + 1) * b1) / (2 * np.sqrt(3)))) / 2
        a1 += h
        b1 += h

    outres1[m] = s1
    print(inres, outres1[m], outres1[m] - inres, outres1[m] / inres * 100)
    m += 1
    n *= 2

if k >= 3:
    print("\n\nGAUSS")
    print("\n2^p:\nExpect:", 2 ** 3)
    val = (outres1[1] - outres1[0]) / (outres1[2] - outres1[1])
    print("Real:", val)  # Real
    p = np.log2(val)
    C = (outres1[1] - outres1[0]) / (h1 ** p * (1 - 0.5 ** p))
    print("\nAFFECT\nRunge:", C, "\nReal:", inres - outres1[0], "\np expect and real:", 3, p)
