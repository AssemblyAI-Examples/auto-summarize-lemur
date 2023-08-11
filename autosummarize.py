import assemblyai as aai

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/lex_guido.webm")

if transcript.error:
  raise Exception(f'Transcription error: {transcript.error}')

context = "A GitLab meeting to discuss logistics"

answer_format = '''**<topic header>**
<topic summary>
'''

result = transcript.lemur.summarize(
  context=context,
  answer_format=answer_format,
)

print(result.response)
