class GemRecipeService:
    @staticmethod
    def generate_recipe(state, type):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        # Prompt includes location and preference so Gemini can factor in what produce is in season and affordable in that region right now
        prompt = f"Please provide a simple recipe that is good based on produce season and pricing for {state} and preference: {type}"

        # the JSON schema + Google Search grounding (Only Gemini 3) take time and stream can give frontend ability to render as it arrives, also might look cool.
        def stream():  
            try:
                yield ndjson({
                    "event": "start",
                    "value": {
                        "state": state,
                        "type": type,
                    },
                })

                response = client.models.generate_content_stream(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config={
                    # Google Search lets Gemini ground the image URL in a real result
                    # "tools": [{"google_search": {}}],

                    # Forces the response to be valid JSON matching our Recipe schema
                    "response_mime_type": "application/json",
                    "response_json_schema": Recipe.model_json_schema(),
                },
            )
      
                # generate_content_stream returns the response in chunks — 
                full_recipe = ""
                for chunk in response:
                    if chunk.text:
                        full_recipe += chunk.text # reassemble them into one string before parsing.

            # Validate and parse the raw JSON string into a typed Recipe object
                recipe = Recipe.model_validate_json(full_recipe)
                recipe_dict = recipe.model_dump()
                recipe_dict["image"] = pixabay_image(recipe.recipe_name)