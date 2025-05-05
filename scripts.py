from datacenter.models import Schoolkid, Subject, Mark, Lesson, Teacher, Chastisement, Commendation
import random
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import os 


COMMENDATIONS = ["Молодец!", "Отлично!", 
                 "Хорошо!", "Ты меня приятно удивил!", 
                 "Великолепно!", "Прекрасно!", 
                 "Ты меня очень обрадовал!", 
                 "Именно этого я давно ждал от тебя!", 
                 "Очень хороший ответ!", 
                 "Талантливо!", "Ты сегодня прыгнул выше головы!"]


def kid_name(full_name):
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print("Ученик с именем '{full_name}', не найден".)
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с именем "{full_name}". ")
    return None


def fix_marks(schoolkid):
    school_subjects = Subject.objects.filter(title="Математика", year_of_study=6)
    new_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4, subject=school_subjects).update(points=5)
   


def remove_chastisements(schoolkid):
    his_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    his_chastisements.delete()


def create_commendation(schoolkid, child_lessons):
    school_teacher = Teacher.objects.filter(full_name__contains="Котов Флорентин").first()
    school_subjects = Subject.objects.filter(title="Математика", year_of_study=6)
    child_lessons = Lesson.objects.filter(year_of_study=6, 
                                          group_letter="А", 
                                          subject__title="Математика",
                                          date="2019-2-19", 
                                          timeslot=3).first()
    if not child_lessons:
        print("Не найден урок по предмету")
        return None
 
    your_commendation = random.choice(COMMENDATIONS)

    school_commendation = Commendation.objects.create(text=random.choice(COMMENDATIONS), 
                                                      created="2019-2-19", 
                                                      schoolkid=schoolkid, 
                                                      subject=child_lessons, 
                                                      teacher=school_teacher)


def main():
    schoolkid = kid_name("Ваше ФИО")
    if child:
        fix_marks(schoolkid)
        remove_chastisements(schoolkid)
        create_commendation(schoolkid, subject)

if __name__=="__main__":
    main()
