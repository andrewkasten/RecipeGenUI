import { useState } from "react";

const API_BASE = import.meta.env.VITE_BASE_URL || "";
const prompt =
  "Short note on if tomorrow's weather is good for walking a dog in Lehi, Utah? If it's Sunshine and clouds mixed, High 56F, Winds SSW at 5 to 10 mph, Humidity 31 ";

export default function Header() {
  // const [note, setNote] = useState<string>("");
  // const [loading, setLoading] = useState(false);

  // const handleDogWalk = async () => {
  //   setLoading(true);
  //   try {
  //     const res = await fetch(`${API_BASE}/api/ai/gem`, {
  //       method: "POST",
  //       headers: { "Content-Type": "application/json" },
  //       body: JSON.stringify({ input: prompt }),
  //     });
  //     const body = await res.json();
  //     setNote(body.output);
  //   } catch (e) {
  //     console.error(e);
  //   } finally {
  //     setLoading(false);
  //   }
  // };

  return (
    <div className="relative">
      {/* <aside className="absolute right-0 top-0 max-w-xs text-right">
        <button
          // onClick={handleDogWalk}
          disabled={loading}
          className="text-xs text-gray-400 hover:text-teal-500 underline disabled:opacity-50"
        >
          {loading ? "Checking..." : "Dog walk weather?"}
        </button>
        {note && (
          <p className="mt-1 text-xs text-gray-500 leading-snug">{note}</p>
        )}
      </aside> */}

      <header className="mx-auto max-w-2xl text-center">
        <h2 className="text-4xl font-semibold tracking-tight text-balance text-teal-500 sm:text-5xl">
          Seasonal Recipe Card Generator
        </h2>
        <p className="mt-10 text-lg/8 text-gray-700">
          Choose a location and what you're craving. AI will generate the recipe with seasonal produce and choose the text color. Watch live as a new card component appears.
        </p>
      </header>
    </div>
  );
}
