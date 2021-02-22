from datetime import datetime

def fprint(message, type = ''):
    if type == 'i':
        print('[' + datetime.now().strftime("%H:%M:%S") + '] INFO# ' + str(message))
    elif type == 'd':
       print('DEBUG# ' + str(message))
    elif type == 'e':
        print('ERROR# ' + str(message))
    else:
        print(str(message))


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)