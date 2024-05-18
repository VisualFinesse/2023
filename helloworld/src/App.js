import axios from "axios";
import { useEffect, useState } from "react";

const App = () => {
  const [error, setError] = useState(null);
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:1337/api/content")
      .then(({ data }) => setRestaurants(data.data))
      .catch((error) => setError(error));
  }, []);

  if (error) {
    // Print errors if any
    return <div>An error occured: {error.message}</div>;
  }

  return (
    <div className="App">
      <ul>
        {restaurants.map(({ id, attributes }) => (
          <li key={id}>{attributes.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
