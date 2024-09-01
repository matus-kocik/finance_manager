# Generated by Django 5.0.7 on 2024-09-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="investment",
            name="investment_date",
        ),
        migrations.RemoveField(
            model_name="investmentplan",
            name="planned_investment_date",
        ),
        migrations.AddField(
            model_name="investment",
            name="balance",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=12,
                verbose_name="Current Balance",
            ),
        ),
        migrations.AddField(
            model_name="investment",
            name="goal",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=12,
                verbose_name="Investment Goal",
            ),
        ),
        migrations.AddField(
            model_name="investment",
            name="percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=6,
                verbose_name="Percent Change",
            ),
        ),
        migrations.AddField(
            model_name="investmentplan",
            name="balance",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=12,
                verbose_name="Current Balance",
            ),
        ),
        migrations.AddField(
            model_name="investmentplan",
            name="goal",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=12,
                verbose_name="Investment Goal",
            ),
        ),
        migrations.AddField(
            model_name="investmentplan",
            name="percent_change",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=6,
                verbose_name="Percent Change",
            ),
        ),
    ]
