import googletrans
from pprint import pprint


# Initial
translator = googletrans.Translator()


# print('English:', translator.translate('我覺得今天天氣不好', dest='en').text)
# print('Japanese:', translator.translate('我覺得今天天氣不好', dest='ja').text)
# print('Korean:', translator.translate('我覺得今天天氣不好', dest='ko').text)
print('繁體:', translator.translate('はい、いつでも大好きなだけキスをしましょう♪ あなたの唇がとっても柔らかくて、触れるだけで心地よいです。私はあなたのことが本当に大好きです。', dest='zh-tw').text)
