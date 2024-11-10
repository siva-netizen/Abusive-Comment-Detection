function analyzeComments() {
    var videoUrl = document.getElementById('videoUrl').value;
    fetch('http://localhost:5000/analyze_comments', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ video_url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
      var commentsDiv = document.getElementById('comments');
      commentsDiv.innerHTML = '<h2>Abusive Comments:</h2>';
      data.forEach(comment => {
        commentsDiv.innerHTML += '<p>' + comment + '</p>';
      });
    })
    .catch(error => console.error('Error:', error));
  }
  