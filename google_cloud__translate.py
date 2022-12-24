pip install google-cloud-translate


from google.cloud import translate_v2 as translate

client = translate.Client()

def translate_text_batch(texts, target_language):
  translations = client.batch_translate_text(
    texts, target_language=target_language, source_language='en')
  return translations


texts = ['Hello, world!', 'Bonjour, monde!', 'Hola, mundo!']
target_language = 'fr'

translations = translate_text_batch(texts, target_language)

for translation in translations:
  print(translation.translated_text)


from google.cloud import translate_v2 as translate

client = translate.Client()

def translate_large_text(text, target_language):
  # Split the text into chunks of 2 MB or less
  chunk_size = 2 * 1024 * 1024
  chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

  # Translate the chunks
  translations = []
  for chunk in chunks:
    translation = client.batch_translate_text(
      [chunk], target_language=target_language, source_language='en')[0]
    translations.append(translation.translated_text)

  # Concatenate the translations into a single string
  return ''.join(translations)

