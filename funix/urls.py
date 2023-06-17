from funix.views.problem import ProblemView 
from funix.views.submission import abort_submission
from django.urls import path, include
from judge.views.widgets import rejudge_submission


urlpatterns = [
    path('/problem/<str:problem>', include([
        path('', ProblemView.as_view(), name='beta_problem'), 
        path('/submission/<int:submission>', ProblemView.as_view(), name='beta_problem'), 
    ])),
    path('submission/<int:submission>', include([
        path('/abort', abort_submission, name='beta_submission_abort'), 
    ])),
    path('widgets/', include([
        path('rejudge', rejudge_submission, name='beta_submission_rejudge'),
        ])
    )
]