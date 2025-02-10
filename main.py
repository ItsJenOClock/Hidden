def hidden(matrix, n):
    # Your implementation here!
    """
    Question: Input: matrix, n (int)
    Return string that contains nth character from iteration
    
    Initialize an empty string
    Iterate through the matrix with a for loop, skipping by n
    Add that char to the string
    Return string
    """
    secret_phrase = ""
    char_list = []
    for row in matrix:
        for char in row:
            char_list.append(char)

    for i in range(0, len(char_list), n):
        secret_phrase += char_list[i]

    return secret_phrase

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)

assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

