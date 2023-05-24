questions = [('Who was the last king of Nepal?\n '),("Who is known as father of computer?\n "),'What is the Tallest peak of the world?\n ','Does CodeWithHarry had his kids yet? ','Who was the winner of the FIFA World Cup 2022? \n']

answers = ['gyanendra shah','charles babbage','mount everest','no','argentina']
desc = ['Y','N']
count = 0
j= 0
for i in range(len(questions)):

    while True: 
        print('\n')   
        
        ques = input(questions[i]).lower()
        print('\n')
        desci = input('Do you want to lock the answer move move forward? Y/N: ').upper()
        if desci == desc[0]:
            
            if ques in answers:
                print("Good Job, It's the right one.")
                count += 100
                print("You've won total of $$",count)
                j += 1
                break
            else:
                
                print('Sorry, It\'s the wrong answer, the correct answer is', answers[j])
                j += 1                
                break
        
    
        
    print("You took total of $$",count,"with you today")
        
    