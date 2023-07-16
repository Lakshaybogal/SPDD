import re

class Cards:
    def __init__(self, PROGRAM_LENGTH, SYMBOLS):
        self.SYMBOLS = SYMBOLS
        self.NAME_LIST_PASS = []
        self.TYPES_LIST_PASS = []
        self.ID_LIST_PASS = []
        self.RELADD_LIST_PASS = []
        self.LENGTH_PASS = []
        self.REL_ADD_pass = []
        self.ANS = []
        self.RESULT = []
        self.COMMENTS = []
        self.RLD_CARD_SYMBOLS = []
        self.FLAGS = []
        self.ADD_REL = []
        self.ID_LISTS = []
        self.RLD_DICT = {}
        self.PROGRAM_LENGTH = PROGRAM_LENGTH
        self.ID = 2
        self.J = 0

    def ESD_CARD(self, ESD_CARD_DICT_SD, ESD_CARD_DICT_LD, ESD_CARD_DICT_ER):
        for i in ESD_CARD_DICT_SD:
            self.NAME_LIST_PASS.append(i)
            self.TYPES_LIST_PASS.append(ESD_CARD_DICT_SD[i])
            self.ID_LIST_PASS.append("01")
            self.RELADD_LIST_PASS.append("00")
            self.LENGTH_PASS.append(self.PROGRAM_LENGTH)

        for i in ESD_CARD_DICT_LD:
            FLAG = 0
            self.NAME_LIST_PASS.append(i)
            self.TYPES_LIST_PASS.append(ESD_CARD_DICT_LD[i])
            FLAG2 = 0
            self.ID_LIST_PASS.append("--")
            for j in range(len(self.SYMBOLS)):
                if i in self.SYMBOLS[j]:
                    FLAG = 1
                    self.RELADD_LIST_PASS.append(str(self.SYMBOLS[j][0]))
            if not(FLAG):
                self.RELADD_LIST_PASS.append("--")
            self.LENGTH_PASS.append("--")
        for i in ESD_CARD_DICT_ER:
            self.NAME_LIST_PASS.append(i)
            self.TYPES_LIST_PASS.append(ESD_CARD_DICT_ER[i])
            self.ID_LIST_PASS.append("0" + str(self.ID))
            self.RLD_DICT[i] = "0" + str(self.ID)
            self.ID += 1
            self.RELADD_LIST_PASS.append("00")
            self.LENGTH_PASS.append("--")

    def TXT_CARD(self,TXT_CARDS_COMMENTS):
        for i in range(len(TXT_CARDS_COMMENTS)):
            self.REL_ADD_pass.append(f"{i * 4} - {(i + 1) * 4 - 1}")
        for txt in TXT_CARDS_COMMENTS:
            x = re.findall("[+]|-", txt)
            if len(x):
                idx = re.search("[(]", txt).start()
                new_txt = txt[idx + 1:len(txt) - 1]
                r1 = re.search("[-]", new_txt)
                r2 = re.search("[+]", new_txt)
                result = re.split("[+]|[-]", new_txt)
                present = 0
                symbol = ""
                number = '"'
                # evaluation = 0
                self.RESULT.append(result)
                # replace Symbols with their values and apply eval() function
                for sym in self.SYMBOLS:
                    for _ in result:
                        if _ in sym:
                            new_txt = new_txt.replace(_, str(sym[0]))
                        else:
                            # new_txt = new_txt.replace(_,"0")
                            try:
                                num = int(_)
                            except:
                                new_txt = new_txt.replace(_, "0")
                self.ANS.append([eval(new_txt)])
                self.COMMENTS.append([new_txt])

            else:
                idx = re.search("[(]", txt).start()
                new_txt = txt[idx + 1:len(txt) - 1]
                self.RESULT.append([new_txt])
                present = 0
                value = 0
                for sym in self.SYMBOLS:
                    if new_txt in sym:
                        # ANS.append(sym[0])
                        present = 1
                        value = int(sym[0])
                        break
                self.ANS.append([str(value)])
                self.COMMENTS.append([str(value)])

    def isOperator(self,sign: str) -> bool:
        if sign == '+' or sign == '-':
            return True
        return False

    def RLD_CARD(self,TXT_CARDS_COMMENTS,ESD_CARD_DICT_ER,ESD_CARD_DICT_SD,ESD_CARD_DICT_LD,TXT_DF):
        WANT = []
        traverler = 0
        TEMPORARY = lambda x: x[2:len(x) - 1]
        # print(PASS_CARDS[0].RESULT)
        VAR_TEMP = [TEMPORARY(i) for i in TXT_CARDS_COMMENTS]
        for _ in self.RESULT:
            sdlist = []
            ldlist = []
            for k in _:
                if k in ESD_CARD_DICT_ER:
                    WANT.append(_)
                    break
                elif k in ESD_CARD_DICT_SD:
                    sdlist.append(k)
                elif k in ESD_CARD_DICT_LD:
                    ldlist.append(k)
            if len(sdlist) >= 1 and len(ldlist) == 0:
                WANT.append(sdlist)
            elif len(ldlist) >= 1 and len(sdlist) == 0:
                WANT.append(ldlist)
        WANT = list(filter(lambda x: x in self.RESULT, WANT))
        INDICES = {}
        relADDRESSES = []
        rldContent = []
        NUMBERS = [str(i) for i in range(1, 1001)]
        for k in WANT:
            idx = self.RESULT.index(k)
            INDICES[idx] = k
            relADDRESSES.append(TXT_DF.iloc[idx]["Rel Add"])
            rldContent.append(TXT_DF.iloc[idx]["Contents"])
        ALL_SIGNS = []
        FLAGS_DICT = []
        for var in VAR_TEMP:
            signTraveler = 0
            sign = []
            sign.append('+')
            # print(var)
            for i in range(len(var)):
                if self.isOperator(var[i]) and i + 1 < len(var) and var[i + 1] not in NUMBERS:
                    sign.append(var[i])
            ALL_SIGNS.append(sign)
        for i, j in enumerate(INDICES.values()):
            d = {}
            for k in range(len(j)):
                if j[k] not in NUMBERS:
                    try:
                        d[j[k]] = ALL_SIGNS[i][k]
                    except:
                        pass

            FLAGS_DICT.append(d)


        temp_dict = {}
        for i, j in INDICES.items():
            for _ in j:
                if _ not in NUMBERS and _ in temp_dict:
                    break
                elif _ not in NUMBERS and _ not in temp_dict:
                    try:
                        temp_dict[_] = relADDRESSES[self.J]
                        self.J += 1
                    except:
                        pass

        for i in FLAGS_DICT:
            for j in i:
                if j in ESD_CARD_DICT_ER:
                    self.ID_LISTS.append(self.RLD_DICT[j])
                elif j in ESD_CARD_DICT_SD:
                    self.ID_LISTS.append("01")
                elif j in ESD_CARD_DICT_LD:
                    self.ID_LISTS.append("01")
                self.FLAGS.append(i[j])
                try:
                    self.ADD_REL.append([temp_dict[j]])
                except:
                    pass