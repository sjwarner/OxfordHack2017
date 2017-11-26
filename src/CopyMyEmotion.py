########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, os.path

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = ''

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

# Body. The URL of a JPEG image to analyze.
# body = {'url': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}

img_filename = 'src/test.png'
with open(img_filename, 'rb') as f:
    img_data = f.read()

try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', uri_base + '/face/v1.0/detect', data=img_data, headers=headers, params=params)

    parsed = json.loads(response.text)
    emotions = parsed[0]['faceAttributes']['emotion']
    max_value = 0
    max_key = ""
    for key in emotions.keys():
        if emotions[key] > max_value:
            max_key = key
            max_value = emotions[key]

    if os.path.isfile('./emotions1.txt'):
        emotions_file = open('./emotions2.txt','x')
    else:
        emotions_file = open('./emotions1.txt', 'x')

    emotions_file.write(max_key + ',' + str(max_value))

    # print ('Your most dominant emotion was: ' + (str(max_key)) +  (str(emotions[max_key])))

except Exception as e:
    print('Error:')
    print(e)

####################################    

