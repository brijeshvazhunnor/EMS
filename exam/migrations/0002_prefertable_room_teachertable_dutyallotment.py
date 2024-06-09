# Generated by Django 5.0.2 on 2024-02-07 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="preferTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("teacher_id", models.IntegerField()),
                ("exam_id", models.IntegerField()),
                ("date", models.DateField()),
                ("room_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_id", models.IntegerField()),
                ("room_no", models.IntegerField()),
                ("no_of_coloums", models.IntegerField()),
                ("location", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="teacherTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("teacher_id", models.IntegerField()),
                ("dept_id", models.IntegerField()),
                ("name", models.CharField(max_length=40)),
                ("designation", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="dutyAllotment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "exam_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.exam"
                    ),
                ),
                (
                    "room_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.room"
                    ),
                ),
                (
                    "teacher_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exam.teachertable",
                    ),
                ),
            ],
        ),
    ]