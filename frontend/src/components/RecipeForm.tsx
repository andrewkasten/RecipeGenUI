import { useState } from "react";

const STATES = [
  "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
  "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
  "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
  "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
  "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
  "New Hampshire", "New Jersey", "New Mexico", "New York",
  "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
  "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
  "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
  "West Virginia", "Wisconsin", "Wyoming",
];

const TYPES = [
  "Breakfast", "Lunch", "Dinner", "Snack", "Dessert",
  "Vegetarian", "Vegan", "Gluten-free",
  "Italian", "Mexican", "Asian", "Mediterranean", "American comfort food", "BBQ",
];

const inputClasses =
  "block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600";

export default function RecipeForm({
  handleRecipeSubmit,
}: {
  handleRecipeSubmit: (state: string, type: string) => void;
}) {
  const [state, setState] = useState<string>("");
  const [type, setType] = useState<string>("");

  return (
    <form
      method="POST"
      onSubmit={(e) => {
        e.preventDefault();
        handleRecipeSubmit(state, type);
      }}
      className="mx-auto mt-5 mb-5 max-w-xl sm:mt-5"
    >
      <div className="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
        <div>
          <label
            htmlFor="state"
            className="block text-sm/6 font-semibold text-gray-900"
          >
            State
          </label>
          <div className="mt-2.5">
            <select
              id="state"
              name="state"
              value={state}
              required
              onChange={(e) => setState(e.target.value)}
              className={inputClasses}
            >
              <option value="" disabled>
                Select a state…
              </option>
              {STATES.map((s) => (
                <option key={s} value={s}>
                  {s}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div>
          <label
            htmlFor="type"
            className="block text-sm/6 font-semibold text-gray-900"
          >
            Type
          </label>
          <div className="mt-2.5">
            <select
              id="type"
              name="type"
              value={type}
              required
              onChange={(e) => setType(e.target.value)}
              className={inputClasses}
            >
              <option value="" disabled>
                Select a type…
              </option>
              {TYPES.map((t) => (
                <option key={t} value={t}>
                  {t}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
      <div className="mt-10">
        <button
          type="submit"
          disabled={!state || !type}
          className="block w-full rounded-md bg-gray-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-xs hover:bg-gray-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600 disabled:cursor-not-allowed disabled:opacity-50"
        >
          Generate
        </button>
      </div>
    </form>
  );
}
