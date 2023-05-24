
user = "500"

nepal_dict = {1: "Ek",5:"Paach",10:"Das",50:"Paachas",100:"Saye",500:"paach saye",1000:"Hajar"}


for i in nepal_dict.keys():
    if (len(user)==3):
        print(nepal_dict[user[0]] + nepal_dict[100])

    elif(len(user)==4):
        print(user[0]+nepal_dict[1000])
        break
