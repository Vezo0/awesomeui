#variables
a = []
enter = ''
#title text
sex = 'Choose your sex'

segment = 'Which segment of body do you want to inspect?'

part = 'What exactly do you want to inspect?'

surgeon = 'You should go to surgeon. Please, select a suitable day and time for yourself.'

therapist = 'You should go to therapist. Please, select a suitable day and time for yourself.'

stomatologist = 'You should go to stomatologist. Please, select a suitable day and time for yourself.'

ophthalmologist = 'You should go to ophthalmologist. Please, select a suitable day and time for yourself.'

cardiologist = 'You should go to cardiologist. Please, select a suitable day and time for yourself.'

mammologist = 'You should go to mammologist. Please, select a suitable day and time for yourself.'

urologist = 'You should go to urologist. Please, select a suitable day and time for yourself.'

proctologist = 'You should go to proctologist. Please, select a suitable day and time for yourself.'

venerologist = 'You should go to venerologist. Please, select a suitable day and time for yourself.'

#functions
def nex(x, title):
    print(title)
    a.append(x)

def nex2(x):
    a.append(x)
    if a == [1, 1, 1] or a == [2, 1, 1]:
        print(surgeon)
    elif a == [1, 1, 2] or a == [2, 1, 2]:
        print(therapist)
    elif a == [1, 1, 3] or a == [2, 1, 3]:
        print(stomatologist)
    elif a == [1, 1, 4] or a == [2, 1, 4]:
        print(ophthalmologist)
    elif a == [1, 2, 1] or a == [2, 2, 1]:
        print(cardiologist)
    elif a == [1, 2, 2] or a == [2, 2, 2]:
        print(surgeon)
    elif a == [2, 2, 3]:
        print(mammologist)
        
def nex3(x):
    a.append(x)
    if a == [1, 2, 2, 1]:
        print(urologist)
    elif a == [1, 2, 2, 2] or [2, 2, 2, 2]:
        print(proctologist)
    elif a == [2, 2, 2, 1]:
        print(venerologist)
#####        
nex(enter, sex)


nex(enter, segment)
if a == [1, 3] or a == [1, 4] or a == [2, 3] or a == [2, 4]:
    print(surgeon)

nex(enter, part)

nex2(enter)

nex3(enter)