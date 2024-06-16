def diagonalDifference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(arr)
    
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n-i-1]
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = []
    index = 1
    for i in range(n):
        arr.append(list(map(int, data[index:index+n])))
        index += n
    
    result = diagonalDifference(arr)
    print(result)
