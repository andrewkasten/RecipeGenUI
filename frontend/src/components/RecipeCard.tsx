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

type RecipeCardProps = {
  state: string;
  type: string;
  recipe: RecipeData;
};




export default function RecipeCard({ state, type, recipe }: RecipeCardProps) {
  return (
    <div className="animate-fade bg-gray-50 mt-10 shadow-xl rounded-2xl overflow-hidden max-w-4xl w-full grid md:grid-cols-2 hover:scale-[1.02] hover:shadow-gray-900/20">
      <div className="h-64 md:h-auto bg-gray-200">
        {recipe.image && (
          <img
            src={recipe.image}
            alt={recipe.recipe_name}
            className="w-full h-full object-cover animate-fade animate-delay-550"
          />
        )}
      </div>

      <div className=" p-6 flex flex-col justify-between">
        <div>
          <h2 className=" animate-fade text-3xl font-bold text-gray-800 mb-7">
            {recipe.recipe_name}
          </h2>

          <ul className="text-gray-600 mb-2 flex justify-center gap-4">
            <li className="flex items-top gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#6b7280">
                <path d="M360-840v-80h240v80H360Zm80 440h80v-240h-80v240Zm-99.5 291.5Q275-137 226-186t-77.5-114.5Q120-366 120-440t28.5-139.5Q177-645 226-694t114.5-77.5Q406-800 480-800q62 0 119 20t107 58l56-56 56 56-56 56q38 50 58 107t20 119q0 74-28.5 139.5T734-186q-49 49-114.5 77.5T480-80q-74 0-139.5-28.5ZM678-242q82-82 82-198t-82-198q-82-82-198-82t-198 82q-82 82-82 198t82 198q82 82 198 82t198-82ZM480-440Z" />
              </svg>
              <div className="animate-fade animate-delay-550 flex flex-col leading-tight">
                <span className="font-semibold" style={{color: `${recipe.color}`}}>
                  {recipe.prep_time_minutes ?? "--"}
                </span>
                <span className="text-xs text-gray-600">Minutes</span>
              </div>
            </li>

            <li className="flex items-top gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#6b7280">
                <path d="M200-200v-560 454-85 191Zm0 80q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v320h-80v-320H200v560h280v80H200Zm494 40L552-222l57-56 85 85 170-170 56 57L694-80ZM348.5-451.5Q360-463 360-480t-11.5-28.5Q337-520 320-520t-28.5 11.5Q280-497 280-480t11.5 28.5Q303-440 320-440t28.5-11.5Zm0-160Q360-623 360-640t-11.5-28.5Q337-680 320-680t-28.5 11.5Q280-657 280-640t11.5 28.5Q303-600 320-600t28.5-11.5ZM440-440h240v-80H440v80Zm0-160h240v-80H440v80Z" />
              </svg>
              <div className="flex flex-col leading-tight animate-fade animate-delay-550 ">
                <span className="font-semibold " style={{color: `${recipe.color}`}}>{recipe.ingredients?.length ?? "--"}</span>
                <span className="text-xs text-gray-600">Ingredients</span>
              </div>
            </li>

            <li className="flex items-top gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="34px" fill="#6b7280">
                <path d="M536.5-503.5Q560-527 560-560t-23.5-56.5Q513-640 480-640t-56.5 23.5Q400-593 400-560t23.5 56.5Q447-480 480-480t56.5-23.5ZM480-186q122-112 181-203.5T720-552q0-109-69.5-178.5T480-800q-101 0-170.5 69.5T240-552q0 71 59 162.5T480-186Zm0 106Q319-217 239.5-334.5T160-552q0-150 96.5-239T480-880q127 0 223.5 89T800-552q0 100-79.5 217.5T480-80Zm0-480Z" />
              </svg>
              <div className="flex flex-col leading-tight animate-fade animate-delay-550">
                <span className="font-semibold " style={{color: `${recipe.color}`}}>{state}</span>
                <span className="text-xs text-gray-600">Location</span>
              </div>
            </li>

            <li className="flex items-top gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#6b7280">
                <path d="M371.5-208.5Q380-217 380-230v-240q26-8 43-28.5t17-49.5v-152q0-8-6-14t-14-6q-8 0-14 6t-6 14v100h-30v-100q0-8-6-14t-14-6q-8 0-14 6t-6 14v100h-30v-100q0-8-6-14t-14-6q-8 0-14 6t-6 14v152q0 29 17 49.5t43 28.5v240q0 13 8.5 21.5T350-200q13 0 21.5-8.5Zm240 0Q620-217 620-230v-224q33-16 51.5-51t18.5-82q0-57-28.5-95T590-720q-43 0-71.5 38T490-587q0 47 18.5 82t51.5 51v224q0 13 8.5 21.5T590-200q13 0 21.5-8.5ZM160-80q-33 0-56.5-23.5T80-160v-640q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v640q0 33-23.5 56.5T800-80H160Zm0-80h640v-640H160v640Zm0 0v-640 640Z" />
              </svg>
              <div className="flex flex-col leading-tight animate-fade animate-delay-550">
                <span className="font-semibold" style={{color: `${recipe.color}`}}>{type}</span>
                <span className="text-xs text-gray-600">Type</span>
              </div>
            </li>
          </ul>
          <p className="text-gray-600 mb-4 animate-fade animate-delay-1050">{recipe.reasoning}</p>
          <div className="mb-4">
            <h3 className="text-xl font-semibold mb-2 animate-fade animate-delay-1550" style={{color: `${recipe.color}`}}>Ingredients</h3>
            <h5 className="text-lg">Calories: {recipe.calories}</h5>
            <ul className="list-disc pl-5 space-y-1 text-gray-700 text-sm animate-fade animate-delay-1650 ">
              {recipe.ingredients?.map((ingredient, index) => (
                <li key={index}>
                  {ingredient.name} - {ingredient.quantity}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3 className="text-xl font-semibold mb-2 animate-fade animate-delay-2150" style={{color: `${recipe.color}`}}>Instructions</h3>
            <ol className="list-decimal pl-5 space-y-1 text-gray-600 text-sm animate-fade animate-delay-2250">
              {recipe.instructions?.map((step, index) => (
                <li key={index}>{step}</li>
              ))}
            </ol>
          </div>
        </div>
      </div>
    </div>
  );
}
