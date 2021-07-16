
A=int(input('คะแนนเก็บ ='))
B=int(input('คะแนนสอบกลางภาค ='))
C=int(input('คะแนนสอบปลายภาค ='))
Z=A+B+C
if (80<=Z<=100) : 
   print("A")
elif (75<=Z<=79) :
   print("B+")
elif (70<=Z<=74) : 
   print("B")
elif (65<=Z<=69) :
   print("C+")
elif (60<=Z<=64) : 
   print("C")
elif (55<=Z<=59) :
   print("D+")
elif (50<=Z<=54) : 
   print("D")
elif (0<=Z<=49) :
   print("F")