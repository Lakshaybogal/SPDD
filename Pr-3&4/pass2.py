from pass1 import MOT

base_table = {}
with open('base_table.txt', 'r') as file:
    for line in file:
        if ';' in line or line.count("=") >= 5:
            continue
        register, constant = list(map(str.strip, line.strip().split('\t')))
        base_table[register] = int(constant)

literal_table = {}
with open('literal_table.txt', 'r') as file:
    for line in file:
        if ';' in line or line.count("=") >= 5:
            continue
        literal, value, length = list(map(str.strip, line.strip().split('\t')))
        literal_table[literal] = (value, length)

symbol_table = {}
with open('symbol_table.txt', 'r') as file:
    for line in file:
        if ';' in line or line.count("=") >= 5:
            continue
        symbol, value = list(map(str.strip, line.strip().split('\t')))
        symbol_table[symbol] = value

machine_code = []
base_register = 0


def insert_machine_code(lc, opcode, operands):
    machine_code.append({
        'lc': lc,
        'opcode': opcode,
        'operands': operands,
    })


def convert_to_machine_code(lc: str, opcode: str, operands: str):
    global base_register, machine_code
    if opcode == 'USING':
        base_register = int(operands.split(',')[1])
    elif opcode in ['SR', 'AR']:
        insert_machine_code(lc, opcode, operands)
    elif opcode in ['DC', 'DS']:
        insert_machine_code(lc, operands, '')
    elif opcode in ['L', 'A', 'ST', 'C']:
        rx, label = operands.split(',')
        if label in symbol_table:
            insert_machine_code(
                lc, opcode, f'{rx}, {int(symbol_table[label]) - int(base_table[str(base_register)])}({0}, {base_register})')
        elif label in literal_table:
            insert_machine_code(
                lc, opcode, f'{rx}, {int(literal_table[label][0]) - int(base_table[str(base_register)])}({0}, {base_register})')
        else:
            insert_machine_code(
                lc, opcode, f'{rx}, {label}({0}, {base_register})')
    elif opcode == 'END':
        insert_machine_code(lc, opcode, "")


with open('lc_table.txt', 'r') as file:
    for line in file:
        if ';' in line or line.count("=") >= 5 or line.find("START") != -1:
            continue
        line_data = list(map(str.strip, line.strip().split('\t')))
        line_number, lc, opcode = line_data[:3]
        opdata = [x for x in opcode.split(" ") if x != ""]
        if opdata[0] in MOT:
            opcode = opdata[0]
            opdata.pop(0)
        elif len(opdata) > 1 and opdata[1] in MOT:
            opcode = opdata[1]
        else:
            opcode = opdata[0]
        operands = " ".join(opdata)
        convert_to_machine_code(lc, opcode, operands)


with open('machine_code.txt', 'w') as file:
    file.write('; Machine Code\n')
    file.write('; Location Counter\tInstruction\n')
    file.write('=====================\n')
    for line in machine_code:
        file.write(
            f'{line["lc"].ljust(4)}\t{line["opcode"]}\t{line["operands"]}\n')
    print("Pass 2 completed successfully")
