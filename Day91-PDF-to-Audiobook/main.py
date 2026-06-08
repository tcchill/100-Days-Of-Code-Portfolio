from pypdf import PdfReader
from google.cloud import texttospeech

# Create a reader object
reader = PdfReader("day91_introduction.pdf")

# Get total number of pages
number_of_pages = len(reader.pages)
print(f"Total Pages: {number_of_pages}")

pdf_text = ""
# Extract text from the first page
for i in range(number_of_pages):
    page = reader.pages[i]
    pdf_text += page.extract_text() + " "

print(pdf_text)


cl = texttospeech.TextToSpeechClient()
syn_input = texttospeech.SynthesisInput(text=pdf_text)

voice_pr = texttospeech.VoiceSelectionParams(
    language_code="vi-VN",
    name="vi-VN-Neural2-D"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = cl.synthesize_speech(
    input=syn_input,
    voice=voice_pr,
    audio_config=audio_config
)

output_audio_path = "./output.mp3"
with open(output_audio_path, "wb") as out:
    out.write(response.audio_content)
    print(f"Audio file has been created in: {output_audio_path}")