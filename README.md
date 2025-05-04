# Взлом электронного дневника
### Описание
Этот скрипт позволяет:
* Улучшить плохие оценки
* Удалить выговоры
* Добавить похвалу по предмету

### Требования
* Python 3.8+
* Django 3.2+
* Проект электронного дневника с моделями:
  Schoolkid, Mark, Lesson, Teacher, Subject,
  Chastisement, Commendation

### Установка
1. Убедитесь, что у вас установлен Python и Django:
```
python --version
pip install django
```
2. Подключитесь к проекту электронного дневника.
3. Поместите файл scripts.py в корень проекта (рядом с manage.py).

### Использование
1. Запустите сервер:
```
python manage.py runserver
```
2. Откройте Django shell:
```
python manage.py shell
```
3. Импортируйте функции scripts.py
```
from datacenter.scripts import fix_marks, remove_chastisements, create_commendation
```
4. Запустите нужную функцию, указав ФИО ученика и (для похвалы) название предмета:
```
fix_marks("Ваше ФИО")
remove_chastisements("Ваше ФИО")
create_commendation("Ваше ФИО", "Предмет")
```
 
