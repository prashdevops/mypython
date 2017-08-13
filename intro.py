# This is my first python program and This is Intrduction
# Developed by Prash.DevOps
my_message = 'Hello Word'
my_custom_message = 'Prash\'s Custom Message'
my_custom_message_one = "Prash's Second Message"
my_custom_message_multiline = """ Hi , Here is my example of custom variables
   which is having multilines """
print(my_message)
print(my_custom_message)
print(my_custom_message_one)
print(my_custom_message_multiline)
print(len(my_custom_message))
print(my_custom_message[0])
#print(my_custom_message[24])
print(my_custom_message[0:21])
print(my_custom_message[:22])
print(my_custom_message[0:])
print(my_custom_message.lower())
print(my_custom_message.upper())
print(my_custom_message.count('a'))
print(my_custom_message.find('P'))
my_replace_variable = my_custom_message.replace('Prash','DevOPS')
print(my_replace_variable)

greet = 'Hello'
name = 'Prash DevOPS'
mygreet = greet + ' warm ' +  name
print(mygreet)
mymessage = 'Welcome {}, {} '.format (greet, name)
print(mymessage)
#print(dir(my_custom_message))
