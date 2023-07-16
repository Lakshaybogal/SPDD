from FILES import *
from CardsCreation import Cards
from CardsMaker import *
from FILES import Files
import pandas as pd
TOTAL_PASSES = []
PASSES = 0

with open("input.txt","r") as file:
    lines = file.readlines()
    for i in lines:
        instr = i.split()
        if "END" in instr:
            PASSES += 1

for _ in range(PASSES):
    p = Files()
    TOTAL_PASSES.append(p)

with open("input.txt", 'r') as file:
    lines = file.readlines()
    for i in lines:
        instr = i.split()
        if "START" in instr:
            LC = 0
            TOTAL_PASSES[I].ESD_CARD.extend(instr[0])
            TOTAL_PASSES[I].ESD_CARD_DICT_SD[instr[0]] = "SD"

        elif "ENTRY" in instr or "EXTERN" in instr:
            TOTAL_PASSES[I].ESD_CARD.extend(instr[1].split(','))
            if "ENTRY" in instr:
                tp = instr[1].split(',')
                for j in tp:
                    TOTAL_PASSES[I].ESD_CARD_DICT_LD[j] = "LD"
            else:
                tp = instr[1].split(',')
                for j in tp:
                    TOTAL_PASSES[I].ESD_CARD_DICT_ER[j] = "ER"
        elif "DC" in instr:
            idx = instr.index("DC")
            if idx == 0:
                length = len(instr[1].split(','))
                TOTAL_PASSES[I].TXT_CARDS_COMMENTS.extend(instr[1].split(','))
                LC += 4*length
            elif idx == 1:
                TOTAL_PASSES[I].SYMBOLS.append([LC,instr[0]])
                length = len(instr[2].split(','))
                TOTAL_PASSES[I].TXT_CARDS_COMMENTS.extend(instr[2].split(','))
                LC += 4*length
        elif "END" in instr:
            I += 1
            PROGRAM_LENGTH.append({LC: "END"})


PASS_CARDS = []
DISPLAY_CARDS = []
RLD_STATUS = []
for i in range(PASSES):
    pass_cards = Cards(PROGRAM_LENGTH[i].keys(),TOTAL_PASSES[i].SYMBOLS)
    pass_cards.ESD_CARD(TOTAL_PASSES[i].ESD_CARD_DICT_SD,TOTAL_PASSES[i].ESD_CARD_DICT_LD,TOTAL_PASSES[i].ESD_CARD_DICT_ER)
    pass_cards.TXT_CARD(TOTAL_PASSES[i].TXT_CARDS_COMMENTS)
    cards = DisplayCards(pass_cards.NAME_LIST_PASS,pass_cards.TYPES_LIST_PASS,pass_cards.ID_LIST_PASS,pass_cards.RELADD_LIST_PASS,pass_cards.LENGTH_PASS,pass_cards.REL_ADD_pass,pass_cards.ANS,pass_cards.COMMENTS)
    cards.CreateESDCard()
    cards.CreateTXTCard()
    pass_cards.RLD_CARD(TOTAL_PASSES[i].TXT_CARDS_COMMENTS, TOTAL_PASSES[i].ESD_CARD_DICT_ER,
                        TOTAL_PASSES[i].ESD_CARD_DICT_SD, TOTAL_PASSES[i].ESD_CARD_DICT_LD, cards.TXT_DF)
    try:
        cards.CreateRLDCard(pass_cards.ID_LISTS,pass_cards.FLAGS,pass_cards.ADD_REL)
        RLD_STATUS.append(0)
    except:
        RLD_STATUS.append(1)
    cards.CreateRLDCard(pass_cards.ID_LISTS,pass_cards.FLAGS,pass_cards.ADD_REL)
    # print(pass_cards.ID_LISTS)
    # print(pass_cards.FLAGS)
    # print(pass_cards.ADD_REL)
    PASS_CARDS.append(pass_cards)
    DISPLAY_CARDS.append(cards)

for i in range(PASSES):
    print(f"**** PASS {i+1} ****")
    print("---- ESD CARD ----")
    print(DISPLAY_CARDS[i].ESD_DF)
    print()
    print("---- TXT CARD ----")
    print(DISPLAY_CARDS[i].TXT_DF)
    print()
    if RLD_STATUS[i]:
        print("SORRY!! 😔 This Algorithm is not able to print RLD CARD for given Instructions")
    else:
        print("---- RLD CARD ----")
        print(DISPLAY_CARDS[i].RLD_DF)

        print()
    print()
