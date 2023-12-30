from lark import Lark, tree, Transformer

parser = Lark(r"""

    level: block ([operator block])* 
    ?block: statement | "{" level "}"
    operator: "|"  -> or
             | "&" -> and
             | "!" -> not        
    statement: "{" "*"value "}" -> starts_with
        | "{" value"*" "}" -> ends_with
        | "{" "*"value"*" "}" -> contains
        | "{" value "}" -> exact
    ?value: ESCAPED_STRING     


    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS

    """, start='level')

# text = '{{"lvl1"}&{"lvl1"}}|{"lvl0"}&{{"lvl1"}&{{"lvl2"}&{{"lvl3"}&{{"lvl4"}&{{"lvl5"}&{"lvl6"}}}}}}'
text = '{{"lvl1"}&{"lvl1"}}|{"lvl0"}&{{"lvl1"}&{{"lvl2"}&{{"lvl3"}&{{"lvl4"}&{{"lvl5"}&{"lvl6"}}}}}}'

x = parser.parse(text)
print(x)
print(x.pretty())

