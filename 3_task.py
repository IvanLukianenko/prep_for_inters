#3. Дан массив A - набор натуральных чисел. 
# Нужно найти два таких индекса i, j, что значение min(A[i], A[j]) * |i - j|  максимально из возможных. 
# O(N)

def solve(M):
    l = 0
    r = len(M) - 1
    max_ = -1e12
    actual = 0
    while(l < r):
        if M[l] < M[r]:
            actual = M[l]*(r-l)
            if max_ < max(max_, actual):
                a = l
                b = r
                max_ = max(max_, actual)
            l+=1
        else:
            actual = M[r]*(r-l)
            if max_ < max(max_, actual):
                a = l
                b = r
                max_ = max(max_, actual)
            r-=1

    return a, b


if __name__ == "__main__":
    M = [1, 3, 4, 1000, 1000, 5]
    print(solve(M))