def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum(1 for apple in apples if s <= a + apple <= t)
    orange_count = sum(1 for orange in oranges if s <= b + orange <= t)
    
    print(apple_count)
    print(orange_count)

# Example usage:
if __name__ == '__main__':
    st = input().strip().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().strip().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().strip().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().strip().split()))
    oranges = list(map(int, input().strip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
