#while loop
times=1
while times<=3:
    print(times* "Hello,")
    times=times+1

#lists
counties=['Mombasa','Meru','Kisumu','Eldoret','Kiambu','Nairobi']
cities=['Thika','Kiambu','Nyeri','Muranga','Mtwapa','Bondo']
print(counties)
print(cities[0:3])
counties.insert(2,'embu')
print("Meru" in counties)
print(counties)
print(cities[0:3])
print (len(cities))
name=str(input('enter name : '))
sname=str(input('enter surname : '))
yob=int(input("enter year of birth : "))



age= int(2024- int(yob))
basic= float(int (age)*int(yob)/(int(age)*5))
print("Welcome to G-Tech "+ name.upper()+ ", aged  "+ str(age ) +" years old."
                     "Basic sallary of :\n Ksh "+str(basic.__round__(2)))

print( name.replace(' ',sname).lower()+ ",is aged  "+ str(age ) +" years old."
                     "Basic sallary of :\n Ksh "+str(basic.__round__(2)))
print('j' in name)

#arithmetic operators
print(basic%3)

#comparson oerators
old=age>18
print(old)



#if
if age>=18:
    reason = str(input("Enter: (N) new  or (R) Replacement :\n"))
    print(name.upper()+ name.lower()+" qualifies for a "+ reason+" ID card." )
elif age<18:
    print(name.lower() + " is underage and does not qualify for an ID")
else:
    print("Error!")

print("Check completed.")


