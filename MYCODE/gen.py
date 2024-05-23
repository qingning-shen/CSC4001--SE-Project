import random

def create_var(var_names, var_types):
    select_names = []
    numnum = random.randint(0, 20)
    select = random.choices(range(0, 5), k=numnum)
    if numnum == 0:
        var_type = random.choice(var_types)
        bits = int(var_type[2:])
        val = "".join(random.choices(["0", "1"], k=bits))
        select_names.append(val)
    elif numnum != 0:
        for i in select:
            if random.randint(0, 1) == 0:
                var_type = random.choice(var_types)
                bits = int(var_type[2:])
                val = "".join(random.choices(["0", "1"], k=bits))
                select_names.append(val)
            else:
                select_names.append(var_names[i])
    return select_names

def create__exp(select_names, operators):
    if len(select_names) == 1:
        return select_names[0]
    pos = random.randint(1, len(select_names)-1)
    left = create__exp(select_names[:pos], operators)
    right = create__exp(select_names[pos:], operators)
    bop = random.choice(operators)
    add_not = random.random() < 0.2
    expression = ""
    if add_not:
        expression += '! ( '
    expression += "( " + left + " ) " + bop + " ( " + right + " )"
    if add_not:
        expression += ' )'
    return expression

f = open("./input.pig", "w")
var_types = ["bv8", "bv16", "bv32", "bv64"]
operators = ['+', '-', '&', '|']
var_num_num = random.sample(range(0, 1000), 120)
k = 0
count = 0

while k < 9:
    var_nums = random.sample(var_num_num, 5)
    var_names = []
    for i in range(0, 5):
        var_name = f"v{var_nums[i]:03d}"
        var_type = random.choice(var_types)
        bits = int(var_type[2:])
        sta = f"D {var_type} {var_name}"
        print(sta, file=f)
        var_names.append(var_name)
        count += 1
    for i in range(0, 90):
        y = random.randint(0,9)
        if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
            while True:
                select_names = create_var(var_names, var_types)
                exp = create__exp(select_names, operators)
                if len(exp) <= 1000:
                    break
            select_names = []
            x = random.randint(0, 4)
            var_name = var_names[x]
            sta = f"A {var_name} ( {exp} )"
            print(sta, file=f)
        elif y == 5:
            while True:
                select_names = create_var(var_names, var_types)
                exp = create__exp(select_names, operators)
                if len(exp) <= 1000:
                    break
            select_names = []
            s = random.randint(count+1, (k+1)*100-5)
            line = f"{s:03d}"
            sta = f"B {line} ( {exp} )"
            print(sta, file=f)
        elif y == 6 or y == 7 or y == 8 or y == 9:
            x = random.randint(0, 4)
            var_name = var_names[x]
            sta = f"O {var_name}"
            print(sta, file=f)
        count += 1
    for i in range(0, 5):
        sta = f"R {var_names[i]}"
        print(sta, file=f)
        count += 1
    k+=1


print("""D bv8 v000
D bv8 v001
A v000 ( 00000000 )
A v001 ( 00000000 )
A v001 ( ( v001 ) + ( 00000001 ) )
A v000 ( ( v000 ) + ( v001 ) )
B 904 ( ( v001 ) - ( 00001000 ) )
O v000""", file = f)

print("""D bv8 v002
A v002 ( 00000101 )
B 914 ( 00010000 )
A v002 ( ( v002 ) + ( 00000001 ) )
A v002 ( ( v000 ) + ( v002 ) )
O v002
A v002 ( ( v002 ) - ( 00000001 ) )
B 913 ( v002 )""", file = f)

print("""R v000
R v001
R v002""", file = f)

s = random.randint(0,900)
line = f"{s:03d}"
print(f"B {line} ( {'00000000'} )", file=f)

s = random.random() < 0.2
if s:
    print("B 000 ( 11111111 )", file=f)