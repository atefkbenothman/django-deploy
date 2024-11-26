from .celery import app


@app.task(name="convert_audio_file_to_hls")
def convert_audio_file_to_hls(filename: str):
    print("-------")
    print(f"converting file {filename}")
    print("-------")
    return
