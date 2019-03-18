def reverse_string(string_input):
    return string_input[::-1]

print(reverse_string("hello world"))

def reverse_string_2(string_input):
    new_string = []
    index = len(string_input)
    while index:
        index -= 1
        new_string.append(string_input[index])
    return ''.join(new_string)

print(reverse_string_2("hello world"))

def reverse_string_3(string_input):
    output = ''
    for c in string_input:
        output = c + output
    return output

print(reverse_string_3("hello world"))