from django import forms

class HealthProfileForm(forms.Form):
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'input-field'}))
    weight = forms.IntegerField(label='Weight (kg)', widget=forms.NumberInput(attrs={'class': 'input-field'}))
    height = forms.IntegerField(label='Height (cm)', widget=forms.NumberInput(attrs={'class': 'input-field'}))

    health_conditions = forms.MultipleChoiceField(
        choices=[
            ('Healthy', 'Healthy'), 
            ('Heart Diseases', 'Heart Diseases'), 
            ('High BP/Diabetes', 'High BP/Diabetes'),
            ('Thyroid Issues', 'Thyroid Issues'),
            ('Cholesterol', 'Cholesterol'),
            ('PCOS/PCOD', 'PCOS/PCOD'),
            ('Digestive Disorders', 'Digestive Disorders'),
            ('Respiratory Issues', 'Respiratory Issues')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    fitness_goals = forms.MultipleChoiceField(
        choices=[
            ('Weight Loss', 'Weight Loss'), 
            ('Muscle Gain', 'Muscle Gain'), 
            ('Maintenance', 'Maintenance'),
            ('Improve Endurance', 'Improve Endurance'),
            ('Increase Flexibility', 'Increase Flexibility'),
            ('Recovery', 'Recovery'),
            ('Body Toning', 'Body Toning'),
            ('Improve Metabolism', 'Improve Metabolism')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    dietary_preferences = forms.MultipleChoiceField(
        choices=[
            ('Vegetarian', 'Vegetarian'), 
            ('Non-Vegetarian', 'Non-Vegetarian'), 
            ('Keto', 'Keto'),
            ('Vegan', 'Vegan'),
            ('Paleo', 'Paleo'),
            ('Gluten-Free', 'Gluten-Free'),
            ('Mediterranean', 'Mediterranean'),
            ('Pescatarian','Pescatarian')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    meal_preferences = forms.MultipleChoiceField(
        choices=[
            ('Three Meals a Day', 'Three Meals a Day'), 
            ('Small Frequent Meals', 'Small Frequent Meals'), 
            ('Intermittent Fasting', 'Intermittent Fasting'),
            ('Balanced Macro Diet', 'Balanced Macro Diet'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

