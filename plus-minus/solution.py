def plusMinus(arr):
    n = len(arr)
    pos_count = sum(1 for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)
    
    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    plusMinus(arr)
