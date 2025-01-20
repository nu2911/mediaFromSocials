# MediaFromSocials

MediaFromSocials is a Flask-based web application that allows users to download videos and audio from social media platforms using URLs. The app leverages [yt-dlp](https://github.com/yt-dlp/yt-dlp) for handling downloads and provides a simple, intuitive interface.

## Features

- Download videos or audio directly from a URL.
- User-friendly interface for input and action selection.
- Automatically generates a download link for the media file.
- Lightweight and easy to set up.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/MediaFromSocials.git
   cd MediaFromSocials
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   source env/bin/activate       # On macOS/Linux
   .\env\Scripts\activate        # On Windows
   ```

3. **Install dependencies:**

   Ensure you have `pip` installed and then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   Start the Flask development server:

   ```bash
   python app.py
   ```

5. **Access the app:**

   Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. **Open the app** in your web browser by navigating to `http://127.0.0.1:5000`.

2. **Enter a URL** of the video or audio you want to download in the input field.

3. **Select an action:**
   - Click **Download Video** to download the video with audio.
   - Click **Download Audio** to download the audio only (e.g., MP3).

4. **Wait for the process to complete.** 
   - A link will be provided to download the requested media file.

5. **Click the download link** to save the file to your system.

## Project Structure

```plaintext
MediaFromSocials/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Main HTML page
├── static/
│   ├── styles.css        # CSS styles
│   └── chips.webm        # Spinner animation
└── temp_downloads/       # Folder where downloaded media files are stored temporarily
```

## Dependencies

- Flask
- yt-dlp
- Python 3.7+

## Notes

- Ensure `yt-dlp` is updated regularly for the best compatibility with supported platforms.
- Media files are saved in the `downloads` folder.
