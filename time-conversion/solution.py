def timeConversion(s):
    period = s[-2:]  # Get AM or PM
    hour = int(s[:2])  # Get hour part as integer
    minute_second = s[2:-2]  # Get minute and second part
    
    if period == 'AM':
        if hour == 12:
            hour = 0  # Midnight case
    else:
        if hour != 12:
            hour += 12  # PM other than 12:00 PM
    
    return '{:02}:{:02}:{:02}'.format(hour, *map(int, minute_second.split(':')))

# Example usage:
if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)  # Output: 19:05:45
