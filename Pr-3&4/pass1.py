def write_literal_table(literal_table):
    with open('literal_table.txt', 'w') as literal_file:
        literal_file.write('; Literal Table\n')
        literal_file.write('; Literal\tValue\tLength\n')
        literal_file.write('=====================\n')
        for literal, data in literal_table.items():
            lc = data['LC']
            length = data['Length']
            literal_file.write(f'{literal.ljust(10)}\t{lc}\t{length}\n')


def write_symbol_table(symbol_table):
    with open('symbol_table.txt', 'w') as symbol_file:
        symbol_file.write('; Symbol Table\n')
        symbol_file.write('; Symbol\tValue\n')
        symbol_file.write('=====================\n')
        for symbol, data in symbol_table.items():
            value = data['Value']
            symbol_file.write(f'{symbol.ljust(10)}\t{value}\n')


def write_lc_table(lc_table):
    with open('lc_table.txt', 'w') as lc_file:
        lc_file.write('; Location Counter Table\n')
        lc_file.write('; Line\tLC\n')
        lc_file.write('=====================\n')
        for i, (lc, line) in enumerate(lc_table):
            lc_file.write(
                f'{str(i+1).ljust(5)}\t{str(lc).ljust(10)}\t{line}\n')


def write_base_table(base_table):
    with open('base_table.txt', 'w') as base_file:
        base_file.write('; Base Table\n')
        base_file.write('; Register\tConstant\n')
        base_file.write('=====================\n')
        for register, data in base_table.items():
            constant = data['Constant']
            base_file.write(f'{register.ljust(10)}\t{constant}\n')


def pass1(filename):
    with open('question.txt', 'r') as file:
        lines = file.readlines()

    literal_table = {}
    symbol_table = {}
    lc_table = []
    base_table = {}

    LC = 0
    base_register = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):
            continue

        lc_table.append((LC, line))
        tokens = line.split()

        if len(tokens) > 1 and tokens[1] == 'EQU':
            symbol = tokens[0]
            value = tokens[2]
            if value == '*':
                value = LC
            symbol_table[symbol] = {'Value': value}

        for i in range(1, len(tokens)):
            if '=' in tokens[i]:
                literal = tokens[i].split('=')[1]
                literal_table['=' + literal] = {'Length': 4}

        if tokens[0] == 'USING':
            constant_value, base_register = tokens[1].split(',')
            if constant_value == '*':
                constant_value = LC
            base_table[base_register] = {'Constant': constant_value}

        if tokens[0] in MOT:
            opcode = tokens[0]
            opcode_size = MOT[opcode]
            LC += opcode_size

        if len(tokens) > 1 and tokens[1] in MOT:
            opcode = tokens[1]
            opcode_size = MOT[opcode]
            symbol = tokens[0]
            value = LC
            symbol_table[symbol] = {'Value': value}
            LC += opcode_size

    if LC != 8:
        LC += 8 - LC % 8

    for i in literal_table.keys():
        literal_table[i]["LC"] = LC
        LC += 4

    write_literal_table(literal_table)
    write_symbol_table(symbol_table)
    write_lc_table(lc_table)
    write_base_table(base_table)
    print("Pass 1 completed successfully.")


MOT = {
    'LDA': 4,
    'STA': 4,
    'ADD': 4,
    'HLT': 4,
    'DC': 4,
    'DS': 4,
    'LA': 4,
    'SR': 2,
    'L': 4,
    'ST': 4,
    'AR': 2,
    'A': 4,
    'C': 4,
    'BNE': 4,
    'USING': 0,
}

assembly_file = 'question.txt'
pass1(assembly_file)
