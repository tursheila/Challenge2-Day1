year_of_birth=int(input('enter year of birth'))
this_year=2018
age=this_year-year_of_birth
if age<18:
    print ('Minor')
elif age>=18 and age<=36:
    print ('Youth')
else:
    print('Elder')
    