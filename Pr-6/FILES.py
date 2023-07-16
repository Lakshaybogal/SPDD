PROGRAM_LENGTH = []
PSUEDO_OP_LIST = ["START","ENTRY","EXTERN"]
I:int = 0
class Files:
    def __init__(self):
        self.ESD_CARD = []
        self.TXT_TABLE = []
        self.RLD_CARD = []
        self.SYMBOLS = []
        self.TXT_CARDS_COMMENTS = []
        self.ESD_CARD_DICT_SD = {}
        self.ESD_CARD_DICT_ER = {}
        self.ESD_CARD_DICT_LD = {}
        self.SD, self.ER, self.LC= 1, 2, 0