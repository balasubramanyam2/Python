C =int( input("Enter the centegrade value: "))
def tempconv(cel1):
       return round((32+1.8*cel1), 1)
      
print("The foreign heat equivelant of  " + str(C)+ "degree celcius is"+ str(tempconv(C))+".")