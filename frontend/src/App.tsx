import { useState, useEffect } from "react";
import "./App.css";
import RecipeCard from "./components/RecipeCard";
import Header from "./components/header";
import RecipeForm from "./components/RecipeForm";
import Skeleton from "./components/Skeleton";

const API_BASE = import.meta.env.VITE_BASE_URL || "";

type Ingredient = {
  name: string;
  quantity: string;
};

type RecipeData = {
  recipe_name: string;
  prep_time_minutes: number | null;
  reasoning: string;
  ingredients: Ingredient[];
  instructions: string[];
  image: string;
  calories:string;
  color: string;
};

type RecipeItem = {
  id: number;
  state: string;
  type: string;
  recipe: RecipeData;
};

type WeatherNote = {
  zip_code: string;
  note: string;
};

function App() {
  const [recipe, setRecipe] = useState<RecipeItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  // const [weatherNote, setWeatherNote] = useState<WeatherNote | null>(null);
  // console.log(recipe)
  // useEffect(() => {
  //   fetch(`${API_BASE}/api/ai/gem/weather-note`)
  //     .then((res) => res.ok ? res.json() : null)
  //     .then((data) => data && setWeatherNote(data))
  //     .catch(() => {});
  // }, []);

  const fetchRecipes = async () => {
    setIsLoading(true);
    fetch(`${API_BASE}/api/ai/gem/recipe`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then((data) => setRecipe(Array.isArray(data) ? data : []))
      .catch((err) => console.error("Error:", err))
      .finally(() => setIsLoading(false));
  };

  useEffect(() => {
    fetchRecipes();
  }, []);

  const handleRecipeSubmit = async (state: string, type: string) => {
    setIsLoading(true);
    try {
      const response = await fetch(`${API_BASE}/api/ai/gem/recipe`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ state, type }),
      });
      if (!response.ok)
        throw new Error(`HTTP error! status: ${response.status}`);
      await fetchRecipes();
    } catch (error) {
      console.error("Recipe error:", error);
    }
  };

  return (
    <>
      {/* {weatherNote && (
          <div className="mt-3 flex items-start gap-2 rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-800">
            <span className="text-base">☁️</span>
            <span>{weatherNote.note}</span>
          </div>
        )} */}
      <div className="isolate bg-gray-50 px-5 py-6 sm:py-5 lg:px-5">
        <Header />

        <RecipeForm handleRecipeSubmit={handleRecipeSubmit} />
      </div>
      <section className="bg-gray-60 min-h-screen flex flex-col items-center justify-start gap-6 p-6">
        {isLoading && <Skeleton />}
        {recipe
          .slice()
          .reverse()
          .map((obj) => (
            <RecipeCard
              key={obj.id}
              state={obj.state}
              type={obj.type}
              recipe={obj.recipe}
            />
          ))}
      </section>
    </>
  );
}

export default App;
