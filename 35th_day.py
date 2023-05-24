import random
import string

print("Hi, this is EncoderAndDecoder!")
endc = input("\n\nDo you want to Encode(E) or Decode?(D).\nPlease Enter either E or D.").upper()
if (endc=='E'):
# for encoding
    code = input("\nPlease enter the code:")
    length = len(code)
    codelist = list(code)
    if (length>=3):
        
        firstchar = code[0]
        # print(firstchar)
        codelist.append(firstchar)
        codelist.pop(0)
        # print(' '.join(codelist))


        character_set = string.ascii_letters.lower()
        lastchar = (''.join(random.choice(character_set) for i in range(3)))
        codelist.append(lastchar)
        firstchar = (''.join(random.choice(character_set) for i in range(3)))
        codelist = [firstchar] + codelist
        codelist = ''.join(codelist)
        print("the encoded code is: ",codelist)

    else:
    #     reverse = ''
    #     for i in codelist(length-1,0,-1):
    #         result = result + codelist[i]
    # print(result)
        reverse = reversed(code)
        #  print(' '.join(reverse))

        print("".join(reverse))
elif(endc == 'D'):
# for decoding
    decode = input("Enter the code to decode:")
    decodelist = list(decode)
    if len(decode)<3:
        reverse1 = reversed(decode)
        print(''.join(reverse1))
    else:
        # to remove firsts letter
        for i in range(3):
            i = 0
            # print(decodelist[i])
            del decodelist[i]
        # to remove last leters
        for i in range(3):
            i = -1
            del decodelist[-1]


        letter = decodelist[-1]
        decodelist.insert(0,letter)

        
        del decodelist[-1]
        decodelist = ''.join(decodelist)
        print("the decoded code is: ",decodelist)

print('program ended')

#sandip -  
# asdandipshjg







