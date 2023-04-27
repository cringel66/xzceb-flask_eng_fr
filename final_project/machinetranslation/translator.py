""" translate words from different languages """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

#authenticator = IAMAuthenticator('$apikey')
authenticator = IAMAuthenticator('jHhUBmdBaXAsLOlGHoO5D5CZETgODmauhHRlfTSuztNS')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

#language_translator.set_service_url('$url')
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/bfa8534a-d13c-4055-8e4e-ea33de9bbb2c')

def englishToFrench(englishtext):
    """ translate english to french """
    translation=language_translator.translate(text=englishtext,model_id="en-fr").get_result()
    frenchtext=translation['translations'][0]['translation']
    return frenchtext

def frenchToEnglish(frenchtext):
    """ translate french to english """
    translation=language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    englishtext=translation['translations'][0]['translation']
    return englishtext
