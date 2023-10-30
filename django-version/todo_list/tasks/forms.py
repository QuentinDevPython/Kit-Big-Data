"""Forms for the tasks."""

from django import forms


class PositionForm(forms.Form):
    """A Django Form class for capturing position information."""

    position = forms.CharField()
