# simple-calculator-compiler
Compilador de calculadora que interpreta expressões matemáticas com suporte a variáveis, decimais, operações aritméticas básicas, exponenciação, operadores relacionais e ordem de precedência (parênteses incluídos).
<br><br>
## Tecnologias
Este projeto foi desenvolvido em Python 3 utilizando a biblioteca PLY (Python Lex-Yacc), baseada na documentação disponível em https://www.dabeaz.com/ply/ply.html
<br><br>
## Estrutura do projeto 
O repositório possui a seguinte organização:
```text
simple-calculator-compiler/
├── examples/
│   └── example1.calc
├── src/
│   ├── calculadoraLex.py
│   └── calculadoraParser.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Como rodar 
Para rodar o compilador, siga os passos abaixo:
1. Instale o pacote necessário:
  ```bash
  pip install ply
  ```
2. Execute o compilador:
  ```bash
  python src/calculadoraParser.py
  ```
3. Digite comandos como os disponíveis em examples/example1.calc:
 ```text
 # Atribuição de variáveis
 w := 4
 x := -2
 y := 4.5
 z := 3.8 + 5
    
 # Operações aritméticas básicas
 6.2 + 9.3
 x + 3.5
 w - y 
 -x
 x * 2 + 5
 2 / 5
    
 # Exponenciação
 x ** 2
 4 ** 5 + y ** 2
    
 # Ordem de precedência
 x + y * 3
 (x + y) * 3
 6 * 3 + 8 / 2 - 1 * 4
 6 * (3 + 8) / (2 - 1) * 4
    
 # Operadores relacionais
 x < y
 x > y
 x <= y
 x >= y
 x != y
 x == y
 ```
   
O compilador mostra automaticamente o resultado das operações. Para ver o valor de uma variável já atribuída, basta digitá-la no prompt. Para encerrar, pressione Ctrl+C.
<br><br>
## Síntese dos comandos
1. Atribuição de valor: ':='
2. Operadores básicos: '+', '-', '*', '/'
3. Exponenciação: '**'
4. Operadores relacionais: '<', '>', '<=', '>=', '==', '!='
5. Ordem de precedência natural e dada por parênteses '( )'
<br><br>
