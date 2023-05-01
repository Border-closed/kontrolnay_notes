import csv
import os

# Ввод режима работы пользователем
def mode_start ():
    m_s = input('Доступные режимы работы с заметками: \nввод заметки - 1 \nвывод всех заметок - 2 \nвывод заметки, созданной в конкретную дату - 3 \nредактирование заметки - 4 \nудаление заметки - 5 \nВведите режим работы: \n')
    return m_s

# Ввод название заметки пользователем
def print_head_note ():
    data = input('Введите название заметки: ')
    return data

# Ввод текста заметки пользователем
def print_note ():
    data = input('Введите текст заметки: ')
    return data

# Ввод даты пользователем для фильтрации
def print_date ():
    date = input('Введите дату для поиска заметки в формате YYYY-MM-DD: ')
    return date

# Определение структуры  csv файла
fields = ['id', 'head', 'note', 'creation time', 'change time']

# Запись заметки в файл csv
def inp (x):
    with open ('notes.csv', 'a', newline='') as inp_notes:
         fields = ['id', 'head', 'note', 'creation time', 'change time']
         writer = csv.DictWriter(inp_notes, fields)
         writer.writerow(x) 
         inp_notes.close()

# Вывод списка заметок из файла
def out ():
    with open('notes.csv', 'r', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
        File.close()

# Вывод отфильтрованной по дате создания заметки из файла
def out_one (x):
    with open('notes.csv', 'r', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            if x in row[3]:
                print(row)
        File.close()

# Удаление заметки по названию/телу или дате создания заметки
def delet (x):
    input = open ('notes.csv', 'r')
    output = open('notes_after_del.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if x not in row[1] and x not in row[2]:
            writer.writerow(row)
    input.close()
    output.close()
    os.rename('notes_after_del.csv', 'notes.csv')

# Редактирование заметки
def change (x, d):
    input = open ('notes.csv', 'r')
    output = open('notes_after_change.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if x not in row[1] and x not in row[2]:
            writer.writerow(row)
        else:
            writer.writerow(d)
    input.close()
    output.close()
    os.rename('notes_after_change.csv', 'notes.csv')

# Ввод текста заголовка или заметки для поиска, чтобы дальше удалить
def search ():
    sch = input('Введите текст для поиска в заголовке или тексте заметки ')
    return sch

# Проверка наличия такой заметки в файле
def search_note (x):
    input = open ('notes.csv', 'r')
    count = 0
    for row in csv.reader(input):
        if x in row[1] or x in row[2]:
            count = count + 1
    input.close()
    return count

# Определение id для изменяемой заметки
def id_note (x):
    input = open ('notes.csv', 'r')
    id = 0
    for row in csv.reader(input):
        if x in row[1] or x in row[2]:
            id = row[0]
    input.close()
    return id

# Определение create_time для изменяемой заметки
def create_time_f (x):
    input = open ('notes.csv', 'r')
    time = 0
    for row in csv.reader(input):
        if x in row[1] or x in row[2]:
            time = row[3]
    input.close()
    return time

# Определение количества строк в csv
def count_csv ():
    with open('notes.csv', 'r', newline='') as File:  
        reader = csv.reader(File, delimiter=' ', quotechar='|')
        count = 0
        for row in reader:
            count = count +1
        File.close()
    return count