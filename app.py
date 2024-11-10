# app.py

from flask import Flask, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)
from joblib import load
svm_model = load('svm_model.joblib')


# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey='AIzaSyAB84HJKtEdw1jtcWSL28t8b4CQrTUzGf4')

# Route to handle requests from the extension
@app.route('/analyze_comments', methods=['POST'])
def analyze_comments():
    # Get video ID from request
    video_url = request.json.get('video_url')
    video_id = extract_video_id(video_url)
    
    # Fetch comments from YouTube API
    comments = fetch_comments(video_id)
    
    # Pass comments through ML model (replace with your actual model)
    abusive_comments = svm_model(comments)
    
    # Return abusive comments to the extension
    return jsonify(abusive_comments)

def extract_video_id(video_url):
    # Extract video ID from YouTube video URL
    # Example URL: https://www.youtube.com/watch?v=VIDEO_ID
    video_id = video_url.split('v=')[-1]
    return video_id

def fetch_comments(video_id):
    # Use YouTube API to fetch comments for the given video ID
    request = youtube.commentThreads().list(part="snippet", videoId=video_id, textFormat="plainText")
    response = request.execute()
    
    # Extract comments from response
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response['items']]
    
    return comments

def detect_abusive_comments(comments):
    # Placeholder for your abusive comment detection algorithm
    # Replace this with your actual ML model code
    abusive_comments = []
    for comment in comments:
        if is_abusive(comment):
            abusive_comments.append(comment)
    return abusive_comments

def is_abusive(comment):
    # Placeholder for abusive comment detection
    # Replace this with your actual abusive comment detection logic
    return False  # Dummy logic for now

if __name__ == '__main__':
    app.run(debug=True)
