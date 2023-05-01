import data_from_user
from datetime import datetime

def buttom ():
    m_s = data_from_user.mode_start()
    if m_s == '1':
        print()
        head_note = data_from_user.print_head_note()
        print()
        note = data_from_user.print_note ()
        print()
        id = data_from_user.count_csv()+1
        create_time = datetime.now()
        change_time = datetime.now()
        d = {"id" : id, "head" : head_note, "note" : note, "creation time" : create_time, "change time" : change_time}
        data_from_user.inp(d)
        print ('Заметка сохранена\n')
    elif m_s == '2':
        print('\n id | заголовок | текст | время создания | время изменения ')
        data_from_user.out()
        print('Все заметки из файла выведены\n')
    elif m_s == '3':
        print()
        user_date = data_from_user.print_date()
        print('\n id | заголовок | текст | время создания | время изменения ')
        data_from_user.out_one(user_date)
        print(f'Все заметки из файла, созданные {user_date} выведены\n')
    elif m_s == '4':
        print()
        search = data_from_user.search()
        print()
        if data_from_user.search_note(search) > 0:
            head_note = data_from_user.print_head_note()
            print()
            note = data_from_user.print_note ()
            print()
            id = data_from_user.id_note(search)
            create_time = data_from_user.create_time_f (search)
            change_time = datetime.now()
            # new_d = {"id" : id, "head" : head_note, "note" : note, "creation time" : create_time, "change time" : change_time}
            new_d = [id, head_note, note, create_time, change_time]
            # new_d = { change_time, create_time, note, head_note, id}
            data_from_user.change(search, new_d)
            print(f'Заметка изменена\n')
        else:
            print(f'Заметк c текстом {search} нет\n')
    elif m_s == '5':
        print()
        search = data_from_user.search()
        data_from_user.delet(search)
        print(f'Заметка с текстом {search} удалена\n')
    else:
        print('Вы ввели не корректное значение\n')