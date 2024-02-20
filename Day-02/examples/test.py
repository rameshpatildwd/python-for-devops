##concatinate

str1 = "hello"
str2 = "how are you?"
result = str1 + " " + str2
print(result)

#################

###length

text = "testing"
length = len(text)
print(length)

##################

#lowercase, uppercase

case = "this is to check length"
lowercase = text.lower()
uppercase = text.upper()
print("Uppercase:", uppercase)
print("lowercase:", lowercase)

################################

###replace

text = "This is to check string replacement"
new_text = text.replace("string", "STRING")
print("modified text:", new_text)

#####################

###split

text = "this is to check split function"
word = text.split()
print("words", word)

#############

#substring

text = "This is to check substring"
substring = "check"
if substring in text:
    print(substring, "found in text")


#######################

##Integer

num1 = 10
num2 = 25

addition = num1 + num2
print("Addition:", addition)

substraction = num2 - num1
print("Sub:", substraction)

multiplication = num1 * num2
print("Multiplication:", multiplication)

division = num2 / num1
print("Division:", division)

round = round(3.143278, 3) ##ROUND TO TWO decimals
print("RoundedValue:", round)

################################




