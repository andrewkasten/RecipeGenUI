import httpx
import json
import logging
import os
from typing import List, Optional
from google import genai
from pydantic import BaseModel, Field
from datetime import date

logger = logging.getLogger(__name__)

with open(os.path.join(os.path.dirname(__file__), 'US_Seasonal.json')) as us_seasonal:
    us_seasonal_data = json.load(us_seasonal)

today = date.today()

# Pydantic models define and constrain the AI response.
# Return JSON matching schemas, structured data rather than free-form text.

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")


class Recipe(BaseModel):
    reasoning: str = Field(description="Based on produce season for area and type preferences")
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    color: str = Field(description="choose one hex color for this recipe's UI")    # AI picks a hex color
    ingredients: List[Ingredient]
    instructions: List[str]


def unsplash_image(query: str) -> str | None:
    try:
        resp = httpx.get(
            "https://api.unsplash.com/search/photos",
            params={"query": query, "per_page": 1, "orientation": "landscape"},
            headers={"Authorization": f"Client-ID {os.getenv('UNSPLASH_ACCESS_KEY')}"},
            timeout=5.0,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        return results[0]["urls"]["regular"] if results else None
    except Exception:
        logger.warning("unsplash_image failed for query: %s", query)
        return None


def calorie_ninjas(query: str) -> str | None:
    try:
        resp = httpx.get(
        "https://api.calorieninjas.com/v1/nutrition",
        params={"query": query},
        headers={"X-Api-Key": f"{os.getenv('CALORIE_NINJAS_API_KEY')}"},
        )
        resp.raise_for_status()
        items = resp.json().get("items", [])
        return sum(items["calories"]) if items else None
    except Exception:
        logger.warning("calorie ninjas failed for query: %s", query)
        return None

class GemRecipeService:
    @staticmethod
    def generate_recipe(state, type):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        state = us_seasonal_data[state]

        # Prompt includes location and preference so Gemini can factor in the produce in season
        prompt = f"Please provide a simple recipe based on produce in season, plus staples, for month, {today}, within {state} and preference: {type}"
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            config={
                # Forces the response to be valid JSON matching our Recipe schema
                "response_mime_type": "application/json",
                "response_json_schema": Recipe.model_json_schema(),
            },
        )
        # Validate and parse the raw JSON string into a typed Recipe object
        recipe = Recipe.model_validate_json(response.text)
        recipe_dict = recipe.model_dump()
        recipe_dict["image"] = unsplash_image(recipe.recipe_name)
        # recipe_dict["calories"] = calorie_ninjas(recipe_dict['ingredients']['name'],recipe_dict['ingredients']['quantity'])
        return recipe_dict






