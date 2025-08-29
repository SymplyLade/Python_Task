from pathlib import Path
import file_ops
def localpath():
    folder = Path('participant_pkg')
    return folder / 'participants.csv'

def participant():
    try:
        dic = {}
        name = input('Enter participant\'s name here: ')
        age = int(input('Enter participant\'s age here: '))
        phone = input('Enter participant\'s phone here: ')
        track = input('Enter participant\'s track here: ')

        if name.isalpha() == False:
            raise ValueError('Name cannot be left empty')
        elif len(phone) != 11:
            raise ValueError('Phone number isn\'t correct')
        elif track.isalpha() == False:
            raise ValueError('Track cannot be left empty')
            super_list.append([name, age, phone, track])
        dic['name'] = name
        dic['age'] = age
        dic['phone'] = phone
        dic['track'] = track

    except ValueError as e:
        print('Error:', e)
    return dic

def participant_list(n):
    path = localpath()
    for i in range(n):
        participant_dic = participant()
        file_ops.save_participant(path, participant_dic)

participant_list(2)



