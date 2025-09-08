import yt_dlp
import os

def download_and_send(url, update):
    update.message.reply_text("⏳ Downloading... Please wait!")

    try:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'mp4/bestaudio/best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        with open(file_path, "rb") as video:
            update.message.reply_video(video)

        os.remove(file_path)  # clean up

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")
