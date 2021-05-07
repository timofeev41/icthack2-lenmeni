from django.db import models

class Tasks(models.Model):
    TASK_STATUS = (
        ("OK", "Completed"),
        ("PR", "In progress"),
        ("NS", "Not started yet")
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=60)
    status = models.CharField(max_length=2, choices=TASK_STATUS)
    progress = models.CharField(max_length=3)
    startdate = models.DateTimeField(auto_now=True)
    completedate = models.DateTimeField(max_length=30)

    def __str__(self) -> str:
        return f"#{self.id}: {self.title}"
