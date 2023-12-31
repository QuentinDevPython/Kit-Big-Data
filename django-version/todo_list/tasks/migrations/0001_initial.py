"""Migrated model."""
# Generated by Django 4.0 on 2023-10-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Migration class."""

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                (
                    "title",
                    models.CharField(blank=True, max_length=200, null=True),
                    ),
                ("description", models.TextField(blank=True, null=True)),
                ("complete", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.user",
                    ),
                ),
            ],
            options={
                "ordering": ["complete"],
            },
        ),
    ]
