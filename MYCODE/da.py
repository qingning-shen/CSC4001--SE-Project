def create_set(statements):
    ins, outs = [], []
    problem_lines = set()
    for i in range(len(statements)):
        ins.append(set([f"v{i:03d}" for i in range(1000)]))
        outs.append(None)
    ins[0] = set()
    changed = True
    for i in range(len(statements)):
        changed = False
        for j in range(len(statements)):
            outs[j] = ins[j].copy()
            if statements[j][1] == 'D':
                outs[j].add(statements[j][2])
            elif statements[j][1] == 'R':
                if statements[j][2] in ins[j]:
                    outs[j].remove(statements[j][2])
                else:
                    problem_lines.add(statements[j][0])
            elif statements[j][1] == 'O':
                if statements[j][2] not in ins[j]:
                    problem_lines.add(statements[j][0])
            elif statements[j][1] == 'B':
                if any([v not in ins[j] for v in statements[j][2][1:]]):
                    problem_lines.add(statements[j][0])
            elif statements[j][1] == 'A':
                if any([v not in ins[j] for v in statements[j][2]]):
                    problem_lines.add(statements[j][0])
            if j < len(statements) - 1:
                new_ins = ins[j + 1].copy()
                ins[j + 1] &= outs[j]
                if ins[j + 1] != new_ins:
                    changed = True
            if statements[j][1] == 'B':
                v = int(statements[j][2][0])
                new_ins = ins[v].copy()
                ins[v] &= outs[j]
                if ins[v] != new_ins:
                    changed = True
            # print(f"j={j}, ins={ins[j]}, outs={outs[j]}, problem_lines={problem_lines}")
        if not changed:
            break
    return problem_lines

lines = []
while True:
	try:
		i = input()
		assert i
	except:
		break
	lines.append(i)

statements = []
for line_number, line in enumerate(lines):
    parts = line.split()
    type = parts[0]
    variables = parts[1:]
    if type == 'D':
        statements.append((line_number, type, variables[1]))
    elif type == 'R' or type == 'O':
        statements.append((line_number, type, variables[0]))
    elif type == 'A':
        tokens = []
        for variable in variables:
            if variable.startswith("v"):
                tokens.append(variable)
        statements.append((line_number, type, tokens))
    elif type == 'B':
        tokens = []
        for variable in variables:
            if variable.startswith("v"):
                tokens.append(variable)
        statements.append((line_number, type, [variables[0]] + tokens))
problem_lines = create_set(statements)
print(len(problem_lines))