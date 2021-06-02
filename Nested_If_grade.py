#nested if
A=int(input("enter the score: "))
if A>=90:
   print("Student scored"+" "+str(A)+" "+"And the student Grade is A")
else:
	   if A>=80 and A<90:
	       print("Student scored"+" "+str(A)+" "+"And the student Grade is B")
	   else:
	      if A>=70 and A<80:
	      	print("Student scored"+" "+str(A)+" "+"And the student Grade is C")
	      else:
   	   	   if A>=60 and A<70:
   	   	   	print("Student scored"+" "+str(A)+" "+"And the student Grade is D")
   	   	   else:
   	   	   		print ("Student scored"+" "+str(A)+" "+"And the student Grade is F")