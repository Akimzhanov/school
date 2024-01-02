# Generated by Django 4.2.7 on 2023-11-30 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_remove_user_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tariff",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("price", models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="tariff_price",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="tariff",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tariff",
                to="student.tariff",
            ),
        ),
    ]
