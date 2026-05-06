import { useState } from "react";

export default function RecipeForm({ handleRecipeSubmit }: { handleRecipeSubmit: (state: string, type: string) => void }) {

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
              <input
                id="state"
                name="state"
                type="text"
                value={state}
                autoComplete="off"
                placeholder="New York, Wisconsin, Idaho, California..."
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                  setState(e.target.value)
                }
                className="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              />
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
              <input
                id="type"
                name="type"
                type="text"
                value={type}
                autoComplete="off"
                placeholder="Breakfast, Italian, vegan, BBQ, comfort food..."
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                  setType(e.target.value)
                }
                className="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              />
            </div>
          </div>
        </div>
        <div className="mt-10">
          <button
            type="submit"
            className="block w-full rounded-md bg-gray-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-xs hover:bg-gray-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
          >
            Generate
          </button>
        </div>
      </form>
    )
}