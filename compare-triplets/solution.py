def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):  # Since both lists are always of length 3
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return [alice_score, bob_score]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    a = list(map(int, data[:3]))
    b = list(map(int, data[3:]))
    
    result = compareTriplets(a, b)
    print(" ".join(map(str, result)))
