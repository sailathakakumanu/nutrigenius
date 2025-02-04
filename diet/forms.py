from django import forms

class HealthProfileForm(forms.Form):
    age = forms.IntegerField()
    weight = forms.IntegerField()
    height = forms.IntegerField()
    health_conditions = forms.MultipleChoiceField(
        choices=[('Healthy', 'Healthy'), ('Heart Diseases', 'Heart Diseases'), ('High BP/Diabetes', 'High BP/Diabetes')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    fitness_goals = forms.MultipleChoiceField(
        choices=[('Weight Loss', 'Weight Loss'), ('Muscle Gain', 'Muscle Gain'), ('Maintenance', 'Maintenance')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    dietary_preferences = forms.MultipleChoiceField(
        choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'), ('Keto', 'Keto')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
