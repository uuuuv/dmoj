import traceback

from django.shortcuts import render
from django.utils.translation import gettext as _


def error(request, context, status):
    return render(request, 'error.html', context=context, status=status)


def error404(request, exception=None):
    if request.user.is_superuser:
        # TODO: "panic: go back"
        return render(request, 'generic-message.html', {
            'title': _('404 error'),
            'message': _('Could not find page "%s"') % request.path,
        }, status=404)
        
    return render(request, 'funix/404.html', status=404)


def error403(request, exception=None):
    if request.user.is_superuser:
        return error(request, {
            'id': 'unauthorized_access',
            'description': _('no permission for %s') % request.path,
            'code': 403,
        }, 403)

    return render(request, 'funix/403.html', status=403)

def error500(request):
    if request.user.is_superuser:
        return error(request, {
            'id': 'invalid_state',
            'description': _('corrupt page %s') % request.path,
            'traceback': traceback.format_exc(),
            'code': 500,
        }, 500)
    
    return render(request, 'funix/500.html', status=500)
