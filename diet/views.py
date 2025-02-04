from django.shortcuts import render

# Landing page view
def home(request):
    return render(request, 'home.html')

def get_started(request):
    if request.method == 'POST':
        # Handle form submission and generate meal plan
        return render(request, 'get_started.html')
    else:
        # Handle GET request to show the form
        return render(request, 'get_started.html')

# Meal plan page view
def meal_plan(request):
    # This is where you display the generated meal plan
    return render(request, 'meal_plan.html', context={'meal_plan': generated_meal_plan})
