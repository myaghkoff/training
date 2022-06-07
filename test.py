print('Is X smaller than 10 or bigger than 20?')
x=5
if x<10:
    print('Smaller')
if x>20:
    print('Bigger')
print('Over')
print('')

n=5
while n>0:
    print(n)
    n=n-1
print('Bim!')
print('')

x=x+3
print(x)
print('')

jj=23%5
print(jj)
kk=4**3
print(kk)
print('')

##LOOPS
print('LOOPS')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('')

largest_num=-1
print('FINDING THE LARGEST VALUE', largest_num)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_num:
        largest_num=the_num
    print(largest_num,the_num)
print('After', largest_num)
print('')

zork=0
print('COUNTING IN A LOOP', zork)
for thing in [9,42,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
print('After',zork)
print('')

zork=0
print('SUMMING IN A LOOP', zork)
for thing in [9,42,12,3,74,15]:
    zork=zork+thing
    print(zork,thing)
print('After',zork)
print('')

count=0
sum=0
print('FINDING THE AVERAGE IN A LOOP', 'count ', count, 'sum ', sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,value,sum)
print('END LOOP RESULTS', count, sum, sum/count)
print('')

print('FILTERING IN A LOOP')
for value in [9,41,12,3,74,15]:
    if value>20:
        print('Numbers greater than 20', value)
print('')


found=False
print('SEARCH USING A BOOLEAN VARIABLE')
for value in [9,41,12,3,74,15]:
    if value==3:
        found=True
        print(found, value)
print('End Loop')
print('')

smallest=None
print('FINDING THE SMALLEST VALUE', smallest)
for the_num in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=the_num
    elif the_num<smallest:
        smallest=the_num
    print('After ', smallest, the_num)
print('')
