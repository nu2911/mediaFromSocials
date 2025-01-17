from flask import Flask, render_template, request, send_file, redirect
import yt_dlp
import os

app = Flask(__name__)

downloadFolder = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)

def downloadVideo(url):
    try:
        ydl_opts = {
            'outtmpl': f'{downloadFolder}/%(title)s.%(ext)s',
            'format': 'best',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return os.path.basename(filename)  
    except Exception as e:
        return str(e)

def downloadAudioOnly(url):
    try:
        ydl_opts = {
            'outtmpl': f'{downloadFolder}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'noplaylist': True,
            'extractaudio': True,
            'audioformat': 'mp3',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return os.path.basename(filename) 
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
                elif action == "audio":
                    filename = downloadAudioOnly(url)
                else:
                    message = "Invalid action"
                    return render_template('index.html', message=message)

                if filename and os.path.exists(os.path.join(downloadFolder, filename)):
                    file_url = f'/download/{filename}'
                    message = f"{filename}."
                else:
                    message = "Error: File not found or download failed!"
            except Exception as e:
                message = f"Error: {str(e)}"

    return render_template('index.html', message=message, file_url=file_url)


@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(downloadFolder, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

# @app.route('/about')
# def about():
#     return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
