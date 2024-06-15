def simpleArraySum(ar):
    return sum(ar)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    ar = list(map(int, data[1:1+n]))
    
    result = simpleArraySum(ar)
    print(result)
