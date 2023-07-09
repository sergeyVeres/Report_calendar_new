from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Company(models.Model):
    name = models.CharField('название компании',max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="company")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Report(models.Model):
    PERIODS = [
        ('Quarter', (
            ('1st quarter', '1'),
            ('2nd quarter', '2'),
            ('3rd quarter', '3'),
            ('4th quarter', '4'),
        )
         ),
        ('Month', (
            ('january', 'jan'), ('february', 'feb'), ('march', 'mar'),
            ('april', 'apr'), ('may', 'may'), ('june', 'jun'),
            ('july', 'jul'), ('august', 'aug'), ('september', 'sep'),
            ('october', 'oct'), ('november', 'nov'), ('december', 'dec'),
        )
         ),
    ]
    YEARS = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
    )
    NAMES = (
        ('Декларация по НДС', 'НДС'),
        ('Декларация по налогу на прибыль', 'Прибыль'),
        ('Расчет по страховым взносам', 'Взносы'),
        ('Персонифицированные сведения', 'Персонифицированные'),
        ('Уведомление об исчисленных суммах налогов', 'Уведомление'),

    )
    report_name = models.CharField(verbose_name='Название отчета',max_length=100, choices=NAMES)
    year = models.CharField(verbose_name='Год отчета',max_length=100, choices=YEARS)
    period = models.CharField(verbose_name='Период отчета',max_length=100, choices=PERIODS)
    deadline = models.DateField(verbose_name='Срок сдачи', null=True)
    deadline_status = models.BooleanField(default=False)
    done = models.BooleanField(verbose_name='Отчет сдан', default=False)
    comment = models.CharField(verbose_name='Комментарий', max_length=300, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.report_name

    class Meta:
        ordering = ['deadline']






