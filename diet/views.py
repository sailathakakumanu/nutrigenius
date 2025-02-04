from django.shortcuts import render
from .forms import HealthProfileForm
import google.generativeai as genai

# Configure Gemini AI API key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Landing page view
def home(request):
    return render(request, 'home.html')

# View to handle form submission and generate the diet plan
def get_started(request):
    if request.method == 'POST':
        form = HealthProfileForm(request.POST)
        
        # If the form is valid, process the data
        if form.is_valid():
            # Capture form data
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            health_conditions = ", ".join(form.cleaned_data['health_conditions'])
            fitness_goals = ", ".join(form.cleaned_data['fitness_goals'])
            dietary_preferences = ", ".join(form.cleaned_data['dietary_preferences'])
            
            # Prepare the prompt for the Gemini AI API
            prompt = (
                f"Generate a personalized diet plan based on the following details: "
                f"Age: {age}, Weight: {weight} kg, Height: {height} cm, "
                f"Health Conditions: {health_conditions}, Fitness Goals: {fitness_goals}, "
                f"Dietary Preferences: {dietary_preferences}. "
                "Provide a meal plan for a week with breakfast, lunch, and dinner for each day."
            )
            
            # Send request to Gemini AI API to generate meal plan
            response = model.generate_content(prompt)
            
            # Extract the generated meal plan from the response
            generated_meal_plan = response.text

            # Pass the generated meal plan to the meal plan page
            return render(request, 'meal_plan.html', {'meal_plan': generated_meal_plan})

    else:
        # Display the form if the request is GET
        form = HealthProfileForm()

    return render(request, 'get_started.html', {'form': form})

# Meal plan page view
def meal_plan(request):
    # This is where you display the generated meal plan
    return render(request, 'meal_plan.html', context={'meal_plan': generated_meal_plan})
