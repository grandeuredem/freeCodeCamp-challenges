def tribonacci_sequence(start_sequence, lenght):
    '''
    this is a tribonacci sequence generator whatever that may be that was made by yours truly
    '''
    first_position = 0
    third_position = 3
    #repeat as many times as the lenght is
    while len(start_sequence) < lenght:
        #add  and append the sum of the first three digits in the list of numbers
        start_sequence.append(sum(start_sequence[first_position:third_position]))
        #increase the shifting index accordingly
        first_position += 1
        third_position += 1
    return start_sequence

print(tribonacci_sequence([0,0,1], 10))
