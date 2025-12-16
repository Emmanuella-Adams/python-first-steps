def number_pattern(n):
    #n = int(n)
    if not isinstance(n,int):
        return "Argument must be an integer value."
        
    if n <= 0:
        return "Argument must be an integer greater than 0."

    pattern_list = []

    for i in range( 1, n + 1):
        pattern_list.append(str(i))

    return " ".join(pattern_list)

print(number_pattern(8))