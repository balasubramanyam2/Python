#upper lower cases of strings
A = "A Song of Ice and Fire"
print(A.isupper())
print(A.islower())
print(A.upper())
print(A.lower())
print(A.title())
B=A.title()
print(B)
print(A.startswith("A"))
print(A.endswith("e"))
C = A.split()
print(C)
print(" ".join(C).isalpha)

#Left adjust, Right adjust, center adjust
print("Hello World".rjust(15))
print("Hello world".ljust(15))
print("Hello world".center(15))

#Strip of string
print("You are my best friend best".strip("best"))
print("You you are my best friend best".lstrip("You"))
print("You are my best friend best".rstrip("best"))
print("good morning".replace("morning", "afternoon"))

#Length of string
print(len("whwn are you coming from India"))
