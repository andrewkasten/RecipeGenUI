import { useState, useEffect } from "react";
import "./App.css";

const API_BASE = import.meta.env.VITE_BASE_URL || "";

type GeminiOutput = {
  id: number;
  input: string;
  output: string;
};

export default function GeminiPrompt(){

const [input, setInput] = useState<string>("");
const [output, setOutput] = useState<GeminiOutput[]>([]);

  useEffect(() => {
    const url = `${API_BASE}/api/ai/gem`;
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setOutput(data))
      .catch((err) => console.error("Error:", err));
  },[])
  console.log(output)

  const handleGeminiSubmit = async () => {
    const obj = {
      input: input,
    };
    const payload = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    };
    try {
      const response = await fetch(`${API_BASE}/api/ai/gem`, payload);
      const body = await response.json();
      return body;
    } catch (error) {
      console.log(error);
    }
  };

return (
    <>
   <div>
          <h1>Talk to Gemini</h1>
        </div>
        <form
          method="POST"
          onSubmit={(e) => {
            e.preventDefault();
            handleGeminiSubmit();
          }}
        >
          <textarea
            name="prompt"
            value={input}
            placeholder="Type something..."
            onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => {
              setInput(e.target.value);
            }}
          ></textarea>
          <button className="counter"> Generate</button>
        </form>
        <h2>Response:</h2>
        {output.map((item) => (
          <p key={item.id}>{item.output}</p>
        ))} 
</>
    )
}
