
import React, { useEffect, useState } from "react";
import { collectData } from "./dataCollector";
import { collectInteractions } from "./interactionFallback";
import { sendData } from "./api";

function App() {
  const [verdict, setVerdict] = useState("Verifying...");

  useEffect(() => {
    const runAnalysis = async () => {
      let data = collectData();
      let result = await sendData(data);

      if (result.is_bot === "maybe") {
        const interactionData = await collectInteractions();
        data = { ...data, ...interactionData };
        result = await sendData(data);
      }

      setVerdict(result.is_bot ? "Bot detected" : "Human detected");
    };

    runAnalysis();
  }, []);

  return <div>{verdict}</div>;
}

export default App;
