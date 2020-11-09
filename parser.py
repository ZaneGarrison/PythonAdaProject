from tokens import *
from scanner import Scanner
from binaryTree import *


class Parser():
    def __init__(self):
        self.parseTreeRoot = None
        self.parseTrees = []
        self.tokens = []
        self.nextToken = None
        self.idIntHolder = None
        self.hasFunction = False

        self.analyser = Scanner("test5.jl")
        print('code: ')
        temp = self.analyser.getTokens(returnTokens=True)
        for data in temp:
            self.tokens.append(data)
        self.nextToken = self.tokens.pop(0)

    def parse(self):
        print(self.analyser.code)
        s = Scanner("test5.jl")
        print(s.getTokens())
        print('Parser Output:')
        print()
        if self.nextToken.getTypeID() == FUNCTION_KEYWORD.getTypeID():
            self.hasFunction = True
            self.function()
        else:
            self.block()

    def statement(self):
        print("<statement>")
        print("<statement>->", end=' ')
        if (
                self.nextToken.getTypeID() == IDENTIFIER.getTypeID() or self.nextToken.getTypeID() == INT_LITERAL.getTypeID()):
            self.idIntHolder = self.nextToken
            self.lex()
        if (self.nextToken.getTypeID() == ASSIGNMENT_OPERATOR.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parseAssignment()

        if (self.nextToken.getTypeID() == PRINT_FUNCTION.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parsePrintFunction()

        if (self.nextToken.getTypeID() == IF_KEYWORD.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parseIf()

        if (self.nextToken.getTypeID() == WHILE_KEYWORD.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parseWhile()

        if (self.nextToken.getTypeID() == FOR_KEYWORD.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parseFor()

        self.printInOrderValueToKeyword(self.parseTreeRoot)
        self.printPreOrder(self.parseTreeRoot)
        print()
        self.printPostOrder(self.parseTreeRoot)
        print('\n')
        self.addToParseTreeList()

    # parses assignment statements into BNF form also works with for loop assignment expressions
    def parseAssignment(self):
        # output assignment statement form
        print("<assignment_statement>")
        print("<assignment_statement>->", end=' ')
        # output variable keyword that would be on the left hand side of the assignment statement
        print("<" + self.idIntHolder.getKeyword() + ">")
        #print("<" + self.idIntHolder.getValue() + ">")
        # add it to the parse tree
        self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.idIntHolder)

        # output the assignment operator statement
        print("<" + self.nextToken.getKeyword() + ">")

        # move the next token
        self.lex()
        ##determine what type of expression is next
        ##if it is a for loop expression I.E 5 : 10
        if (len(self.tokens) > 0 and self.tokens[0].getTypeID() == EACH_OPERATOR.getTypeID()):
            self.forExpression()
        ##normal arithmetic expressions
        else:
            self.arithmeticExpression()

    # handles parsing simple math expressions
    def arithmeticExpression(self):
        # output statements
        print("<arithmetic_expression>")
        print("<arithmetic_expression>->", end='')
        # if the nextToken is an operator
        if (self.nextToken.getTypeID() == ADD_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == SUB_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MUL_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == DIV_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MOD_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == REV_DIV_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == EACH_OPERATOR.getTypeID()):
            # output the apropriate keyword
            print("<" + self.nextToken.getKeyword() + ">")
            # add it to the parse tree
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            # move to the next token
            self.lex()
            # calls itself since  you could have something like 1+1-3
            self.arithmeticExpression()
            # move to the next token
            self.lex()

        # determines if the token is a left parenthesis
        if (self.nextToken.getTypeID() == LEFT_PARENTHESIS.getTypeID()):
            # calls itself since an arithmetic expression is conrained between two parenthesis
            self.arithmeticExpression()
            # error checks
            if (self.nextToken.getTypeID() != RIGHT_PARENTHESIS.getTypeID()):
                self.error("Error unclosed parenthesis")

        # determines if the token is an identifier or an int
        if (self.nextToken.getTypeID() == IDENTIFIER.getTypeID() or
                self.nextToken.getTypeID() == INT_LITERAL.getTypeID()):
            # add the token to the parse tree
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            # determine if the token after this one will be an int or each operator
            # to determine the output format so it looks consistent and cleaner
            if (len(self.tokens) > 0 and self.tokens[0].getTypeID() == INT_LITERAL.getTypeID() or
                    len(self.tokens) > 0 and self.tokens[0].getTypeID() == EACH_OPERATOR.getTypeID()):
                print("<" + self.nextToken.getKeyword() + ">")
            else:
                print("<" + self.nextToken.getKeyword() + ">")

    # used with for epressions in the form of for x = 5:10
    def forExpression(self):
        # output for expression statements
        print("<for_expresssion>")
        print("<for_expression>->", end='')
        # syntax check
        if (self.nextToken.getTypeID() == IDENTIFIER.getTypeID() or
                self.nextToken.getTypeID() == INT_LITERAL.getTypeID()):
            # since range arguments can be expressions
            self.arithmeticExpression()
            # iterate to the next token
            self.lex()
        else:
            self.error("Error for loop missing iteration variable")
        # syntax check
        if (self.nextToken.getTypeID() != EACH_OPERATOR.getTypeID()):
            self.error("Error for loop missing :")
        else:
            # adds the : to the parse tree
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            # iterate to the next token
            self.lex()
            # handle the next expression on the right hand side of :
            self.arithmeticExpression()

    # handles parsing boolean expressions for if statements and while loops
    def booleanExpression(self):
        print("<boolean_expression>")
        print("<boolean_expression>->", end='')
        # determine if next token is a boolean operator
        if (self.nextToken.getTypeID() == LE_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == LT_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == GE_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == GT_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == EQ_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == NE_OPERATOR.getTypeID()):
            print("<" + self.nextToken.getKeyword() + ">")
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.lex()

        else:
            self.error("Error if statement requires boolean expressions")

        # since booleans types can be statements on one side to check
        if (self.nextToken.getTypeID() == LEFT_PARENTHESIS.getTypeID()):
            self.statement()
            if (self.nextToken.getTypeID() != RIGHT_PARENTHESIS.getTypeID()):
                self.error("Error unclosed parenthesis")
            # determine if next operator is an identifier or int literal
            if (self.nextToken.getTypeID() == IDENTIFIER.getTypeID() or
                    self.nextToken.getTypeID() == INT_LITERAL.getTypeID()):
                print("<" + self.nextToken.getKeyword() + ">")
                # add to the parse tree
                self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
                # move to the next token
                self.lex()
                # check evaluate the token which iw the second operand in the equality
                self.arithmeticExpression()

    # removes a token from the tokens linked list effectively incrementing by one
    def lex(self):
        if (len(self.tokens) < 1):
            return None
        else:
            self.nextToken = self.tokens.pop(0)

    # handles parsing functions
    def function(self):
        # output function statment
        print("<function>")
        print("<function>->", end=' ')
        self.lex()
        if (self.nextToken.getTypeID() != IDENTIFIER.getTypeID()):
            self.error("Error missing function name")

        self.lex()
        if (self.nextToken.getTypeID() != LEFT_PARENTHESIS.getTypeID()):
            self.error("Error missing function  opening parenthesis")

        self.lex()
        if (self.nextToken.getTypeID() != RIGHT_PARENTHESIS.getTypeID()):
            self.error("Error missing function  closing parenthesis")

        self.block()
        if (self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):
            self.error("Error missing end for function")

        self.lex()

    def block(self):
        print("<block>")
        print("<block>->", end='')
        # determine when to stop iterating
        if (self.hasFunction):
            # iterate through the tokens
            while (len(self.tokens) > 1):
                if ((self.nextToken.getTypeID() == IDENTIFIER.getTypeID()) or
                        (self.nextToken.getTypeID() == INT_LITERAL.getTypeID()) or
                        (self.nextToken.getTypeID() == IF_KEYWORD.getTypeID()) or
                        (self.nextToken.getTypeID() == FOR_KEYWORD.getTypeID()) or
                        (self.nextToken.getTypeID() == PRINT_FUNCTION.getTypeID()) or
                        (self.nextToken.getTypeID() == WHILE_KEYWORD.getTypeID())):
                    self.statement()
                # move to the next token
                self.lex()
        else:
            # iterate through the tokens
            while (len(self.tokens) > 0):
                if ((self.nextToken.getTypeID() == IDENTIFIER.getTypeID()) or
                        (self.nextToken.getTypeID() == INT_LITERAL.getTypeID()) or
                        (self.nextToken.getTypeID() == IF_KEYWORD.getTypeID()) or
                        (self.nextToken.getTypeID() == FOR_KEYWORD.getTypeID()) or
                        (self.nextToken.getTypeID() == PRINT_FUNCTION.getTypeID()) or
                        (self.nextToken.getTypeID() == WHILE_KEYWORD.getTypeID())):
                    self.statement()
                # move to the next token
                self.lex()

    # parses the ulia print function
    def parsePrintFunction(self):
        # output print_function statement
        print("<" + self.nextToken.getKeyword() + ">->", end='')
        # move to the next token
        self.lex()
        # syntax check
        if (self.nextToken.getTypeID() != LEFT_PARENTHESIS.getTypeID()):
            self.error("Error missing parenthesis for print function")
        else:
            # move to the next token
            self.lex()
            # handle the expression between the parenthesis
            self.arithmeticExpression()
            # move to the next token
            self.lex()
        # syntax chceck
        if (self.nextToken.getTypeID() != RIGHT_PARENTHESIS.getTypeID()):
            self.error("Error unclosed parenthesis")
        else:
            self.lex()

    # parses the if and else statements
    def parseIf(self):
        # output if statement bnf form
        print("<if_statement>")
        print("<if_statement>->", end='')
        # move to the next token
        self.lex()

        # parrse the boolean expressionS
        self.booleanExpression()
        # print the boolean expression
        self.printInOrderValueToKeyword(self.parseTreeRoot)
        self.printPreOrder(self.parseTreeRoot)
        print()
        self.printPostOrder(self.parseTreeRoot)
        print()
        self.addToParseTreeList()
        # move to the nexr token
        self.lex()
        # keep parsing statements until th end of the if statement
        while ((self.nextToken.getTypeID() != END_KEYWORD.getTypeID() and
                self.nextToken.getTypeID() != ELSE_KEYWORD.getTypeID())
               and not (len(self.tokens) < 1)):
            self.statement()
            if (self.nextToken.getTypeID() != ELSE_KEYWORD.getTypeID() and
                    self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):
                self.lex()
        # parse the else statements
        if (self.nextToken.getTypeID() == ELSE_KEYWORD.getTypeID()):
            print("<else_statement>")
            print("<else_statement>->", end='')
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            while (self.nextToken.getTypeID() != END_KEYWORD.getTypeID() and
                   not (len(self.tokens) < 1)):
                self.lex()
                if (self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):
                    self.statement()

        if (self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):
            self.error("Error missing end for if ")

    # parses the while loop
    def parseWhile(self):
        # output while statement in bnf form
        print("<while_statement>")
        print("<while_statement>->", end='')
        # move to the next token
        self.lex()
        # parse the boolean expressionS
        self.booleanExpression()
        # output boolean expression
        self.printInOrderValueToKeyword(self.parseTreeRoot)
        self.printPreOrder(self.parseTreeRoot)
        print()
        self.printPostOrder(self.parseTreeRoot)
        print()
        self.addToParseTreeList()
        # move to the next token
        self.lex()

        # parse all the statements within the while loop
        while (self.nextToken.getTypeID() != END_KEYWORD.getTypeID() and not (len(self.tokens) < 1)):
            self.statement()
            if (self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):  # move to the next token
                self.lex()

        if (self.nextToken.getTypeID() != END_KEYWORD.getTypeID()):
            self.error("Error missing end statement for while loop")

    # parses the for loop
    def parseFor(self):
        # output for statement in bnf form
        print("<for_statement>")
        print("<for_statement>->", end='')
        # move to the next token
        self.lex()
        # check for syntax error
        if (self.nextToken.getTypeID() != IDENTIFIER.getTypeID()):
            self.error("Error in for statement")
        else:
            self.statement()

    # outputs error messages to the console
    def error(self, msg):
        print(msg)

    def addToParseTree(self, root, item):
        if root is None:
            root = binaryTree()
            root.setValue(item)
        elif root.getLeftChild() is None:
            root.setLeftChild(self.addToParseTree(root.getLeftChild(), item))
        elif root.getRightChild() is None:
            root.setRightChild(self.addToParseTree(root.getRightChild(), item))
        elif root.getRightChild() is not None:
            root.setRightChild(self.addToParseTree(root.getRightChild(), item))
        return root

    def printInOrderValueToKeyword(self, root):
        if root is None:
            return
        self.printInOrderValueToKeyword(root.getLeftChild())
        print(root.getValue().returnvalue() + " ->", end='')
        print(root.getValue().returnkeyword())
        self.printInOrderValueToKeyword(root.getRightChild())


    def printPreOrder(self, root):
        if root is None:
            return
        print(root.getValue().getValue() + " ", end= ' ')
        self.printPreOrder(root.getLeftChild())
        self.printPreOrder(root.getRightChild())


    def printPostOrder(self, root):
        if root is None:
            return
        print(root.getValue().getValue() + " ", end= ' ')
        self.printPostOrder(root.getRightChild())
        self.printPostOrder(root.getLeftChild())


    def addToParseTreeList(self):
        self.parseTrees.append(self.parseTreeRoot)
        self.parseTreeRoot = None


test = Parser()
test.parse()


