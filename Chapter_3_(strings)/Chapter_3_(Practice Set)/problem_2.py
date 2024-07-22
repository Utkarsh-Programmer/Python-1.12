# Problem 2
# write a program to fill in a letter template given below with name and date.

# NOTE: `replace` method is used to replace a specified substring within a string with another specified substring.

letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        '''
print(letter.replace("<|Name|>", "Utkarsh").replace("<|Date|>", "18/6/2027"))
