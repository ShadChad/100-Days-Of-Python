"""Metacharacters in regular expressions
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs"""


import re


# pattern = "was"
pattern = r"[A-Z]yclone"
text = '''Cyclone Dumazile was a strong tropical Dyclone in the South-West
Indian Ocean that affected Madagascar and Réunion in early March 2018.
Dumazile originated from a low-pressure area that formed near
Agaléga on 27 February. It became a tropical disturbance on 2
March, and was named the next day after attaining tropical
storm status. Dumazile reached its peak intensity on 5 March,
with 10-minute sustained winds of 165 km/h (105 mph),
 1-minute sustained winds of 205 km/h (125 mph), 
 and a central atmospheric pressure of 945 hPa (27.91 inHg).
 As it tracked southeastwards, Dumazile weakened steadily over 
 the next couple of days due to wind shear, and became a post-tropical
 cyclone on 7 March before completely dissipating on 10 March. Dumazile dropped 
 torrential rainfall in Réunion and Madagascar—reaching 1,600 mm (63 in) in Salazie 
 and 210 mm (8.3 in) in northeastern Madagascar—causing widespread flooding and damaging 
 crops and infrastructure. Two deaths were caused by Dumazile, both in Madagascar.'''



# match = re.search(pattern,text)
# print(match)


matches = re.finditer(pattern,text)

for match in matches:
    # print(match)
    print(match.span())
    print(type(match.span())) #willl return tuple

    print(text[match.span()[0]:match.span()[1]])

# Searching for a pattern in re using re.search() Method
# define a regular expresssion pattern
pattern1= r"expression"

# match the pattern against a string
text1 = "hello world"

match1 = re.search(pattern1,text1)


if match1:
    print("match found!")

else:
    print("match not found")


# earching for a pattern in re using re.findall() Method
pattern2 = r"[a-z]+at"
text2 = "the cat is in the hat"

matches1 = re.findall(pattern2,text2)
print(matches1)

# Replacing a pattern

new_text = re.sub(pattern2,"dog",text2)

print(new_text)


# Extracting information from a string

text3 = "the email address is example@example.com"

pattern3 = r"\w+@\w+\.\w+"

match2 = re.search(pattern3,text3)

if match:
    email = match.group()
    print(email)



