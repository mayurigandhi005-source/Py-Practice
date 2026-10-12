letter = ''' Dear <|Name|>,
you are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Harry").replace("<|Date|","24 September 2027"))