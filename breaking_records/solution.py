def breakingRecords(scores):
    # Initialize the variables with the first game's score
    min_score = max_score = scores[0]
    min_breaks = max_breaks = 0
    
    # Iterate through the scores starting from the second game
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1
    
    # Return the counts of breaks in a list
    return [max_breaks, min_breaks]

# Example usage:
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))  # Output: [2, 4]

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(scores))  # Output: [4, 0]
