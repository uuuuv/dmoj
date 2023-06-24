from funix.views.problem import ProblemBeta, ProblemListBeta,ProblemCommentsBeta, ProblemDetailsBeta
from funix.views.problem_data import beta_update_problem_data
from funix.views.submission import abort_submission_beta, SubmissionTestCaseQueryBeta
from django.urls import path, include
from judge.views.widgets import rejudge_submission

urlpatterns = [
    path('/problems', ProblemListBeta.as_view(), name='beta_problem_list'),
    path('/problem/<str:problem>', include([
        path('', ProblemBeta.as_view(), name='beta_problem'), 
        path('/comments', ProblemCommentsBeta.as_view(), name='beta_problem_comments'), 
        path('/submission/<int:submission>', ProblemBeta.as_view(), name='beta_problem'), 
        path('/data', beta_update_problem_data, name='beta_update_problem_data'), 
        # path('/submit', ProblemSubmitBeta.as_view(), name='beta_problem_submit'), 
    ])),
    path('submission/<int:submission>', include([
        path('/abort', abort_submission_beta, name='beta_submission_abort'), 
    ])),
    path('widgets/', include([
        path('rejudge', rejudge_submission, name='beta_submission_rejudge'),
        path('submission_testcases', SubmissionTestCaseQueryBeta.as_view(), name='beta_submission_testcases_query'),
        path('details', ProblemDetailsBeta.as_view(), name='beta_problem_details'),
        ])
    )
]