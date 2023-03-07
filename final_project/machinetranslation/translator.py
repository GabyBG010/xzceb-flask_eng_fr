import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

apikey = 'Wo0bGZ_Z9tq1OOwlXn0nCYscXmXh-YLAeiJvq3Qc4nXW'
url='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/15fb284d-9a81-4aa5-be3c-109f0de7f701'
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()['translations'][0]['translation']    
    return englishText