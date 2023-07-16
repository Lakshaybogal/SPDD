import pandas as pd
class DisplayCards():
    def __init__(self, NAME_LIST_PASS, TYPES_LIST_PASS, ID_LIST_PASS, RELADD_LIST_PASS, LENGTH_PASS,REL_ADD_pass,ANS,COMMENTS):
        self.NAME_LIST_PASS = NAME_LIST_PASS
        self.TYPES_LIST_PASS = TYPES_LIST_PASS
        self.ID_LIST_PASS = ID_LIST_PASS
        self.RELADD_LIST_PASS = RELADD_LIST_PASS
        self.LENGTH_PASS = LENGTH_PASS
        self.REL_ADD_pass = REL_ADD_pass
        self.COMMENTS = COMMENTS
        self.ANS = ANS
        self.ESD_DF = pd.DataFrame()
        self.TXT_DF = pd.DataFrame()
        self.RLD_DF = pd.DataFrame()

    def CreateESDCard(self):
        dict1 = {
            "NAME": self.NAME_LIST_PASS,
            "TYPE": self.TYPES_LIST_PASS,
            "ID": self.ID_LIST_PASS,
            "Rel Add": self.RELADD_LIST_PASS,
            "LENGTH": self.LENGTH_PASS
        }

        self.ESD_DF = pd.DataFrame(dict1)

    def CreateTXTCard(self):
        dict2 = {
            "Rel Add": self.REL_ADD_pass,
            "Contents": self.ANS,
            "Comments": self.COMMENTS
        }

        self.TXT_DF = pd.DataFrame(dict2)

    def CreateRLDCard(self,ID_LISTS,FLAGS,ADD_REL):
        if len(ADD_REL) != len(ID_LISTS):
            ADD_REL.append(ADD_REL[-1])
        dict3 = {
            "ESD Id":ID_LISTS,
            "FLAG":FLAGS,
            "LENGTH":[4 for i in range(len(FLAGS))],
            "Rel Add":ADD_REL
        }
        self.RLD_DF = pd.DataFrame(dict3)