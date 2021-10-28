
#pretty self explainatory
age = input('What is your age? Please input here:')
age = int(age)
if age >= 100:
    print('wtf')
elif age >= 65:
    print ('Old man')
elif age >= 40:
    print ('Middle age')
elif age >= 18:
    print ('Young man')
elif age >= 0:
    print ('kid')
else:
    print ('wtf are you gay?')



#lets add more calculatiosn
hgt = input ('Thanks for that age, now how tall are you in m:')
hgt = float(hgt)
wgt = input ('And how much you weigh in kg')
wgt = float(wgt)

bmi = wgt / (hgt**2)

if bmi >= 32:
    s = 'FAT FUCK'
elif bmi >= 28:
    s = 'cancer candidate'
elif bmi >= 25:
    s = 'overweighted'
elif bmi >= 18.5:
    s = 'healthy body'
else:
    s = 'underweighted'

print ('your bmi is %.2f, and you are a %s' % (bmi, s))