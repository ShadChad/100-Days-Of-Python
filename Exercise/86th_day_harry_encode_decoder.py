while True:
    st = input("enter a message: ")
    words = st.split(" ")
    code = int(input('1 for encoding and 2 for decoding and 0 for quiting the program'))
    if code==1:
        nwords = []
        for word in words:
            # print(word)
            if(len(word)>=3):
                r1 = 'fsd'
                r2 = 'fsd'
                stnew = r1 + word[1:] + word[0] + r2
                # print(stnew)
                nwords.append(stnew)
            else: 
                nwords.append(word[::-1])
        print('your encoded format is:'," ".join(nwords))
    elif(code ==2):
        words = st.split(" ")
        nwords = []
        for word in words:
            if len(word)>=3:
                stnew = word[3:-3] 
                stnew = stnew[-1] + stnew[:-1]
                # print(stnew)
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print('your decoded format is:'," ".join(nwords))
    elif code == 0:
        print("Program quitted")
        break
    else:
        print('error occured')

