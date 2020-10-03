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