from main.models import Declaration


def get_all_declarations():
    return Declaration.objects.all()
