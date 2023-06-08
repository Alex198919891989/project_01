 
# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
str = input('введите текст: ')
print ("Исходная строка: " + str) 
remove_exclamation_marks = str.replace('!', '') 
print("Строка после удаления всех символов !: " + remove_exclamation_marks) 
# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
str = input('введите текст: ')
print ("Исходная строка: " + str) 
str = str.removesuffix('!')
print("Строка после удаления одного символа !: " +str)