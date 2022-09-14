# Enter the first year 2015
# re run the script, Enter the second year as a 2020
year=int(input('Enter a year: '))
if ((year%4==0 and year%100!=0) or year%400==0):
    print('The given year {} is leap'.format (year))
else:
    print('The given year {} is not leap'.format (year))
    
