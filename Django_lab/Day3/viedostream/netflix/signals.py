from netflix.models import Categories

categories = [
    (1, 'action'),
    (2, 'comedy'),
    (3, 'drama'),
    (4, 'romance'),
    (5, 'crime'),
    (6, 'horror')
]


def init_categories(sender, *args, **kwargs):
    for category_instance in categories:
        Categories(id=category_instance[0], status=category_instance[1]).save()
