def tribonacci_sequence(start_sequence, lenght):
    '''
    this is a tribonacci sequence generator whatever that may be that was made by yours truly
    '''
    counter = 0
    first_position = 0
    third_position = 3
    #repeat as many times as the lenght is
    while counter < lenght:
        #a way to break out of the loop once the desired lenght has been reached
        if len(start_sequence) >= lenght:
            break
        #add the sum of the first three digits in the list of numbers
        added_digits = sum(start_sequence[first_position:third_position])
        #append the sum iback nto the list
        start_sequence.append(added_digits)
        #increase the watch variable and shifting index accordingly
        counter += 1
        first_position += 1
        third_position += 1
    #return the final list
    return start_sequence

print(tribonacci_sequence([0,0,1], 10))
