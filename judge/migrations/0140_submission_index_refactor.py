# Generated by Django 3.2.16 on 2023-02-12 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0139_user_index_refactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='points',
            field=models.FloatField(null=True, verbose_name='points granted'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='result',
            field=models.CharField(blank=True, choices=[('AC', 'Accepted'), ('WA', 'Wrong Answer'), ('TLE', 'Time Limit Exceeded'), ('MLE', 'Memory Limit Exceeded'), ('OLE', 'Output Limit Exceeded'), ('IR', 'Invalid Return'), ('RTE', 'Runtime Error'), ('CE', 'Compile Error'), ('IE', 'Internal Error'), ('SC', 'Short Circuited'), ('AB', 'Aborted')], default=None, max_length=3, null=True, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.FloatField(null=True, verbose_name='execution time'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['problem', 'user', '-points', '-time'], name='judge_submi_problem_8d5e0a_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['result', '-id'], name='judge_submi_result_7a005c_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['result', 'language', '-id'], name='judge_submi_result_ba9a62_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['language', '-id'], name='judge_submi_languag_dfe850_idx'),
        ),
    ]
