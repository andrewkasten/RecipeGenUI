from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional
from .models import Preferences

import os



class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")


class Recipe(BaseModel):
    reasoning: str = Field(description="Based on produce season and pricing")
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]
    
    
class GemService:
    @staticmethod 
    def generate_recipe(city_state, type):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        prompt = f"Please provide a simple recipe that is good based on produce season and pricing for {Preferences.city_state} and preference: {Preferences.type}"
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_json_schema": Recipe.model_json_schema(),
            },
        )
        recipe = Recipe.model_validate_json(response.text)
        print(recipe)
        return recipe



# class GemService:
#     @staticmethod 
#     def generate_text(input):
#         client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=input
#             )
#         print(response.text)
#         return response.text
    

#"Tell me a short joke about programming."


# decision about recipe 
# Input
#   Area
#   Type
# Output 
#   reason
#   recipe_name
#   prep_time
#   ingredients
#   instructions 


#Search and filtering. Most e-commerce and content sites still use keyword-matching search. AI-powered semantic search (where "comfortable work shoe under $100" actually works)

#Contextual help
# what is a suggestions based on 

#content summarization

#Accessibility assistance. AI-generated alt text, plain-language rewrites of complex content, dynamic font/contrast adjustments based on user behavior — the tech is there but adoption is very low.

#Scheduling and coordination. Finding a meeting time across multiple people, suggesting optimal times based on patterns — still mostly manual even with tools like Calendly. The AI layer is thin.

# Nudges over automation. Instead of AI writing your email, it flags that your tone reads harsher than usual, or that you forgot to answer a question from the previous thread. The human still writes — AI just catches blind spots.

# Decision scaffolding. A budgeting app where AI doesn't auto-categorize your spending but instead asks "you spent $340 at restaurants this week — want to set a target?" It surfaces patterns and prompts reflection rather than making choices.

# Learning reinforcement. Instead of generating flashcards for you, AI notices which concepts you keep getting wrong and adjusts the spacing/difficulty. It shapes the practice without replacing the thinking. (This is basically what your teacher-cs skill does.)

# Draft critique, not draft generation. Upload a cover letter or resume and AI highlights weak spots, vague language, or missing keywords for a specific job posting — but doesn't rewrite it. Preserves voice while improving quality.

# Ambient awareness dashboards. AI that monitors data (website analytics, fitness metrics, project velocity) and only surfaces things when something is unusual. Not "here's your daily report" but "hey, traffic from organic search dropped 40% this week — here's where."

# Guided troubleshooting. Instead of AI fixing your code or config, it asks diagnostic questions like a good senior dev would. "Does the error happen on every request or just POST? Have you checked if the middleware is running?" Builds the user's debugging muscle.