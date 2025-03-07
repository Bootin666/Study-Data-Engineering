def find_bracket_pairs(s): 
    less_than_positions = []
    greater_than_positions = []

    for i, char in enumerate(s):
        if char == '<': 
            less_than_positions.append(i)
        elif char == '>': 
            greater_than_positions.append(i)

    print("Positions of '<':", less_than_positions)
    print("Positions of '>':", greater_than_positions)

    i, j = 0, 0
    pairs = []

    while i < (len(less_than_positions) - 1) and j < len(greater_than_positions):
        if less_than_positions[i + 1] - less_than_positions[i] < greater_than_positions[j] - less_than_positions[i]:
            i += 1
        elif less_than_positions[i + 1] - less_than_positions[i] > greater_than_positions[j] - less_than_positions[i] and greater_than_positions[j] - less_than_positions[i] > 0 and i != (len(less_than_positions) - 1):
            pairs.append((less_than_positions[i], greater_than_positions[j]))
            i += 1
            j += 1
        elif greater_than_positions[j] - less_than_positions[i] < 0:
            j += 1

    while i == (len(less_than_positions) - 1) and j < len(greater_than_positions):
        if less_than_positions[i] > greater_than_positions[j]:
            j += 1
        elif less_than_positions[i] < greater_than_positions[j]:
            pairs.append((less_than_positions[i], greater_than_positions[j]))
            break

    return pairs

s = "(x<3 <and> y<4) <<Or>> (Z>5<and><<N>5)"
pairs = find_bracket_pairs(s)
print("Pairs:", pairs)
cleaned_string = ', '.join([f"{a},{b}" for a, b in pairs])
old_sign = "<"
new_sign = ", "
old_sign_1 = ">"
new_sign_1 = ","

char_list = list(s)

numbers = [int(x.strip()) for x in cleaned_string.split(',')]
for pos in numbers	:
    if char_list[pos] == old_sign:
        char_list[pos] = new_sign
    elif char_list[pos] == old_sign_1:
        char_list[pos] = new_sign_1

new_string = "".join(char_list)

print(new_string)