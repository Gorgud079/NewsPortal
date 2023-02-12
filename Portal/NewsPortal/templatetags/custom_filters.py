from django import template
from ..example import SPISOK, PUN


register = template.Library()
@register.filter()
def censor(value):
        value = list(map(str, value.split()))
        content = []
        for word in value:
            print(word)
            if word.startswith(PUN) and word.endswith(PUN):
                print(word.startswith(PUN))
                print(word.endswith(PUN))
                if (word.lower()[1:-1]) in SPISOK:
                    le = len(word) - 4
                    word = f"{word[0]}{word[1]}{'*' * le}{word[-2]}{word[-1]}"
                    content.append(word)
                else:
                    content.append(word)
            elif word.startswith(PUN):
                if (word.lower()[1:-1]) in SPISOK:
                    le = len(word) - 3
                    word = f"{word[1]}{'*' * le}{word[-1]}"
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

