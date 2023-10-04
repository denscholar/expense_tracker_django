# Generated by Django 4.2.4 on 2023-10-03 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("expenses", "0002_alter_category_options_alter_expense_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="expenses.category"
            ),
        ),
    ]