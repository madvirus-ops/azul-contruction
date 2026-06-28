from core.models import CompanyInfo


def company_context(request):
    return {'company': CompanyInfo.objects.first()}
