#variables

a = []
enter = ''
ex = ''

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
       
#####        
        
while True:

    print(sex)
    enter = input()
    a.append(enter)
    

    print(segment)
    enter = input()
    a.append(enter)
    if a == ['male', 'hands'] or a == ['male', 'legs'] or a == ['female', 'hands'] or a == ['female', 'legs']:
        print(surgeon)
        ex = 1
    if ex == 1:
        break
    
    print(part)
    enter = input()
    a.append(enter)
    if a == ['male','head', 'forehead'] or a == ['female', 'head', 'forehead']:
        print(surgeon)
        ex = 1
    elif a == ['male', 'head', 'nose_ears_throat'] or a == ['female', 'head', 'nose_ears_throat']:
        print(therapist)
        ex = 1
    elif a == ['male', 'head', 'teeth'] or a == ['female', 'head', 'teeth']:
        print(stomatologist)
        ex = 1
    elif a == ['male', 'head', 'eyes'] or a == ['female', 'head', 'eyes']:
        print(ophthalmologist)
        ex = 1
    elif a == ['male', 'chest', 'heart'] or a == ['female', 'chest', 'heart']:
        print(cardiologist)
        ex = 1
    elif a == ['male', 'chest', 'lungs'] or a == ['female', 'chest', 'lungs']:
        print(surgeon)
        ex = 1
    elif a == ['female', 'chest', 'breast']:
        print(mammologist)
        ex = 1
    if ex == 1 :
        break

    print(part)
    enter = input()
    a.append(enter)
    if a == ['male', 'chest', 'gullet', 'penis']:
        print(urologist)
        ex = 1
    elif a == ['male', 'chest', 'gullet', 'butt'] or ['female', 'chest', 'gullet', 'butt']:
        print(proctologist)
        ex = 1
    elif a == ['female', 'chest', 'gullet', 'vagina']:
        print(venerologist)
        ex = 1
    if ex == 1:
        break
        