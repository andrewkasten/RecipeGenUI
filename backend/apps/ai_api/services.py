import httpx
import json
import logging
import os
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date
from google import genai
from google.genai import types
# from PIL import Image  # not needed for recipe card — re-enable + add `pillow` to requirements.txt if a future card does server-side image work
from io import BytesIO

logger = logging.getLogger(__name__)

with open(os.path.join(os.path.dirname(__file__), 'US_Seasonal.json')) as us_seasonal:
    us_seasonal_data = json.load(us_seasonal)

today = date.today()
month = today.strftime("%B")
# Pydantic models define and constrain the AI response.
# Return JSON matching schemas, structured data rather than free-form text.

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    reasoning: str = Field(description="recipe based on preference that also includes produce in season")
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    color: str = Field(description="choose one hex color for this recipe's UI")    # AI picks a hex color
    ingredients: List[Ingredient]
    instructions: List[str]

def pixabay_image(query: str) -> str | None:
    # Returns a photo URL from Pixabay matching the query, or None.
    resp = None
    try:
        resp = httpx.get(
            "https://pixabay.com/api/",
            params={"key": os.getenv("PIXABAY_API_KEY"), "q": query, "image_type": "photo", "per_page": 3},
            timeout=5.0,
        )
        resp.raise_for_status()
        hits = resp.json().get("hits", [])
        return hits[0]["webformatURL"] if hits else None
    except Exception:
        body = resp.text if resp is not None else "<no response>"
        status = resp.status_code if resp is not None else "<no status>"
        logger.warning("pixabay_image failed for query: %s | status=%s body=%s", query, status, body)
        return None

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
    resp = None
    try:
        resp = httpx.get(
        "https://api.calorieninjas.com/v1/nutrition",
        params={"query": query},
        headers={"X-Api-Key": f"{os.getenv('CALORIE_NINJAS_API_KEY')}"},
        )
        print(query)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        print(items)
        return sum(item["calories"] for item in items) if items else None
    except Exception:
        body = resp.text if resp is not None else "<no response>"
        status = resp.status_code if resp is not None else "<no status>"
        logger.warning("calorie ninjas failed for query: %s | status=%s body=%s", query, status, body)
        return None

class GemRecipeService:
    @staticmethod
    def generate_image(recipe_name: str):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        prompt = f"Create a picture of this recipe: {recipe_name}"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=prompt,
        )
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save("recipe_image.png")
                return image
        return None

    def generate_recipe(state, type):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        produce = us_seasonal_data[state][month]

        # Sample a small subset so Gemini treats produce as inspiration, not a checklist
        import random
        seasonal_hint = random.sample(produce, min(8, len(produce))) if produce else []

        # Prompt anchors on a familiar dish for the meal type; produce is a soft hint, not a requirement
        prompt = (
            f"Suggest a single-serving {type} recipe that a typical home cook would recognize "
            f"(e.g., for lunch: sandwich, soup, grain bowl, pasta, wrap, salad, etc.). "
            f"The dish should make sense on its own — do NOT force ingredients in. "
            f"If — and only if — it fits naturally, you may feature 1 or 2 of these in-season items "
            f"as a side, garnish, or substitution: {seasonal_hint}. "
            f"Otherwise ignore the list entirely."
        )
        print(prompt)
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
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
        recipe_dict["image"] = pixabay_image(recipe.recipe_name)

        query = ",".join(f"{i['name']} {i['quantity']}" for i in recipe_dict['ingredients'])
        recipe_dict["calories"] = calorie_ninjas(query)

        return recipe_dict







# for m in client.models.list():
#     print(m.name)
# models/gemini-2.5-flash
# models/gemini-2.5-pro
# models/gemini-2.0-flash
# models/gemini-2.0-flash-001
# models/gemini-2.0-flash-lite-001
# models/gemini-2.0-flash-lite
# models/gemini-2.5-flash-preview-tts
# models/gemini-2.5-pro-preview-tts
# models/gemma-4-26b-a4b-it
# models/gemma-4-31b-it
# models/gemini-flash-latest
# models/gemini-flash-lite-latest
# models/gemini-pro-latest
# models/gemini-2.5-flash-lite
# models/gemini-2.5-flash-image
# models/gemini-3-pro-preview
# models/gemini-3-flash-preview
# models/gemini-3.1-pro-preview
# models/gemini-3.1-pro-preview-customtools
# models/gemini-3.1-flash-lite-preview
# models/gemini-3.1-flash-lite
# models/gemini-3-pro-image-preview
# models/nano-banana-pro-preview
# models/gemini-3.1-flash-image-preview
# models/lyria-3-clip-preview
# models/lyria-3-pro-preview
# models/gemini-3.1-flash-tts-preview
# models/gemini-robotics-er-1.5-preview
# models/gemini-robotics-er-1.6-preview
# models/gemini-2.5-computer-use-preview-10-2025
# models/deep-research-max-preview-04-2026
# models/deep-research-preview-04-2026
# models/deep-research-pro-preview-12-2025
# models/gemini-embedding-001
# models/gemini-embedding-2-preview
# models/gemini-embedding-2
# models/aqa
# models/imagen-4.0-generate-001
# models/imagen-4.0-ultra-generate-001
# models/imagen-4.0-fast-generate-001
# models/veo-2.0-generate-001
# models/veo-3.0-generate-001
# models/veo-3.0-fast-generate-001
# models/veo-3.1-generate-preview
# models/veo-3.1-fast-generate-preview
# models/veo-3.1-lite-generate-preview
# models/gemini-2.5-flash-native-audio-latest
# models/gemini-2.5-flash-native-audio-preview-09-2025
# models/gemini-2.5-flash-native-audio-preview-12-2025
# models/gemini-3.1-flash-live-preview
