import pandas as pd

MDT = []
MNT = []
MNT_NAME = []
ALA = []
REAL_ARGS = []
REAL_ARGS1 = []
ALA_ARGS_DICT = {}
mdlp = 1
mntp = 1

with open("input.txt", "r") as file:
    line = file.readlines()
    for i in range(len(line)):
        if i != 0 and line[i - 1] == "MACRO\n":
            MNT.append([mntp, [mdlp, line[i].split()[0]]])
            MNT_NAME.append(line[i].split()[0])
            mntp += 1
            args = line[i].split()
            args_list = args[1].split(',')
            for j in range(len(args_list)):
                ALA.append([args_list[j], '#' + str(j + 1)])
                ALA_ARGS_DICT[args_list[j]] = '#' + str(j + 1)
            k = i
            while line[k] != "MEND\n":
                MDT.append([mdlp, line[k][:len(line[k]) - 1]])
                mdlp += 1
                k += 1
            MDT.append([mdlp, "MEND"])
            mdlp += 1
        try:
            if line[i].split()[0] == "USING":
                while line[i] != "END":
                    t = line[i].split()
                    for j in MNT:
                        if t[0] in j[1]:
                            REAL_ARGS1.append(t[1].split(','))
                            REAL_ARGS.extend(t[1].split(','))
                    i += 1
        except:
            pass

diff = len(ALA) - len(REAL_ARGS)
REAL_ARGS.extend(['-'] * diff)

i = 1
for i in range(1, len(MDT)):
    next = MDT[i][1].split()
    try:
        next_again = next[1].split(',')
        for j in next_again:
            if next[0] in MNT_NAME or next_again[1] not in ALA_ARGS_DICT:
                continue
            MDT[i][1] = MDT[i][1].replace(
                next_again[1], ALA_ARGS_DICT[next_again[1]])
    except:
        pass

REAL_ARGS_LIST = []
for i in range(len(MNT)):
    d = {MNT[i][1][1]: REAL_ARGS1[i]}
    REAL_ARGS_LIST.append(d)

dict1 = {
    "INDEX": [MDT[i][0] for i in range(len(MDT))],
    "INSTRUCTION": [MDT[i][1] for i in range(len(MDT))]
}

dict2 = {
    "INDEX": [i[0] for i in MNT],
    "NAME": [i[1][1] for i in MNT],
    "MDT INDEX": [i[1][0] for i in MNT]
}

dict3 = {
    "DUMMY ARG": [i[0] for i in ALA],
    "INDEX MARKER": [i[1] for i in ALA],
    "ACTUAL ARGS": ['-' for i in range(len(ALA))]
}

MDT_DF = pd.DataFrame(dict1)
MNT_DF = pd.DataFrame(dict2)
ALA_DF = pd.DataFrame(dict3)

print("\n\n----- MACRO NAME TABLE -----")
print(MNT_DF)
print("\n\n----- MACRO DEFINITION TABLE -----")
print(MDT_DF)
print("\n\n----- ALA TABLE PASS I -----")
print(ALA_DF)

# PASS 2
dict4 = {
    "DUMMY ARG": [i[0] for i in ALA],
    "INDEX MARKER": [i[1] for i in ALA],
    "ACTUAL ARGS": [i for i in REAL_ARGS]
}

PASS2_ALA = pd.DataFrame(dict4)
print()
print("\n\n----- ALA TABLE PASS II -----")
print(PASS2_ALA)
