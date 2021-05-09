from django.db import models
from django.contrib import admin
from django.core import validators

from multiselectfield import MultiSelectField


class Project(models.Model):
    TASK_STATUS = (("Completed", "Completed"), ("In progress", "In progress"), ("Not started yet", "Not started yet"))
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=60)
    status = models.CharField(max_length=40, choices=TASK_STATUS)
    progress = models.IntegerField(validators=[validators.MaxValueValidator(limit_value=100), validators.MinValueValidator(limit_value=0)])
    startdate = models.DateTimeField(auto_now=True)
    completedate = models.DateTimeField(max_length=30)
    description = models.CharField(max_length=100, default="Краткое описание проекта")
    customer = models.CharField(max_length=50, default="ICT InfoLab")
    
    boss = models.CharField(max_length=80, default="Тимофеев Н.А.")

    pic_url = models.URLField(max_length=256, default="https://news.itmo.ru/images/news/big/960500.jpg")

    def __str__(self) -> str:
        return f"#{self.id}: {self.title}"


class Person(models.Model):
    USER_STATUS = (
        ("Student", "Student"),
        ("Teacher", "Teacher"),
        ("Mentor", "Mentor"),
        ("Administration", "Administration"),
        ("Customer", "Customer"),
    )
    SKILLS = (
        ("C++", "C++"),
        ("Python", "Python"),
        ("Написание документации", "Написание документации"),
        ("C#", "C#"),
        ("Java", "Java"),
        ("Лонг айленд", "Kotlin"),
        ("Монтаж видео", "Монтаж"),
        ("JavaScript", "JS"),
        ("IOS-разработка", "IOS-разработка"),
        ("UNIX/Linux", "UNIX подобные системы")
    )
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=USER_STATUS)
    telegram = models.CharField(max_length=60)
    mail = models.EmailField()

    skills = MultiSelectField(choices=SKILLS, max_choices=4, default=None, null=True)
    
    curr_task = models.CharField(max_length=64)
    project = models.ManyToManyField(Project)
    # _curr_project = models.CharField(max_length=64)
    # id_proj = models.ForeignKey(Project, on_delete=models.CASCADE)
    # sorting = Person.objects.filter(groups__name__in=['_curr_project'])

    pic_url = models.URLField(max_length=256, default="https://semantic-ui.com/images/avatar2/large/kristy.png")

    def __str__(self) -> str:
        return f"#{self.id} {self.name} {self.surname} - {self.status}"

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # TODO: по id связать с проектом
    # TODO: вес в процентах
    # TODO: сортировка по весу/дедлайну
    weight = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField(auto_now=True)
    responsible = models.ForeignKey(Person, on_delete=models.PROTECT)
        

    def __str__(self) -> str:
        return f"{self.title} - {self.responsible}"

    @admin.display(boolean=True, ordering="project", description="Проект")
    def task_project(self):
        return self.project

    