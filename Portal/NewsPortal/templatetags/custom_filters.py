from django import template
from ..example import SPISOK


register = template.Library()
@register.filter()
def censor(value):
        value = list(map(str, value.split()))
        content = []
        for word in value:
            if (word.lower()) in SPISOK:
                le = len(word) - 2
                word = f"{word[0]}{'*'*le}{word[-1]}"
                content.append(word)
                continue
            else:
                content.append(word)

        return f"{(' '.join(content))}"
    #

