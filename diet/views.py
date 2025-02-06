from django.shortcuts import render, redirect
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
        
        if form.is_valid():
            # Capture form data
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            health_conditions = ", ".join(form.cleaned_data['health_conditions'])
            fitness_goals = ", ".join(form.cleaned_data['fitness_goals'])
            dietary_preferences = ", ".join(form.cleaned_data['dietary_preferences'])
             # Print the selected options in the console
            # print(f"Age: {age}, Weight: {weight}, Height: {height}")
            # print(f"Health Conditions Selected: {''.join(health_conditions)}")
            # print(f"Fitness Goals Selected: {''.join(fitness_goals)}")
            # print(f"Dietary Preferences Selected: {''.join(dietary_preferences)}")
            # Prepare the prompt for the Gemini AI API
            prompt = (
                f"Imagine you are a professional dietitian creating a personalized weekly meal plan for an individual based on the following details:\n"
                f"Age: {age} years, Weight: {weight} kg, Height: {height} cm.\n"
                f"Health Conditions: {health_conditions}.\n"
                f"Fitness Goals: {fitness_goals}.\n"
                f"Dietary Preferences: {dietary_preferences}.\n"
                "Provide a detailed, balanced meal plan for each day of the week, including breakfast, lunch, and dinner. "
                "Each meal should be tailored to the individual's health conditions, fitness goals, and dietary preferences. "
                "Ensure that the meals are nutritious, easy to prepare, and suitable for the individual's specific needs. "
                "Include calorie counts for each meal, and consider hydration tips as well as advice for digestive issues if relevant, focusing on easily digestible foods."
            )

            # Send request to Gemini AI API to generate meal plan
            response = model.generate_content(prompt)
            generated_meal_plan = response.text

            # Store the generated meal plan in session
            request.session['meal_plan'] = generated_meal_plan

            # Redirect to the meal_plan page
            return redirect('meal_plan')
    
    else:
        form = HealthProfileForm()

    return render(request, 'get_started.html', {'form': form})

# Meal plan page view
def meal_plan(request):
    # Retrieve the meal plan from the session
    generated_meal_plan = request.session.get('meal_plan')

    if not generated_meal_plan:
        # Redirect back to get_started if meal plan isn't generated yet
        return redirect('get_started')

    return render(request, 'meal_plan.html', {'meal_plan': generated_meal_plan})
