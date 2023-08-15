import assemblyai as aai

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/lex_guido.webm")

if transcript.error:
  raise Exception(f'Transcription error: {transcript.error}')

context = "An episode of the Lex Fridman podcast, in which he speaks with Guido van Rossum, the creator of the Python programming language"

answer_format = '''**<topic header>**
<topic summary>
'''

result = transcript.lemur.summarize(
  context=context,
  answer_format=answer_format,
)

print(result.response)
