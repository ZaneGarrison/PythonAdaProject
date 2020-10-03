import logging


class Tokens:
    def __init__(self, value, id, keyword):
        self.value = value
        self.ID = id
        self.keyword = keyword

    def setvalue(self, v):
        value = v

    def returnvalue(self):
        return self.value

    def setid(self, id):
        self.ID = id

    def returnid(self):
        return self.ID

    def setkeyword(self, kw):
        self.keyword = kw

    def returnkeyword(self):
        return self.keyword


BEGIN_KEYWORD = Tokens("begin", 100, "begin_keyword")
END_KEYWORD = Tokens("end", 101, "end_keyword")
WHILE_KEYWORD = Tokens("while", 102, "while_keyword")
IF_KEYWORD = Tokens("if", 103, "if_keyword")
ELSE_KEYWORD = Tokens("else", 104, "else_keyword")
ELSEIF_KEYWORD = Tokens("elseif", 105, "elseif_keyword")
FOR_KEYWORD = Tokens("for", 106, "for_keyword")
RETURN_KEYWORD = Tokens("return", 107, "return_keyword")
BREAK_KEYWORD = Tokens("break", 108, "break_keyword")
CONTINUE_KEYWORD = Tokens("continue", 109, "continue_keyword")
FUNCTION_KEYWORD = Tokens("function", 110, "function_keyword")
ASSIGNMENT_OPERATOR = Tokens("=", 300, "assignment_operator")
LE_OPERATOR = Tokens("<=", 301, "le_operator")
LT_OPERATOR = Tokens("<", 302, "lt_operator")
GE_OPERATOR = Tokens(">=", 303, "ge_operator")
GT_OPERATOR = Tokens(">", 304, "gt_operator")
EQ_OPERATOR = Tokens("==", 305, "eq_operator")
NE_OPERATOR = Tokens("!=", 306, "ne_operator")
ADD_OPERATOR = Tokens("+", 307, "add_operator")
SUB_OPERATOR = Tokens("-", 308, "sub_operator")
MUL_OPERATOR = Tokens("*", 309, "mul_operator")
DIV_OPERATOR = Tokens("/", 310, "div_operator")
MOD_OPERATOR = Tokens("%", 311, "mod_operator")
REV_DIV_OPERATOR = Tokens("\\", 312, "rev_div_operator")
EXP_OPERATOR = Tokens("^", 313, "exp_operator")
EACH_OPERATOR = Tokens(":", 314, "each_operator")
LEFT_PARENTHESIS = Tokens("(", 315, "left_parenthesis")
RIGHT_PARENTHESIS = Tokens(")", 316, "right_parenthesis")

IDENTIFIER = Tokens("", 200, "identifier")
INT_LITERAL = Tokens("", 201, "int_literal")
FLOAT_LITERAL = Tokens("", 202, "float_literal")
PRINT_FUNCTION = Tokens("print", 500, "print_function")

try:
    testFile = open("test5.jl", "r")
except FileNotFoundError:
    logging.critical("The file was not found")


class Scanner:

    # constructor
    def __init__(self):
        try:
            self.outputFileName = "output.txt"
            self.inputFileName = "test5.jl"
            # set up the input and output files as well as the buffered writter for writing to an output file
            # input file mut be in the same directory as the package
            self.inputFile = open(inputFileName)
            self.outputFile = open(outputFileName)
            self.bw = open(outputFileName)
            self.variables = None


        except Exception as ex:
            logging.log('error', ex)

    def getTokens(self):

        tokenList = []
        try:
            # initialize Arraylist to hold tokens
            data = readInputFile()

            # iterate through every string
            for s in data:
                # call the lookup function which will determine the token type and return the appropriate output message
                tokenList.add(lookup(s))
                # System.out.println(s);

            for t in tokenList:
                pass
                # System.out.println(t.toString());

            # close the output file
            self.bw.close()


        except Exception as ex:
            logging.log('error', ex)

        return tokenList

    def readInputFile(self):
        # set up string for holding file contents as well as the buffered reader
        data = ""
        br = open(self.inputFile)
        # //used to read file line by line
        line = br.readline()
        # //read file line by line
        while ((line == br.readLine()) != None):
            data += line + " "

        # //splits the String by white space except where it is between quotation marks, also splits string by brackets to seperate the brackets out, and commas

        stringArray = data.split(" (?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\[(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\](?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + ",(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)");

        # //convert string array into an arraylist
        list1 = stringArray
        # //remove all excess whitespace that may be left over from the split
        list1 = [data for data in list1 if len(data.trim()) > 0]
        return list1

    # checks whether a string is an integer number or not
    def isIntNumber(self, s):
        return s.matches("-?\\d+?")

    # checks whether a string is a float number or not
    def isFloatNumber(self, s):
        return s.matches("-?\\d+(\\.\\d+)")

    # checks whether a string is a string literal or not
    def isStringLiteral(self, s):
        return (s.startsWith("\"") and s.endsWith("\""))

    # checks whether a string is an identifier or not
    def isIdentifier(self, s):
        return (not s.contains("(") or not s.contains(")")) and (not s.startsWith("\"") or not s.endsWith("\""))

    def search(tokens):
        currentCode = -1
        keyword = ""

        if str(BEGIN_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = BEGIN_KEYWORD.returnid()
            keyword = BEGIN_KEYWORD.returnkeyword()
        elif str(END_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = END_KEYWORD.returnid()
            keyword = END_KEYWORD.returnkeyword()
        elif str(END_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = END_KEYWORD.returnid()
            keyword = END_KEYWORD.returnkeyword()
        elif str(WHILE_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = WHILE_KEYWORD.returnid()
            keyword = WHILE_KEYWORD.returnkeyword()
        elif str(IF_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = IF_KEYWORD.returnid()
            keyword = IF_KEYWORD.returnkeyword()
        elif str(ELSE_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = ELSE_KEYWORD.returnid()
            keyword = ELSE_KEYWORD.returnkeyword()
        elif str(FOR_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = FOR_KEYWORD.returnid()
            keyword = FOR_KEYWORD.returnkeyword()
        elif str(RETURN_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = RETURN_KEYWORD.returnid()
            keyword = RETURN_KEYWORD.returnkeyword()
        elif str(BREAK_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = BREAK_KEYWORD.returnid()
            keyword = BREAK_KEYWORD.returnkeyword()
        elif str(CONTINUE_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = CONTINUE_KEYWORD.returnid()
            keyword = CONTINUE_KEYWORD.returnkeyword()
        elif str(FUNCTION_KEYWORD.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = FUNCTION_KEYWORD.returnid()
            keyword = FUNCTION_KEYWORD.returnkeyword()
        elif str(ASSIGNMENT_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = ASSIGNMENT_OPERATOR.returnid()
            keyword = ASSIGNMENT_OPERATOR.returnkeyword()
        elif str(LE_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = LE_OPERATOR.returnid()
            keyword = LE_OPERATOR.returnkeyword()
        elif str(LT_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = LT_OPERATOR.returnid()
            keyword = LT_OPERATOR.returnkeyword()
        elif str(GE_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = GE_OPERATOR.returnid()
            keyword = GE_OPERATOR.returnkeyword()
        elif str(NE_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower:
            currentCode = NE_OPERATOR.returnid()
            keyword = NE_OPERATOR.returnkeyword()
        elif str(GT_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = GT_OPERATOR.returnid()
            keyword = GT_OPERATOR.returnkeyword()
        elif str(EQ_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = EQ_OPERATOR.returnid()
            keyword = EQ_OPERATOR.returnkeyword()
        elif str(ADD_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = ADD_OPERATOR.returnid()
            keyword = ADD_OPERATOR.returnkeyword()
        elif str(SUB_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = SUB_OPERATOR.returnid()
            keyword = SUB_OPERATOR.returnkeyword()
        elif str(MUL_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = MUL_OPERATOR.returnid()
            keyword = MUL_OPERATOR.returnkeyword()
        elif str(DIV_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = DIV_OPERATOR.returnid()
            keyword = DIV_OPERATOR.returnkeyword()
        elif str(EACH_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = EACH_OPERATOR.returnid()
            keyword = EACH_OPERATOR.returnkeyword()
        elif str(LEFT_PARENTHESIS.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = LEFT_PARENTHESIS.returnid()
            keyword = LEFT_PARENTHESIS.returnkeyword()
        elif str(RIGHT_PARENTHESIS.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = RIGHT_PARENTHESIS.returnid()
            keyword = RIGHT_PARENTHESIS.returnkeyword()
        elif str(MOD_OPERATOR.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = MOD_OPERATOR.returnid()
            keyword = MOD_OPERATOR.returnkeyword()
        elif str(PRINT_FUNCTION.returnvalue()).lower() == str(tokens.returnvalue()).lower():
            currentCode = PRINT_FUNCTION.returnid()
            keyword = PRINT_FUNCTION.returnkeyword()
