import os
import yt_dlp
from flask import Flask, render_template, request, send_file
from threading import Thread
import time
import datetime

app = Flask(__name__)

# Temporary directory for downloads
temp_download_dir = "temp_downloads"
if not os.path.exists(temp_download_dir):
    os.makedirs(temp_download_dir)


def clean_temp_folder():
    while True:
        now = time.time()
        for filename in os.listdir(temp_download_dir):
            file_path = os.path.join(temp_download_dir, filename)
            if os.path.isfile(file_path):
                file_age = now - os.path.getmtime(file_path)
                if file_age > 60:  
                    os.remove(file_path)
        time.sleep(20)  


cleanup_thread = Thread(target=clean_temp_folder, daemon=True)
cleanup_thread.start()


def downloadVideo(url):
    try:
        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
            'outtmpl': os.path.join(temp_download_dir, '%(title)s.%(ext)s'),
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return filename
    except Exception as e:
        return str(e)

def downloadAudioOnly(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': os.path.join(temp_download_dir, '%(title)s.%(ext)s'),
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return filename
    except Exception as e:
        return str(e)

def sanitizeUrl(url):
    if 'music.youtube.com' in url:
        url = url.replace('music.youtube.com', 'www.youtube.com')
    return url

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    file_url = None
    url = ''
    action = ''

    if request.method == 'POST':
        url = request.form.get('url')
        action = request.form.get('action')

        if not url:
            message = "Error: URL is required!"
        else:
            try:
                url = sanitizeUrl(url)

                if action == "video":
                    filename = downloadVideo(url)
                    download_name = os.path.basename(filename)
                    mime_type = 'video/mp4'
                elif action == "audio":
                    filename = downloadAudioOnly(url)
                    download_name = os.path.basename(filename)
                    mime_type = 'audio/mp3'
                else:
                    message = "Invalid action"
                    return render_template('index.html', message=message)

                if filename and os.path.exists(filename):
                    file_url = f'/download/{download_name}'
                    message = f"{download_name} is ready for download."

                else:
                    message = "Error: Download failed!"
            except Exception as e:
                message = f"Error: {str(e)}"

    return render_template('index.html', message=message, file_url=file_url)

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(temp_download_dir, filename)
    if os.path.exists(file_path):
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/octet-stream',  # Use generic MIME type
            conditional=True
        )
    else:
        return "File not found", 404

@app.route('/about')
def about():
    return render_template('about.index')


if __name__ == '__main__':
    app.run(debug=True)
