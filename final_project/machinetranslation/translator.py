'''
Creates an instance of the Watson Language Translator
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''Translates a piece of English text into French'''
    if english_text == None or len(english_text) == 0 :
        return ''
    translation_response = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = translation_response['translations'][0]['translation']
    # Alternatively: french_text = translation_response.get('translations')[0].get('translation')
    return french_text

def french_to_english(french_text):
    '''Translates a piece of French text into English'''
    if french_text == None or len(french_text) == 0 :
        return ''
    translation_response = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = translation_response.get('translations')[0].get('translation')
    return english_text
