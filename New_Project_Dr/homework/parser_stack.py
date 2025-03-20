def find_and_stack_bracket_positions(s, open_symbol='<', close_symbol='>'):
    open_positions = [i for i, char in enumerate(s) if char == open_symbol]
    close_positions = [i for i, char in enumerate(s) if char == close_symbol]
    
    open_stack = open_positions[::-1]  
    close_stack = close_positions[::-1]
    
    return open_stack, close_stack

def find_pairs(open_stack, close_stack):
    pairs = []
    if len(open_stack) == 0 or len(close_stack) == 0:
        return pairs
        
    elif len(open_stack) == 1:    
        open_first = open_stack[-1]
        close_first = close_stack[-1]
        if open_first > close_first:
            close_stack.pop()
            return pairs + find_pairs(open_stack, close_stack)
        else:
            pairs.append((open_stack.pop(), close_stack.pop()))
            return pairs
    else:
        open_first = open_stack[-2]
        close_first = close_stack[-1]
        if open_first > close_first:
            pairs.append((open_stack.pop(), close_stack.pop()))
            return pairs + find_pairs(open_stack, close_stack)
        else:
            open_stack.pop()
            return pairs + find_pairs(open_stack, close_stack)

def transform_pairs(s, pairs):
    cleaned_string = ' , '.join([f"{a},{b}" for a, b in pairs])
    old_sign = "<"
    new_sign = " , "
    old_sign_1 = ">"
    new_sign_1 = " , "

    char_list = list(s)

    numbers = [int(x.strip()) for x in cleaned_string.split(',')]
    for pos in numbers:
        if char_list[pos] == old_sign:
            char_list[pos] = new_sign
        elif char_list[pos] == old_sign_1:
            char_list[pos] = new_sign_1

    new_string = "".join(char_list)
    return new_string   

def process_string(s):
    open_stack, close_stack = find_and_stack_bracket_positions(s)
    pairs = find_pairs(open_stack, close_stack)
    new_s = transform_pairs(s, pairs)
    return new_s
