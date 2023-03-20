from django import template
from ..example import SPISOK, PUN
from ..models import Post, User, PostCategory
from django.contrib.auth.models import User


register = template.Library()
@register.filter()
def censor(value):
        value = list(map(str, value.split()))
        content = []
        for word in value:
            if word.startswith(PUN) and word.endswith(PUN):
                if (word.lower()[1:-1]) in SPISOK:
                    le = len(word) - 4
                    word = f"{word[0]}{word[1]}{'*' * le}{word[-2]}{word[-1]}"
                    content.append(word)
                else:
                    content.append(word)
            elif word.startswith(PUN):
                if (word.lower()[1:]) in SPISOK:
                    le = len(word) - 3
                    word = f"{word[0]}{word[1]}{'*' * le}{word[-1]}"
                    content.append(word)
                else:
                    content.append(word)
            elif word.endswith(PUN):
                if (word.lower()[0:-1]) in SPISOK:
                    le = len(word) - 3
                    word = f"{word[0]}{'*' * le}{word[-2]}{word[-1]}"
                    content.append(word)
                else:
                    content.append(word)
            else:
                if (word.lower()) in SPISOK:
                    le = len(word) - 2
                    word = f"{word[0]}{'*' * le}{word[-1]}"
                    content.append(word)
                else:
                    content.append(word)
        return f"{(' '.join(content))}"
    #
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

@register.filter()
def scribe(value):
    cat_id = PostCategory.value('category_id')
    user_id = cat_id
    print(cat_id)
    for list in value:
        if 'category_current_id' in list and list['category_current_id'] == cat_id:
            print('ok')
            if 'user_current_id' in list and list['user_current_id'] == user_id:
                return True