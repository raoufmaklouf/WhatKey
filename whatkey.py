import re
import sys

key=sys.argv[1]

REGEX = {
"MD5 Hash":"[a-f0-9]{32}",
"Artifactory API Token":'(?:\s|=|:|"|^)AKC[a-zA-Z0-9]{10,}',
"Basic Auth Credentials":"(?<=:\/\/)[a-zA-Z0-9]+:[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+",
"Cloudinary Basic Auth":"cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+",
"Facebook Access Token":"EAACEdEose0cBA[0-9A-Za-z]+",
"Google Cloud Platform API Key":"(?i)(google|gcp|youtube|drive|yt)(.{0,20})?['\"][AIza[0-9a-z\\-_]{35}]['\"]",
"Google Drive API Key":"AIza[0-9A-Za-z\\-_]{35}",
"Google Drive Oauth":"[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com",
"Gmail API Key":"AIza[0-9A-Za-z\\-_]{35}",
"Youtube API Key":"AIza[0-9A-Za-z\\-_]{35}",
"Youtube Oauth":"[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\\.com",
"Twilio API Key":"55[0-9a-fA-F]{32}",
"Square OAuth Secret":"q0csp-[ 0-9A-Za-z-_]{43}",
"Square Access Token":"sqOatp-[0-9A-Za-z-_]{22}",
"Picatic API Key":"sk_live_[0-9a-z]{32}",
"Foursquare Secret Key":"R_[0-9a-f]{32}",
"Gmail OAuth":"[0-9(+-[0-9A-Za-z_]{32}.apps.qooqleusercontent.com",
"Instagram OAuth ":"[0-9a-fA-F]{7}.[0-9a-fA-F]{32}",
"Facebook Access Token":"[1-9][ 0-9]+-[0-9a-zA-Z]{40}",
"Twitte Access Token":"[1-9][ 0-9]+-[0-9a-zA-Z]{40}",
"Github OAuth":"[0-9a-fA-F]{40}",
"Telegram bot_token":"[0-9]{10}:[a-zA-Z0-9_-]{35}",
"AWS Access Key ID Value":"(A3T[A-Z0-9]|AKIA|AGPA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
"FCM Server Key":"AAAA[a-zA-Z0-9_-]{7}:[a-zA-Z0-9_-]{140}",
"slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
"slack_webhook":"https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
"facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
"twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]",
"heroku_api": "[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
"mailchamp_api": "[0-9a-f]{32}-us[0-9]{1,2}",
"picatic_api": "sk_live_[0-9a-z]{32}",
"google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.googleusercontent.com",
"Google Maps api": "AIza[0-9A-Za-z-_]{35}",
"google_captcha": "^6[0-9a-zA-Z_-]{39}$",
"google_oauth": "ya29\\.[0-9A-Za-z\\-_]+",
"amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}",
"amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
"Amazon Web Services Secret Key":"[0-9a-zA-Z/+]{40}",
"facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+",
"mailgun_api_key": "key-[0-9a-zA-Z]{32}",
"twilio_api_key": "\SK[0-9a-fA-F]{32}$",
"twilio_account_sid": "\AC[a-zA-Z0-9_\\-]{32}$",
"twilio_app_sid": "\AP[a-zA-Z0-9_\\-]{32}$",
"paypal_braintree_access_token": "access_token,production$[0-9a-z]{161[0-9a,]{32}",
"square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\-_]{43}",
"square_access_token": "sqOatp-[0-9A-Za-z\\-_]{22}",
"stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}",
"stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}",
"github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*",
"AMAZON_KEY":"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",

}
s=0
for a,b in REGEX.items():
    mutch=re.search(b, str(key))
    if(mutch):
        print('\033[32m[+]\033[00m '+str(a))
        s=1
        
        
if s==0:
    print('No result found (-_-)')
else:
    print('\n\033[94m[INFO]\033[00m This repository can help you in exploitation:  https://github.com/streaak/keyhacks')
