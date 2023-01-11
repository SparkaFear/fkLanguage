import random

mainfile = open("main.fake","r")

#syntax
syntaxlist = []
prsyntax = "+"
syntaxlist.append(prsyntax)
varsyntax = "var"
syntaxlist.append(varsyntax)

#executors
prexecute = "pr("
randexecute = "rand("

#storage
variables = []
variablevalues = []

#funcs
def checkinary(ary,arg):
    found = False
    for i in ary:
        if i == arg:
            found = True
            break
    return found
    
def findinary(ary,arg):
    item = None
    for i in ary:
        if i == arg:
            item = i
            break
    return item

with mainfile as f:
    lines = [line for line in f]

for line in lines:
    if prexecute in line:
        prline = str.split(line,"(")
        if prline[1][0] == prsyntax:
            spl = str.split(prline[1],prsyntax)
            print(spl[1])
        else:
            canthrough = False
            curVariable = None
            for var in variables:
                if var == str.split(prline[1],")")[0]:
                    canthrough = True
                    curVariable = var
                    break
            if canthrough == True:
                print(variablevalues[variables.index(curVariable)])
            else:
                print("Invalid print function, got " + prline[1][0] + " instead of " + prsyntax + ".")
    if varsyntax in line:
        linesplit = str.split(line," ")
        variablename = linesplit[1]
        variables.append(variablename)
        variablevalue = "temp"
        for i in linesplit:
            if linesplit.index(i) >= 3:
                if variablevalue == "temp":
                    variablevalue = i
                else:
                    variablevalue = variablevalue + " " + i
                        
        
        if not "\n" in variablevalue:
            variablevalues.append(variablevalue)
        else:
            variablevalues.append(variablevalue.replace("\n",""))
    if randexecute in line:
        print(variables)
        prline = str.split(line,"(")
        spl = str.split(prline[1],",")
        for i in spl:
            if ")\n" in i:
                i.removeprefix(")\n")

        if len(spl) == 2:
            if not checkinary(variables,spl[0].replace(")\n","")) == True and not checkinary(variables,spl[1].replace(")\n","")) == True:
                print(random.randint(int(spl[0].replace(")\n","")),int(spl[1].replace(")",""))))
            else:
                if checkinary(variables,spl[0].replace(")\n","")) and not checkinary(variables,spl[1].replace(")\n","")):
                    print(random.randint(int(variablevalues[variables.index(findinary(variables,spl[0].replace(")\n","")))]),int(spl[1].replace(")\n",""))))
                elif checkinary(variables,spl[1].replace(")\n","")) and not checkinary(variables,spl[0].replace(")\n","")) :
                    print(random.randint(int(spl[0].replace(")\n","")),int(variablevalues[variables.index(findinary(variables,spl[1].replace(")\n","")))])))
                else:
                    print(random.randint(int(variablevalues[variables.index(findinary(variables,spl[0].replace(")\n","")))]),int(variablevalues[variables.index(findinary(variables,spl[1].replace(")\n","")))])))
                    
                    
        else:
            print("Need arguments, got " + str(len(spl)))


            

        
