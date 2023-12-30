from lark import Lark

json_parser = Lark("""      

    expr: mblock (op_or mblock)* 
    mblock: ablock (op_and ablock)*
    ablock: term | op_not term 
    term: func | "{" expr "}"
    op_or: "|"  
    op_and: "&" 
    op_not: "!"         
    func: "{" "*"value "}" -> starts_with
        | "{" value"*" "}" -> ends_with
        | "{" "*"value"*" "}" -> contains
        | "{" value "}" -> exact
    value: ESCAPED_STRING     


    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS

    """, start='expr')

#text = '{{"lvl1"}&{"lvl1"}}|{"lvl0"}&{{"lvl1"}&{{"lvl2"}&{{"lvl3"}&{{"lvl4"}&{{"lvl5"}&{"lvl6"}}}}}}'
text = '{{"lvl1"}&{"lvl1"}}|{"lvl0"}&{{"lvl1"}&{{"lvl2"}&{{"lvl3"}&{{"lvl4"}&{{"lvl5"}&{"lvl6"}}}}}}'

x = json_parser.parse(text)
x = json_parser.parse(text)
print( x.pretty() )

