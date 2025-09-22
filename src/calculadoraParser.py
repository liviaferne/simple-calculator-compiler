# Analisador Sintatico (parser)

import ply.yacc as yacc

# Importa tokens do arquivo do Analisador Lexico
from calculadoraLex import tokens  

# -----------------------------------

# Dicionario de variaveis
variaveis = {}

# Regras de precedencia
precedence = (
    ('nonassoc', 'MENOR', 'MAIOR', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'DIFERENTE', 'IGUAL'),  
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'POT'),
    ('right', 'UMINUS'),            # menos unario
)

# Regras de gramatica

# Inicio --------------
start = 'comando'

# Ex: x := 2.0
def p_inicio_atribuicao(p):
    'comando : cmd_expr'
    p[0] = p[1]
    
# Ex: x > 2.0    
def p_comando_op_rel(p):
    'comando : op_rel'
    p[0] = p[1]

def p_comando_expr(p):
    'comando : expr'
    p[0] = p[1]
# --------------------    


# CmdExpr -> Id := Expr
def p_cmd_expr(p):
    'cmd_expr : ID ATRIBUIR expr'
    variaveis[p[1]] = p[3] # Armazenando valor da variavel
    p[0] = p[3]
# --------------------  
    
    
# Op_rel -> ‘<’ | ‘>’ | “<=” | “>=” | “!=” | “==”
def p_op_rel(p):
    '''op_rel : expr MENOR expr
              | expr MAIOR expr
              | expr MENOR_IGUAL expr
              | expr MAIOR_IGUAL expr
              | expr DIFERENTE expr
              | expr IGUAL expr'''
    # p[0] recebe true/false
    if(p[2] == '<'):
        p[0] = p[1] < p[3]
    elif(p[2] == '>'):
        p[0] = p[1] > p[3]
    elif(p[2] == '<='):
        p[0] = p[1] <= p[3]
    elif(p[2] == '>='):
        p[0] = p[1] >= p[3]
    elif(p[2] == '!='):
        p[0] = p[1] != p[3]
    elif(p[2] == '=='):
        p[0] = p[1] == p[3]
# --------------------  


# Expr -> Expr + Termo | Expr – Termo | Termo
def p_expressao_operadores(p):
    '''expr : expr MAIS termo 
            | expr MENOS termo'''
    if(p[2] == '+'):
        p[0] = p[1] + p[3]
    elif(p[2] == '-'):
        p[0] = p[1] - p[3]
    
def p_expressao_termo(p):
    'expr : termo'
    p[0] = p[1]
# --------------------  


# Termo -> Termo * Fator | Termo / Fator | Fator | Termo ** Fator
def p_termo_operadores(p):
    '''termo : termo MULT fator 
             | termo DIV fator
             | termo POT fator'''
    if(p[2] == '*'):
        p[0] = p[1] * p[3]
    elif(p[2] == '/'):
        if(p[3] == 0):
            raise Exception("Divisor nao pode ser zero. Analise interrompida.")
        else:
            p[0] = p[1] / p[3]
    elif(p[2] == '**'):
        p[0] = p[1] ** p[3]
        
def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]
# --------------------      
    
    
# Fator -> Num | Id | ( Expr ) | - Fator
def p_fator_num(p):
    'fator : NUMERO'
    p[0] = p[1]
    
def p_fator_id(p):
    'fator : ID'
    var = p[1]
    if var in variaveis:
        p[0] = variaveis[var]
    else:
        raise Exception(f"Variavel '{var}' nao definida.")

def p_fator_parenteses(p):
    'fator : ESQ_PARENTESE expr DIR_PARENTESE'
    p[0] = p[2]
    
def p_fator_uminus(p):
    'fator : MENOS fator %prec UMINUS'
    p[0] = -p[2]
# --------------------      
    
    
# Erros de sintaxe
def p_error(p):
    raise Exception("Entrada com erro de sintaxe.")
    
    
# Criacao do parser
parser = yacc.yacc()

# -----------------------------------
# Executando a calculadora

print("\n---Funcionamento da calculadora---")
print("\nOperacao de atribuicao: := ")
print("Operacoes matematicas: +, -, *, /, **")
print("Uso de parenteses: ( )")
print("Comparacoes entre variaveis: <, >, <=, >=, !=, ==")
print("Ctrl+C para sair.")
print("\n----------------------------------\n")

while True:
    try:
        entrada = input('Entrada: ').strip()
        if not entrada: 
            continue
        resultado = parser.parse(entrada)
        print(f"Resultado: {resultado}\n")
    except (KeyboardInterrupt):
        print("\nEncerrando a calculadora.")
        break
    except Exception as e:
        print(f">>>Erro: {e}\n")
        continue
