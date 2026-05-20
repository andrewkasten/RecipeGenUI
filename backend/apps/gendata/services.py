import httpx
import json
import logging
import os
from pydantic import BaseModel, Field
from google import genai
import random
from typing import List, Optional


logger = logging.getLogger(__name__)

with open(os.path.join(os.path.dirname(__file__), 'US_Seasonal.json')) as us_seasonal:
    us_seasonal_data = json.load(us_seasonal)



names = ["Michael", "Jessica", "Joshua", "Ashley", "Matthew", "Amanda"]
random_name = random.choice(names)

# Pydantic models define and constrain the AI response.
# Return JSON matching schemas, structured data rather than free-form text. 

#wiki list
#choices 

def wikipedia(query: str) -> str | None:
    
    try:
        resp = httpx.get(
            "https://api.unsplash.com/search/photos",
           
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        return results[0]["urls"]["regular"] if results else None
    except Exception:
        logger.warning("unsplash_image failed for query: %s", query)
        return None


class Style(BaseModel):
    # variant
    # mood
    # layout
  

    variant: str = Field(description="primary choice of theme fitting the animal")
    secondary: str = Field(description="secondary choice of theme fitting the animal")
    score: Optional[int] = Field(description="between 0.0 and 1.0 confidence score of choice for primary")

class Explanation(BaseModel):
    explain: str = "small paragraph explaining this animal at a 5th grade level."
    interesting_fact: str = "share an interesting fact about this animal"

class Output(BaseModel):
    style: List[Style]
    explanation: List[Explanation]

class GeminiService:
    @staticmethod  
    def generate_output(state, type):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        # produce = us_seasonal_data[state][month]

        # Prompt includes location and preference so Gemini can factor in the produce in season
        prompt = f"Please provide a primary and secondary them for animal"
        print(prompt)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            config={
                # Forces the response to be valid JSON matching our Recipe schema
                "response_mime_type": "application/json",
                "response_json_schema": Style.model_json_schema(),
            },
        )
        # Validate and parse the raw JSON string into a typed Recipe object
        recipe = Output.model_validate_json(response.text)
        recipe_dict = recipe.model_dump()
        # recipe_dict['image'] =       
      

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
