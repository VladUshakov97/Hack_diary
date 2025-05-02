from datacenter import models
from models import Schoolkid
from models import Subject 
from models import Lesson
from models import Teacher 
from models import Chastisement
from models import Commendation
import random

def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains="Ваше ФИО")
    school_subjects = Subject.objects.filter(title="Предмет", year_of_study=6)
    new_marks = Mark.objects.filter(schoolkid=child, points__lt=4, subject=school_subjects)
    for Mark in new_marks:
        new_marks.points = 5
        new_marks.save()


def remove_chastisements(schoolkid):
    child = Schoolkid.objects.get(full_name__contains="Ваше ФИО")
    his_chastisements = Chastisement.objects.filter(schoolkid=child_friends)
    his_chastisements.delete()


def create_commendation("Фролов Иван", "Музыка"):
    child = Schoolkid.objects.get(full_name__contains="Ваше ФИО")
    school_teacher = Teacher.objects.filter(full_name__contains="ФИО учителя").first()
    school_subjects = Subject.objects.filter(title="Предмет", year_of_study=6)
    child_lessons = Lesson.objects.filter(year_of_study=6, 
                                          group_letter="А", 
                                          subject__title="Предмет",
                                          date="2019-1-5", 
                                          timeslot=3).first()
        
    commendations = ["Молодец!", "Отлично!", 
                    "Хорошо!", "Ты меня приятно удивил!", 
                    "Великолепно!", "Прекрасно!", 
                    "Ты меня очень обрадовал!", 
                    "Именно этого я давно ждал от тебя!", 
                    "Очень хороший ответ!", 
                    "Талантливо!", "Ты сегодня прыгнул выше головы!"]

    your_commendation = random.choice(commendations)

    school_commendation = Commendation.objects.create(text=random.choice(commendations), 
                                                      created="2019-1-5", 
                                                      schoolkid=child, 
                                                      subject=child_lessons, 
                                                      teacher=school_teacher)
