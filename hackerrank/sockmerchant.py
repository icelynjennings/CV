from collections import Counter

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    matching = 0
    dct = Counter(ar)

    for k, v in dct.items():
        x = v // 2
        matching += x

    print(matching)
