import requests

url = "https://api.apilayer.com/bad_words?censor_character=censor_character"


def profanity_check(posted_content):
    #payload = posted_content.encode("utf-8")
    payload = posted_content
    headers= {
    "apikey": "b79r9QnNxDZ2iJpXow15Qxrca33ImvD0"
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()
    result= result["bad_words_total"]
    if result>0:
        return True
    else:
        return False


