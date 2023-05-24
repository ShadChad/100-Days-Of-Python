class Person:
    name = "aasish"
    occupation = "Software Developer"
    networth = 10
    def info(self): #the objects value goes inside self, hence it prints the specific value which is passeed inside the self
        print(f"{self.name} is a {self.occupation}")
# self means that object  for which the method is called

a = Person()
b = Person()
c = Person()
# a.name = "shubhum" #change the current name to shubhum
# a.occupation = "accountant"
# print(a.name,a.occupation)
a.name = 'shubhum' #overwrites
a.occupation= 'farmer'

b.name = 'hari'
b.occupation = 'accountant'

a.info() #when a.info runs , a goes to self and printst the value of a.name
b.info()
c.info() #prints the default value

