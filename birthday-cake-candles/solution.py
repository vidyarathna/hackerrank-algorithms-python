def birthdayCakeCandles(candles):
    max_height = max(candles)  # Find the maximum height among candles
    count = candles.count(max_height)  # Count how many times max_height appears
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])  # First line is the size of the array (not actually needed to use)
    candles = list(map(int, data[1:]))  # Second line are the heights of the candles
    result = birthdayCakeCandles(candles)
    print(result)
