from django.db import models

from online_school import settings


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="course_preview/",
        verbose_name="Превью курса",
        null=True,
        blank=True,
    )
    description = models.TextField(max_length=200, verbose_name="Описание", blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец курса", blank=True, null=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    name = models.CharField(max_length=50, verbose_name="Название урока")
    description = models.TextField(max_length=200, verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="lesson_preview/",
        verbose_name="Превью урока",
        null=True,
        blank=True,
    )
    video_link = models.URLField(verbose_name="Видео")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец урока", blank=True, null=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
