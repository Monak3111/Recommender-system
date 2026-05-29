import { useState } from "react";

function App() {
  const [userId, setUserId] = useState("");
  const [recs, setRecs] = useState([]);

  const fetchRecommendations = async () => {
    const res = await fetch(`http://backend:8000/recommend/${userId}`);
    const data = await res.json();
    setRecs(data.recommendations);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>📊 Recommender System</h1>

      <input
        placeholder="Enter User ID"
        onChange={(e) => setUserId(e.target.value)}
      />

      <button onClick={fetchRecommendations}>
        Get Recommendations
      </button>

      <h3>Results:</h3>
      <ul>
        {recs.map((item, i) => (
          <li key={i}>Item {item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;