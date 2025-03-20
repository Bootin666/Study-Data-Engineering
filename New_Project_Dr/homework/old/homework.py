def find_bracket_positions(s, open_symbol='<', close_symbol='>'):
    open_positions = [i for i, char in enumerate(s) if char == open_symbol]
    close_positions = [i for i, char in enumerate(s) if char == close_symbol]
    return open_positions, close_positions

def find_pairs(open_positions, close_positions):
    i, j = 0, 0
    pairs = []
    while i < (len(open_positions) - 1) and j < len(close_positions):
        if open_positions[i+1] < close_positions[j]:
            i += 1
        elif open_positions[i + 1] > close_positions[j] and close_positions[j] - open_positions[i] > 0 and i != (len(open_positions) - 1):
            pairs.append((open_positions[i], close_positions[j]))
            i += 1
            j += 1
        elif close_positions[j] - open_positions[i] < 0:
            j += 1

    while i == (len(open_positions) - 1) and j < len(close_positions):
        if open_positions[i] > close_positions[j]:
            j += 1
        elif open_positions[i] < close_positions[j]:
            pairs.append((open_positions[i], close_positions[j]))
            break

    return pairs

def transform_pairs(s, pairs):
    cleaned_string = ', '.join([f"{a},{b}" for a, b in pairs])
    old_sign = "<"
    new_sign = ", "
    old_sign_1 = ">"
    new_sign_1 = ","

    char_list = list(s)

    numbers = [int(x.strip()) for x in cleaned_string.split(',')]
    for pos in numbers:
        if char_list[pos] == old_sign:
            char_list[pos] = new_sign
        elif char_list[pos] == old_sign_1:
            char_list[pos] = new_sign_1

    new_string = "".join(char_list)
    print(new_string)
    return new_string   

def process_string(s):
    open_positions, close_positions = find_bracket_positions(s)  
    pairs = find_pairs(open_positions, close_positions)  
    return transform_pairs(s, pairs)  

s = "(x<2 <and> y<4) <<Or>> (Z>5<and><<N>5)"
s = process_string(s)  