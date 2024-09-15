import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Recommendations() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    axios.post('/recommend')
      .then(response => {
        setRecommendations(response.data.recommendations);
      })
      .catch(error => {
        // Handle error
      });
  }, []);

  return (
    <div>
      {recommendations.map((book) => (
        <div key={book.id}>
          <h3>{book.title}</h3>
          {/* Display book details */}
          {/* Include Rating component */}
        </div>
      ))}
    </div>
  );
}

export default Recommendations;
