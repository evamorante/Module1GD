#user_input = input("Enter a sentence : ")
#sentence_length = len(user_input)
#sentence_response = "The lenght of "+user_input+" is "+str(len(user_input))+" caractères."
#print(sentence_response)

def count_characters(limit_number):
    user_sentence = input("Enter a sentence : ")
    print(user_sentence)
    text_length = len(user_sentence)
    message_result = "The lenght of "+user_sentence+" is "+str(text_length)+" characters."
    print(message_result)
    if text_length > limit_number:
        result = 'Attention la limite de ' +  str(limit_number) + ' caractères est dépassée.'
        print(result)
 
count_characters(limit_number=20)
count_characters(limit_number=5)
count_characters(limit_number=10)
