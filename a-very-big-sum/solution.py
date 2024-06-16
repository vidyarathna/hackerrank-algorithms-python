def aVeryBigSum(ar):
    return sum(ar)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    ar = list(map(int, data[1:n+1]))
    
    result = aVeryBigSum(ar)
    print(result)
