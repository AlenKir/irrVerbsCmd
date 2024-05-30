import random


class Verb:
    def __init__(self, base_form, translation):
        self.base_form = base_form
        self.translation = translation

    def __str__(self):
        return f"{self.base_form} {self.translation}"


class IrregularVerb(Verb):
    def __init__(self, base_form, translation, past_simple, past_participle):
        super().__init__(base_form, translation)
        self.past_simple = past_simple
        self.past_participle = past_participle

    def __str__(self):
        return (f"{self.base_form} ({self.translation}) " +
                f"{self.past_simple} {self.past_participle}")

    def get_task(self, hide_forms=1):
        forms = ['base_form', 'past_simple', 'past_participle']
        random.shuffle(forms)
        hide_forms = forms[:hide_forms]

        task = []
        solution = []
        for form in ['base_form', 'past_simple', 'past_participle']:
            if form in hide_forms:
                task.append("___")
                solution.append((getattr(self, form)))
            else:
                task.append((getattr(self, form)))

        task.insert(1, f"({self.translation})")

        return " ".join(task), " ".join(solution)
