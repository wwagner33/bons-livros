import React, { useState } from 'react';
import axios from 'axios';

function QuestionnaireForm() {
  const [preferences, setPreferences] = useState({
    genres: [],
    authors: [],
    books: []
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/recommend', preferences)
      .then(response => {
        // Redirect to recommendations page
      })
      .catch(error => {
        // Handle error
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Inputs for genres, authors, books */}
      <button type="submit">Get Recommendations</button>
    </form>
  );
}

export default QuestionnaireForm;
