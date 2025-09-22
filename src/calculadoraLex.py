# Analisador Lexico

import ply.lex as lex

# Definicao dos tokens
tokens = (
    'ID', 'NUMERO',
    'MAIS', 'MENOS', 'MULT', 'DIV', 'POT',
    'ESQ_PARENTESE', 'DIR_PARENTESE',
    'ATRIBUIR',
    'MENOR', 'MAIOR', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'DIFERENTE', 'IGUAL',
)

# Palavras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'print': 'PRINT',
    'read': 'READ'
}

# -----------------------------------
# Regras de expressao regular 

# Tokens compostos 
def t_ATRIBUIR(t):
    r':='              
    return t
    
def t_MENOR_IGUAL(t):
    r'<='            
    return t
 
def t_MAIOR_IGUAL(t):
    r'>='           
    return t
    
def t_DIFERENTE(t):
    r'!='             
    return t
    
def t_IGUAL(t):
    r'=='                 
    return t

def t_POT(t):
    r'\*\*'
    return t

# Tokens simples
t_MAIS = r'\+'                 
t_MENOS = r'-'                 
t_MULT = r'\*'                 
t_DIV = r'/'                   
t_ESQ_PARENTESE = r'\('        
t_DIR_PARENTESE = r'\)'       
t_MENOR = r'<'             
t_MAIOR = r'>'     

# Token para NUMERO (permite decimal)    
def t_NUMERO(t):
    r'\d+(\.\d+)?' 
    t.value = float(t.value)
    return t
    
# Token para ID (nome variavel)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')     # Busca na lista de palavras reservadas
    if(t.type != 'ID'):
        raise Exception(f"Nome da variavel {t.value} nao permitido. Palavra reservada.")
        t.value = None
    return t

# Caracteres ignorados: 
# espaco e tabulacao
t_ignore = ' \t'  

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    raise Exception(f"Caractere invalido: '{t.value[0]}' na linha {t.lineno}. Analise interrompida.")
    
# Criacao do analisador lexico
lexer = lex.lex()
