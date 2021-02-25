# 1. Даны два массива целых чисел длин M и N. 
# Проверить, что в первом массиве можно найти число a, а во втором число b так, что |a - b| < 2020. 
# O(no comments)

# Наивная реализация с линейным поиском
# Итоговая ассимптотика O(M*N)
def lin_search(M, element):
    for elem in M:
        if abs(elem - element) < 2020 :
            return True, element, elem
    return False, -1, -1

# Реализцаия с целочисленным бинарным поиском
# Итоговая ассимптотика O(N*log(len(M)))
def bin_search(M, element):
    l = 0
    r = len(M) - 1
    
    while r - l >= 1:
        m = (r+l)//2
        if abs(M[m] - element) < 2020:
            return True, element, M[m]
        if (element - M[i] >2020):
            l = m+1
        if (element - M[i] <-2020):
            r = m

    return False, -1, -1



if __name__ == '__main__':
    M = [0, 0, -3, -4, 0, -6, -7, -8, -9]
    N = [2020, 2030, 2031]
    N = sorted(N)
    M = sorted(M)
    i = 0
    M.append(10000000)
    for element in N:
        indicator, a, b = bin_search(M, element)
        if indicator == True:
            print("True")
            print(a, b)
            break
        i += 1
    if i == len(N):
        print("False")