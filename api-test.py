import requests

translation_url = f"https://api.funtranslations.com/translate/quenya.json"
text_to_translate = f"May the odds ever be in your favor."
data = {
    'text': text_to_translate
}

translation_response = requests.post(translation_url, data=data)
translation_result = translation_response.json()
quenya_statement = translation_result.get('contents', {}).get('translated')

print(quenya_statement)

if 'contents' in translation_result and 'translated' in translation_result['contents']:
       translated_text = translation_result['contents']['translated']
else:
    translated_text = "May the odds ever be in your favor. "
