class GrammarRule():    
    def __init__(self, name, tokenList):  
        self.name = name
        self.tokenList = tokenList
    
    def check(self, index, token):        
        if (index>=len(self.tokenList)):
            return False
        elif(str(self.tokenList[index]) is str(token)):            
            return True
        else:
            return False
        
class Parser():
    def __init__(self):
        self.grammarRuleList = [];        

        self.grammarRuleList.append(  GrammarRule("MUL_COMMENT", ["IDENT", "IDENT","STR_LIT", "IDENT","BE_KW"]) )

        #BASE ARITH
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("ARITH_EXP", ["FLT_LIT", "P_OP","IDENT"]) )

        #BASE REL
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "EQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "UNEQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "GRTR_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "LESS_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "GRTR_EQ","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["IDENT", "LESS_EQ","IDENT"]) )
        
        #RECURSING ARITH 
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["UNEQ_OP","FLT_LIT", "P_OP","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_OP","FLT_LIT", "P_OP","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_OP","FLT_LIT", "P_OP","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["GRTR_EQ","FLT_LIT", "P_OP","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["LESS_EQ","FLT_LIT", "P_OP","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "ADD_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "SUB_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "MUL_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "DIV_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "P_OP","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "ADD_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "SUB_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "MUL_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "DIV_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","IDENT", "P_OP","FLT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","INT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","INT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","INT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","INT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","INT_LIT", "P_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","FLT_LIT", "ADD_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","FLT_LIT", "SUB_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","FLT_LIT", "MUL_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","FLT_LIT", "DIV_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_EXP", ["EQ_OP","FLT_LIT", "P_OP","IDENT"]) )
        

        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "EQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "UNEQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "GRTR_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "LESS_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "GRTR_EQ","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["AND_OP","IDENT", "LESS_EQ","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "EQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "UNEQ_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "GRTR_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "LESS_OP","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "GRTR_EQ","IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["OR_OP","IDENT", "LESS_EQ","IDENT"]) )

        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["NOT_OP","DEL_OPENP","IDENT", "DEL_CLOSEP"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["NOT_OP","DEL_OPENP"]) )
        #Recursing Log Exp
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["DEL_OPENP"]) )
        self.grammarRuleList.append(  GrammarRule("LOG_EXP", ["DEL_CLOSEP"]) )
   
        #Recursing Literals
        self.grammarRuleList.append(  GrammarRule("REC_INT_LITS", ["DEL_ITEMS","FL_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REC_INT_LITS", ["DEL_ITEMS","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REC_INT_LITS", ["DEL_ITEMS","STR_LIT"]) )

        #Data Type Dec
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "INT_LIT","DEL_ITEMS","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "STR_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "STR_LIT","DEL_ITEMS","STR_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "FL_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["IDENT", "COULD_KW","ONLY_KW", "BE_KW", "FL_LIT","DEL_ITEMS","FL_LIT"]) )

        #Variable Dec
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "INT_LIT","DEL_ITEMS","INT_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "STR_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "STR_LIT","DEL_ITEMS","STR_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "FL_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW", "FL_LIT","DEL_ITEMS","FL_LIT"]) )

        self.grammarRuleList.append(  GrammarRule("DT_DEC", ["LET_KW", "IDENT","DEL_DT", "IDENT","BE_KW"]) )

        #Relations Statement
        self.grammarRuleList.append(  GrammarRule("REL_STMT", ["IDENT", "REL_OF","STR_LIT", "REL_IS","STR_LIT"]) )
        self.grammarRuleList.append(  GrammarRule("REL_STMT", ["IDENT", "REL_OF","STR_LIT"]))

        #Conversion Statement
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "ADD_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "SUB_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "MUL_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "DIV_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "P_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "AND_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "OR_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "NOT_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "EQ_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "UNEQ_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "GRTR_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "LESS_OP", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "GRTR_EQ", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "LESS_EQ", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "POINT_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "ACTION_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "REM_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "SHORTEN_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "REP_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "CONDI_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "ADVERB_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "PREP_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "REL_OF", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "REL_IS", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "LET_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "COULD_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "ONLY_KW", "KW_CONV", "STR_LIT"]))
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "BE_KW", "KW_CONV", "STR_LIT"]))

        #Input
        self.grammarRuleList.append(  GrammarRule("CONV_STMT", ["LET_KW", "BE_KW", "KW_CONV", "STR_LIT"]))
   





       

        
        
   
      
        
        self.expressionList = []
        
    
    def parseSymbolTable(self, lexemeList):          
        currentIndex = 0
        currentRule = None

        for symbol in lexemeList:            
            token,line = symbol
            
            
            #print(currentIndex, " ", token)
            
            if(token == "INVALID"):
                #Invalid Token Found
                print("Error: Invalid Token found at Line:" + str(line)  )
                return;     
               
             # Ignore tokens with value "N_WORD"
            if token == "NOISE_W":
                continue

            ruleMatch = 0
            for rule in self.grammarRuleList:
                if(rule.check(currentIndex, token)):
                    currentRule = rule
                    ruleMatch+=1;            
            
                
            if(ruleMatch==0 and currentRule is not None):
                #none of the rules match
                print("Error: Expecting Token: " + str(currentRule.tokenList[currentIndex]) + " at Line:" + str(line))
                return
            elif(currentRule is not None and currentIndex+1 == len(currentRule.tokenList)):
                #epression is found
                self.expressionList.append(currentRule)
                currentIndex = 0
            else:
                currentIndex +=1
                
        if(currentRule is None):
            print("Error: No")
        else:
            print("Success: Syntax Analysis Complete. Found " + str(len(self.expressionList)) + " syntaxes.")