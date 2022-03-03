#Name: Rebecca Glatts
#Lab 3

#Problem 1
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 > num2 :
   if num1 > num3 :
      print(num1)
   else :
      print(num3)
else :
   if num2 > num3 :
      print(num2)
   else :
      print(num3) 

"""
Testing...
Enter a number: 3
Enter a number: 7
Enter a number: 1
7

prints the largest number of 3 that the user inputs
"""


#Problem 2
count = int(input("please enter number of items purchased"))
total = int(input("please enter the total cost"))
print("Average = ", total/count if count != 0 else "0") 

"""
Testing...
please enter number of items purchased0
please enter the total cost30
Average =  0

please enter number of items purchased3
please enter the total cost30
Average =  10.0

"""

#Problem 3
#(a)
i = 1
while i < 10 :
  print(i, end =  " ")
  i = i + 2
  if i == 5 :
     i = 9
#(b)
for j in range (1, 10, 2) : 
  print(j, end =  " ")
  if j == 5 :
     j = 9
"""
Testing...
(a) 1 3 9
(b) 1 3 5 7 9
"""

#Problem 4
"""
Convert to python 

(a)sum = 0;
for (int x = 1; x <= 20; x++) {
            sum = sum + x;
        }
        System.out.println("Sum: " + sum);
 (b) 
while(true){    
        System.out.println("infinitive while loop");    
    }    
(c) 
System.out.println("Enter a number to check Prime or Not");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int i = 2, count = 0;
        while (i <= number / 2) {
            if (number % i == 0) {
                count++;
                break;
            }
            i++;
        }
        if (count == 0) {
            System.out.println(number + " is prime number");
       } else {
            System.out.println(number + " is not a prime number");
        }
"""
#(a)
sum = 0
for x in range(0, 20, 1):
   sum += x
print("Sum:", sum)
#Testing...
#Sum: 190

#(b)
while True:
   print("infinitive while loop")
#Testing...
#infinitive while loop

#(c)
number = int(input("Enter a number to check if Prime or Not"))
i = 2
count = 0
while i <= (number / 2):
   if number % i == 0:
      count += 1
      break
   i += 1

print(number, "is a prime number" if count==0 else "is not a prime number")
"""
(c)
Testing...
Enter a number to check if Prime or Not37
37 is a prime number

Enter a number to check if Prime or Not35
35 is not a prime number

"""
