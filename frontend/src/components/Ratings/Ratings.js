import React from 'react';
import axios from 'axios';

function Rating({ bookId }) {
  const handleRating = (rating) => {
    axios.post('/rate', { book_id: bookId, rating })
      .then(response => {
        // Handle success
      })
      .catch(error => {
        // Handle error
      });
  };

  return (
    <div>
      {[0, 1, 2, 3, 4, 5].map((star) => (
        <button key={star} onClick={() => handleRating(star)}>{star} Star</button>
      ))}
    </div>
  );
}

export default Rating;
