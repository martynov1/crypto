from getpass import getpass
from datetime import date
from hashlib import sha256

access = 0
file = open('pass.txt', 'r')

q1 = sha256(getpass('Какое сегодня число? (введите в формате YYYY-MM-DD)\n>> ').encode()).hexdigest()
if q1 == sha256(str(date.today()).encode()).hexdigest():
    q2 = sha256(getpass('Какой сегодня день недели? (введите число от 0 до 6, где 0-ПН, а 6-ВС)\n>> ').encode()).hexdigest()
    if q2 == sha256(str(date.today().weekday()).encode()).hexdigest():
        q3 = sha256(getpass('В каком городе вы находитесь?\n>> ').upper().encode()).hexdigest()
        if q3 == sha256(('МОСКВА').encode()).hexdigest():
            q4 = getpass('В каком году вы родились?\n>> ')
            q5 = getpass('Сколько Вам лет?\n>> ')
            if int(q5) == date.today().year - int(q4):
                q6 = sha256(getpass('В каком университете вы учитесь?\n>> ').upper().encode()).hexdigest()
                if q6 == sha256(('РТУ').encode()).hexdigest() or q6 == sha256(('РТУ МИРЭА').encode()).hexdigest() or q6 == sha256(('МИРЭА').encode()).hexdigest():
                    q7 = sha256(getpass('В какой группе вы учитесь?\n>> ').upper().encode()).hexdigest()
                    if q7 == sha256(('КТСО-03-15').encode()).hexdigest():
                        print('\nДоступ разрешен!')
                        access = 1
                    else:
                        print('Доступ ЗАПРЕЩЕН!')
                else:
                    print('Доступ ЗАПРЕЩЕН!')
            else:
                print('Доступ ЗАПРЕЩЕН!')
        else:
            print('Доступ ЗАПРЕЩЕН!')
    else:
        print('Доступ ЗАПРЕЩЕН!')
else:
    print('Доступ ЗАПРЕЩЕН!')


if access == 1:
    message = file.read()
    ms = ''
    for i in message:
        ms += i
    print('Зашифрованный текст: ', ms)


