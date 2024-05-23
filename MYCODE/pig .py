def bit_not(origin_string):
    result = ""
    for origin_bit in origin_string:
        if origin_bit == '1':
            result += '0'
        else:
            result += '1'
    return result

def bit_and(origin_string1, origin_string2):
    max_length = max(len(origin_string1), len(origin_string2))
    result = ""
    origin_string1 = origin_string1.zfill(max_length)
    origin_string2 = origin_string2.zfill(max_length)
    for i in range(max_length):
        if origin_string1[i] == '1' and origin_string2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result

def bit_or(origin_string1, origin_string2):
    max_length = max(len(origin_string1), len(origin_string2))
    result = ""
    origin_string1 = origin_string1.zfill(max_length)
    origin_string2 = origin_string2.zfill(max_length)
    for i in range(max_length):
        if origin_string1[i] == '0' and origin_string2[i] == '0':
            result += '0'
        else:
            result += '1'
    return result

def bit_add(origin_string1, origin_string2):
    max_length = max(len(origin_string1), len(origin_string2))
    result = ""
    carry = 0
    origin_string1 = origin_string1.zfill(max_length)
    origin_string2 = origin_string2.zfill(max_length)
    for i in range(max_length-1, -1, -1):
        bit_sum = int(origin_string1[i])+int(origin_string2[i])+carry
        result = str(bit_sum%2)+result
        carry = bit_sum // 2
    return result

def bit_sub(origin_string1, origin_string2):
    max_length = max(len(origin_string1), len(origin_string2))
    result = (int(origin_string1, 2) - int(origin_string2, 2)) % (2**max_length)
    result = f"{result:0{max_length}b}"
    return result

def LP_RP(expression):
    global variables
    if len(expression) == 1:
        if expression[0].startswith('v'):
            return variables[expression[0]]
        else:
            return expression[0]
    depth = 0
    for i in range(len(expression)-1, -1, -1):
        if expression[i] == ')':
            depth += 1
        elif expression[i] == '(':
            depth -= 1
        elif depth == 0 and (expression[i] in {'+' , '-' , '&' , '|', '!'}):
            return i

def find_expression(expression):
    if not expression:
        return None
    expression = expression[1:-1]
    pos = LP_RP(expression)
    if type(pos) == str:
        return pos
    first = find_expression(expression[0:pos])
    second = find_expression(expression[pos+1:])
    operator = expression[pos]
    if operator == '+':
        return bit_add(first, second)
    elif operator == '-':
        return bit_sub(first, second)
    elif operator == '&':
        return bit_and(first, second)
    elif operator == '|':
        return bit_or(first, second)
    elif operator == '!':
        return bit_not(second)

def des_lines(line, fout):
    global num_line, variables
    tokens = line.split()
    req = tokens[0]
    if req == 'D':
        commands, types, vars = tokens
        variables[vars] = '0'*int(types[2:])
    elif req == 'A':
        commands, vars, *expression = tokens
        value = find_expression(expression)
        length = len(variables[vars])
        variables[vars] = value[-length:].zfill(length)
    elif req == 'B':
        commands, positions, *expression = tokens
        value = find_expression(expression)
        if value != '0'*len(value):
            num_line = int(positions) - 1
    elif req == 'O':
        commands, vars = tokens
        print(variables[vars], file=fout)
    elif req == 'R':
        commands, vars = tokens
        if vars in variables:
            del variables[vars]

def codes(fin, fout):
    global num_line
    lines = fin.readlines()
    for _ in range(5000):
        if num_line >= len(lines):
            break
        des_lines(lines[num_line], fout)
        num_line += 1
    else:
        print("too-many-lines", file=fout)

variables = {}
num_line = 0

with open("./input.pig", "r") as fin, open("./1.out", "w") as fout:
    codes(fin, fout)