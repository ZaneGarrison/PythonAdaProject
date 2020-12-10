class Tokens:
    def __init__(self, value, id, keyword):
        self.value = value
        self.ID = id
        self.keyword = keyword
        self.row = -1

    def setvalue(self, v):
        value = v

    def returnvalue(self):
        return self.value

    def getValue(self):
        return self.value

    def setid(self, id):
        self.ID = id

    def returnid(self):
        return self.ID

    def getTypeID(self):
        return self.ID

    def setkeyword(self, kw):
        self.keyword = kw

    def returnkeyword(self):
        return self.keyword

    def getKeyword(self):
        return self.keyword

    def getRow(self):
        return self.row

    def setRow(self, kw):
        self.row = kw

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
DECLARE_OPERATOR = Tokens(":=", 299, "declare_operator")
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
COMMA_OPERATOR = Tokens(",", 317, "comma_operator")
LEFT_PARENTHESIS = Tokens("(", 315, "left_parenthesis")
RIGHT_PARENTHESIS = Tokens(")", 316, "right_parenthesis")
KEYWORD = Tokens("", 204, "keyword")
IDENTIFIER = Tokens("", 200, "identifier")
INT_LITERAL = Tokens("", 201, "int_literal")
FLOAT_LITERAL = Tokens("", 202, "float_literal")
PRINT_FUNCTION = Tokens("print", 500, "print_function")