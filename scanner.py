import logging

from tokens import *

logging.basicConfig(filename='ADAdebug')


class Scanner:

    # constructor
    def __init__(self, testfile):
        try:
            import os
            assumedFile = os.path.realpath(__file__)
            assumedFile = assumedFile[:assumedFile.rfind('/') + 1]
            self.outputFileName = assumedFile + "output.txt"
            self.inputFileName = assumedFile + testfile
            # set up the input and output files as well as the buffered writer for writing to an output file
            # input file mut be in the same directory as the package

            self.inputFile = open(self.inputFileName, 'r')
            try:
                self.outputFile = open(self.outputFileName, 'w')
            except:
                self.outputFile = open(self.outputFileName, 'x')
                self.outputFile.close()
                self.outputFile = open(self.outputFileName, 'w')
            self.bw = open(self.outputFileName, 'w')
            self.variables = None
            self.code = ''


        except Exception as ex:
            logging.log('error', ex)

    def getTokens(self, returnTokens=None):

        tokenList = []
        try:
            # initialize Arraylist to hold tokens
            data = self.readInputFile()

            # iterate through every string
            for s in data:
                # call the lookup function which will determine the token type and return the appropriate output message
                if returnTokens is None:
                    temp = self.search(s[0])
                    tokenList.append(self.search(s[0]))
                else:
                    temp = self.searchToken(s[0])
                    temp.setRow(s[1])
                    tokenList.append(temp)
                # System.out.println(s);

            valuesToPrint = []
            print('\n'.join([f"{hold[0]}:{hold[1]}" for hold in data]))
            for t in tokenList:
                valuesToPrint.append(f"Line Number: {t[3]}\t Lexeme: {t[2]}\t Token: {t[1]}\t ID:{t[0]}")

            print('\n'.join(valuesToPrint))

            # close the output file
            self.bw.close()


        except Exception as ex:
            logging.log(1, ex)
        # print(data)

        return tokenList

    def readInputFile(self):
        # set up string for holding file contents as well as the buffered reader
        data = ""
        br = self.inputFile
        ## //used to read file line by line

        # //read file line by line

        for line in br.readlines():
            self.code = self.code + line
            if line != None:
                data += line + " "
        # //splits the String by white space except where it is between quotation marks, also splits string by brackets to seperate the brackets out, and commas

        stringArray = data.split(" (?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\[(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\](?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + ",(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)")

        # //convert string array into an arraylist
        list1 = str(stringArray[0]).split('\n')

        # list1 = [[broken,index] for data in list1 for broken in data.split(' ') for index in range(0,len(data.split(' ')))]
        count = 0
        list2 = []
        for data in list1:
            if '--' not in data:
                for broken in data.split(' '):
                    if len(broken) > 0:
                        list2.append([broken, count])
            count += 1

        # //remove all excess whitespace that may be left over from the split
        list1 = [temp for temp in list2 if len(temp[0].strip()) > 0]

        return list1

    # checks whether a string is an integer number or not
    def isIntNumber(self, s):
        return s.matches("-?\\d+?")

    # checks whether a string is a float number or not
    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def isFloatNumber(self, s):
        return s.matches("-?\\d+(\\.\\d+)")

    # checks whether a string is a string literal or not
    def isStringLiteral(self, s):
        return (s.startsWith("\"") and s.endsWith("\""))

    # checks whether a string is an identifier or not
    def isIdentifier(self, s):
        return (not s.contains("(") or not s.contains(")")) and (not s.startsWith("\"") or not s.endsWith("\""))

    def search(self, tokens):
        currentCode = -1
        keyword = ""
        # print(tokens)
        # print(tokens)

        if str(BEGIN_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = BEGIN_KEYWORD.returnid()
            keyword = BEGIN_KEYWORD.returnkeyword()
        elif str(END_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = END_KEYWORD.returnid()
            keyword = END_KEYWORD.returnkeyword()
        elif str(WHILE_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = WHILE_KEYWORD.returnid()
            keyword = WHILE_KEYWORD.returnkeyword()
        elif str(IF_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = IF_KEYWORD.returnid()
            keyword = IF_KEYWORD.returnkeyword()
        elif str(ELSE_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = ELSE_KEYWORD.returnid()
            keyword = ELSE_KEYWORD.returnkeyword()
        elif str(ELSEIF_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = ELSEIF_KEYWORD.returnid()
            keyword = ELSEIF_KEYWORD.returnkeyword()
        elif str(FOR_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = FOR_KEYWORD.returnid()
            keyword = FOR_KEYWORD.returnkeyword()
        elif str(RETURN_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = RETURN_KEYWORD.returnid()
            keyword = RETURN_KEYWORD.returnkeyword()
        elif str(BREAK_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = BREAK_KEYWORD.returnid()
            keyword = BREAK_KEYWORD.returnkeyword()
        elif str(CONTINUE_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = CONTINUE_KEYWORD.returnid()
            keyword = CONTINUE_KEYWORD.returnkeyword()
        elif str(FUNCTION_KEYWORD.returnvalue()).lower() in str(tokens).lower():
            currentCode = FUNCTION_KEYWORD.returnid()
            keyword = FUNCTION_KEYWORD.returnkeyword()
        elif str(DECLARE_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = DECLARE_OPERATOR.returnid()
            keyword = DECLARE_OPERATOR.returnkeyword()
        elif str(ASSIGNMENT_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = ASSIGNMENT_OPERATOR.returnid()
            keyword = ASSIGNMENT_OPERATOR.returnkeyword()
        elif str(LE_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = LE_OPERATOR.returnid()
            keyword = LE_OPERATOR.returnkeyword()
        elif str(LT_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = LT_OPERATOR.returnid()
            keyword = LT_OPERATOR.returnkeyword()
        elif str(GE_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = GE_OPERATOR.returnid()
            keyword = GE_OPERATOR.returnkeyword()
        elif str(GT_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = GT_OPERATOR.returnid()
            keyword = GT_OPERATOR.returnkeyword()
        elif str(EQ_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EQ_OPERATOR.returnid()
            keyword = EQ_OPERATOR.returnkeyword()
        elif str(NE_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = NE_OPERATOR.returnid()
            keyword = NE_OPERATOR.returnkeyword()
        elif str(ADD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = ADD_OPERATOR.returnid()
            keyword = ADD_OPERATOR.returnkeyword()
        elif str(SUB_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = SUB_OPERATOR.returnid()
            keyword = SUB_OPERATOR.returnkeyword()
        elif str(MUL_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MUL_OPERATOR.returnid()
            keyword = MUL_OPERATOR.returnkeyword()
        elif str(DIV_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = DIV_OPERATOR.returnid()
            keyword = DIV_OPERATOR.returnkeyword()
        elif str(MOD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MOD_OPERATOR.returnid()
            keyword = MOD_OPERATOR.returnkeyword()
        elif str(REV_DIV_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = REV_DIV_OPERATOR.returnid()
            keyword = REV_DIV_OPERATOR.returnkeyword()
        elif str(EXP_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EXP_OPERATOR.returnid()
            keyword = EXP_OPERATOR.returnkeyword()
        elif str(EACH_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EACH_OPERATOR.returnid()
            keyword = EACH_OPERATOR.returnkeyword()
        elif str(LEFT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = LEFT_PARENTHESIS.returnid()
            keyword = LEFT_PARENTHESIS.returnkeyword()
        elif str(RIGHT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = RIGHT_PARENTHESIS.returnid()
            keyword = RIGHT_PARENTHESIS.returnkeyword()
        elif len(tokens) > 1 and str(tokens)[:-1].lower().isidentifier():
            currentCode = IDENTIFIER.returnid()
            keyword = IDENTIFIER.returnkeyword()
        elif str(tokens).lower().isidentifier():
            currentCode = IDENTIFIER.returnid()
            keyword = IDENTIFIER.returnkeyword()
        elif len(tokens) > 1 and str(tokens).lower().isidentifier() != True:
            currentCode = KEYWORD.returnid()
            keyword = KEYWORD.returnkeyword()
        elif str(tokens).lower().isdigit():
            currentCode = INT_LITERAL.returnid()
            keyword = INT_LITERAL.returnkeyword()
        elif self.isfloat(str(tokens).lower()):
            currentCode = FLOAT_LITERAL.returnid()
            keyword = FLOAT_LITERAL.returnkeyword()
        elif str(PRINT_FUNCTION.returnvalue()).lower() in str(tokens).lower():
            currentCode = PRINT_FUNCTION.returnid()
            keyword = PRINT_FUNCTION.returnkeyword()
        else:
            print(tokens)
            print('token failed')
            # raise Exception
            logging.error('The lookup function was unable to process. \n' + str(
                tokens).lower() + "\nPlease find the missing element.")

        return [currentCode, keyword]

    def searchToken(self, bitches):
        currentCode = -1

        if str(BEGIN_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = BEGIN_KEYWORD
        elif str(END_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = END_KEYWORD
        elif str(WHILE_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = WHILE_KEYWORD
        elif str(IF_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = IF_KEYWORD
        elif str(ELSE_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = ELSE_KEYWORD
        elif str(ELSEIF_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = ELSEIF_KEYWORD
        elif str(FOR_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = FOR_KEYWORD
        elif str(RETURN_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = RETURN_KEYWORD
        elif str(BREAK_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = BREAK_KEYWORD
        elif str(CONTINUE_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = CONTINUE_KEYWORD
        elif str(FUNCTION_KEYWORD.returnvalue()).lower() in str(bitches).lower():
            currentCode = FUNCTION_KEYWORD
        elif str(ASSIGNMENT_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = ASSIGNMENT_OPERATOR
        elif str(LE_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = LE_OPERATOR
        elif str(LT_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = LT_OPERATOR
        elif str(GE_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = GE_OPERATOR
        elif str(GT_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = GT_OPERATOR
        elif str(EQ_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = EQ_OPERATOR
        elif str(NE_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = NE_OPERATOR
        elif str(ADD_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = ADD_OPERATOR
        elif str(SUB_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = SUB_OPERATOR
        elif str(MUL_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = MUL_OPERATOR
        elif str(DIV_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = DIV_OPERATOR
        elif str(MOD_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = MOD_OPERATOR
        elif str(REV_DIV_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = REV_DIV_OPERATOR
        elif str(EXP_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = EXP_OPERATOR
        elif str(EACH_OPERATOR.returnvalue()).lower() in str(bitches).lower():
            currentCode = EACH_OPERATOR
        elif str(LEFT_PARENTHESIS.returnvalue()).lower() in str(bitches).lower():
            currentCode = LEFT_PARENTHESIS
        elif str(RIGHT_PARENTHESIS.returnvalue()).lower() in str(bitches).lower():
            currentCode = RIGHT_PARENTHESIS
        elif str(PRINT_FUNCTION.returnvalue()).lower() in str(bitches).lower():
            currentCode = PRINT_FUNCTION
        elif str(bitches).lower().isidentifier():
            currentCode = IDENTIFIER
            currentCode = Tokens(str(bitches).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        elif str(bitches).lower().isdigit():
            currentCode = INT_LITERAL
            currentCode = Tokens(str(bitches).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        elif self.isfloat(str(bitches).lower()):
            currentCode = FLOAT_LITERAL
            currentCode = Tokens(str(bitches).lower(), currentCode.getTypeID(), currentCode.getKeyword())

        else:
            logging.error('The lookup function was unable to process. \n' + str(
                bitches).lower() + "\nPlease find the missing element.")

        temp = Tokens(str(bitches).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        return temp


s = Scanner("programs.adb")
print(s.getTokens())
# s = Scanner("test2.jl")
# print(s.getTokens())
# s = Scanner("test3.jl")
# print(s.getTokens())
# s = Scanner("test4.jl")
# print(s.getTokens())
