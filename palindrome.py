N=input("Enter the string")
reverse = ""
for i in range (len(N) -1, -1, -1):
   reverse += N[i]
print(reverse)

if reverse ==N:
   print("polindrome")
else:
	print("not a polindrome")