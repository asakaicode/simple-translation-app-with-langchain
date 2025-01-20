from django.shortcuts import get_object_or_404, render

from translation.models import Translation


def index(request):
    translations = Translation.objects.all()
    context = {
        'translations': translations,
    }

    return render(request, 'translation/index.html', context)


def detail(request, translation_id):
    translation = get_object_or_404(Translation, pk=translation_id)

    return render(request, "translation/detail.html", {"translation": translation})
