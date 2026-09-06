def rotate(matrix):
    rev_mat = zip(*matrix)
    final_mat = []

    for position in rev_mat:
        x = list(reversed(position))
        final_mat.append(x)
    return final_mat

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
