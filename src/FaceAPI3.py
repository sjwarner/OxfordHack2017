########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

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
 
    print ('Response:')
    parsed = json.loads(response.text)
    emotion_happy = parsed[0]['faceAttributes']['emotion']['happiness']
    emotion_sad = parsed[0]['faceAttributes']['emotion']['sadness']

    emotions_file = open('./emotions1.txt', 'x')

    if emotion_happy > emotion_sad:
        emotions_file.write('happiness,' + str(emotion_happy))
    else:
        emotions_file.write('sadness,' + str(emotion_sad))

    print(str(emotion_happy) + ',' + str(emotion_sad))

except Exception as e:
    print('Error:')
    print(e)

####################################    

