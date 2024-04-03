

import requests
import httpx
import json

API_KEY = '8f5cdf84227a2388f8a64ee4b6a7e3c9e8b13f6b'

url = 'https://api.deepgram.com/v1/listen?diarize=true&punctuate=true&utterances=true'
# params = {
#     'diarize': 'true',
#     'punctuate': 'true',
#     'utterances': 'true'
# }
#audio_file_path = 'E:\\Audio_Twitter_Tweets.mp3'

from deepgram import DeepgramClient, PrerecordedOptions
def speech_to_text_function(audio_file):

    DEEPGRAM_API_KEY = API_KEY

    # AUDIO_URL = {
    #     "url": "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"
    # }


    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = PrerecordedOptions(
            model="nova-2",
            language="en",
            smart_format=True, 
            diarize=True, 
        )
        buffer_data = audio_file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options=options,timeout=httpx.Timeout(300.0, connect=10.0))
        x = (json.loads(response.to_json()))["results"]['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']
        return x

    except Exception as e:
        print(f"Exception: {e}")
        return f"error {e}"

