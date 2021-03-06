import DNADict as DNADict
import DNADictShort as DNADictShort

inputCode = str(input("DNA Input Sequence \n"))
canCalculateBool = False
RNACode = []
proteinCode = []


def canCalculate(code):
    global canCalculateBool
    if len(code) % 3 != 0:
        print("\nSequence cannot be calculated")
        canCalculateBool = False
    else:
        print("\nSequence can be calculated")
        canCalculateBool = True


def checkStart(code):
    if "TAC" in code or "tac" in code or "AUG" in code or "aur" in code:
        print("Has Start codon")
    else:
        print("No Start Codon")


def translateRNA(code):
    global RNACode
    for x in range(0, len(code)):
        if code[x] == "A" or code[x] == "a":
            RNACode.append("U")
        elif code[x] == "T" or code[x] == "t":
            RNACode.append("A")
        elif code[x] == "C" or code[x] == "c":
            RNACode.append("G")
        elif code[x] == "G" or code[x] == "g":
            RNACode.append("C")
    return RNACode


def transcriptionProtein():
    global RNACode
    global proteinCode
    print("\nPrinting amino acid:")
    for j in range(0, len(RNACode)):
        temp = ""
        if j % 3 == 0:
            for k in range(0, 3):
                temp = temp + RNACode[j + k]
            print(DNADict.codonDict[temp], end=" ")

    print("\nPrinting amino acid in FASTA code:")
    for j in range(0, len(RNACode)):
        temp = ""
        if j % 3 == 0:
            for k in range(0, 3):
                temp = temp + RNACode[j + k]
            print(DNADictShort.codonDict[temp], end=" ")


def keepRNA():
    global RNACode
    global inputCode
    if "U" in inputCode or "u" in inputCode:
        print("\nInput is already RNA, keeping code")
        for i in range(0, len(inputCode)):
            RNACode.append(inputCode[i])
    else:
        translateRNA(inputCode)


def draw(code1, code2):
    print("+" + "#" + code1 + "-" + code2 + "#" + "+")
    print("|     |")


def main():
    global RNACode
    global canCalculateBool
    global inputCode
    canCalculate(inputCode)
    if canCalculateBool == True:
        checkStart(inputCode)
        keepRNA()
        print("\nGenerated mRNA Code: ")
        print(RNACode)
        transcriptionProtein()
        print("")
        # if canCalculateBool == True:
        #     for x in range(0, len(inputCode), 2):
        #         draw(inputCode[x], inputCode[x + 1])
    elif canCalculateBool == False:
        continueInput = input("Input cannot be translated into codons. Continue with translation into RNA? Y/n")
        if continueInput == "Y" or continueInput == "y":
            checkStart(inputCode)
            keepRNA()
            print(RNACode)


main()
