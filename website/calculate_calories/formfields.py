from django import forms


class ChoiceField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        self.blank_choice = kwargs.pop('blank_choice', None)
        super(ChoiceField, self).__init__(*args, **kwargs)

    def _get_choices(self):
        return self._choices

    def _set_choices(self, value):
        choices = list(value)
        if self.blank_choice:
            choices = [('', self.blank_choice)] + choices
        self._choices = self.widget.choices = choices

    choices = property(_get_choices, _set_choices)