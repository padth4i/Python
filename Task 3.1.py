s1=str(input("Input the 1st string: "))

s2=str(input("Input the 2nd string: "))

s3=str(input("Input the 3rd string: "))

s4=str(input("Input the 4th string: "))

s5=str(input("Input the 5th string: "))

s6=str(input("Input the 6th string: "))

s7=str(input("Input the 7th string: "))

s8=str(input("Input the 8th string: "))

s9=str(input("Input the 9th string: "))

s10=str(input("Input the 10th string: "))

s11=str(input("Input the 11th string: "))

s12=str(input("Input the 12th string: "))

sa=s1+s2+s3

sb=sa+s4+s5+s6

sc=sb+s7+s8+s9

sd=sc+s10+s11+s12

srev=''.join(reversed(sd))


if sd==srev :

   print("\nIt is a palindrome")

else:

   print ("\nIt is not a palindrome")