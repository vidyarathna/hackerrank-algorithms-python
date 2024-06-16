def staircase(n):
    for i in range(1, n + 1):
        # Print (n - i) spaces followed by i '#'
        print(' ' * (n - i) + '#' * i)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    staircase(n)
