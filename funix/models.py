from django.db import models
from judge.models.problem_data import ProblemTestCase
from judge.models.problem import Problem
from zipfile import ZipFile


# Create your models here.
class ProblemTestCaseData(models.Model):
    problem_test_case = models.OneToOneField(ProblemTestCase, on_delete=models.CASCADE, related_name='data')
    input_data = models.TextField(verbose_name='input', blank=True)
    output_data = models.TextField(verbose_name='expected output', blank=True)

def save(self, *args, **kwargs):
    super(ProblemTestCase, self).save(*args, **kwargs)
    
    if self.is_pretest == True and ((self.input_file != '' and self.input_file is not None) or (self.output_file != '' and self.output_file is not None)):
        problem = Problem.objects.get(cases=self)
        archive = ZipFile(problem.data_files.zipfile.path, 'r')
        try:
            test_case_data = ProblemTestCaseData.objects.get(problem_test_case=self)
        except ProblemTestCaseData.DoesNotExist:
            test_case_data = ProblemTestCaseData.objects.create(problem_test_case=self)
    
        if self.input_file != '':
            test_case_data.input_data = archive.read(self.input_file).decode('utf-8')
        if self.output_file != '':
            test_case_data.output_data = archive.read(self.output_file).decode('utf-8')
        test_case_data.save()

ProblemTestCase.save = save
del save

