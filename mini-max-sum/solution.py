def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    arr = list(map(int, input().strip().split()))
    miniMaxSum(arr)
