#INPUT
inp=input('Europe Floor? ')
try:
    usf=int(inp)+1
    print('US Floor', usf)
    if usf<5:
        print('>> Try taking a higher floor')
    if usf>5:
            print('Welcome to the penthouse')
    if usf==5:
        print('Sweet Heavens')
except:
    print("It's not a number")
print('')

#FOR
for usf in range(5):
    print(usf)
    if usf>2:
        print('Bigger than 2')
    print('Done with usf', usf)
print('Passing to ELIF')

#ELIF
if usf<2:
    print('small')
elif usf<10:
    print('Medium')
else :
    print('LARGE')
print('')

#TRY/EXCEPT
rawstr=input('Enter a number: ')
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print('Good')
else:
    print("That's not a number")

#LOOPS AND ITERATIONS
while ival>0:
    print(ival)
    ival=ival-1
print('ival equals', ival)
print('')

#BREAKING OUT OF THE LOOP
while True:
    line=input('>> ')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('')

for i in [5,4,3,2,1]:
    print(i,' -1')
