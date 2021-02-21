import random

async def cli(message, dinamic_db, static_db):
    option = message.content.lower()[6:].strip()
    if option == 'help':
        options = ['Here is what I can help you with', 'Here is what I know', 'Choose one of these']
        response = options[random.randint(0, len(options)-1)] + ':\n'
        response += ('\n'.join(static_db.getAttribute('sano_commands'))).strip()
        await message.channel.send(response)
    elif option == 'add':
        await message.channel.send('Implement me, plese!')
    elif option == 'remove':
        await message.channel.send('Implement me, plese!')
    elif option == 'shut up':
        responses = dinamic_db.getAttribute('sano_shut_responses')
        dinamic_db.setAttribute('sano_active', False)
        await message.channel.send(responses[random.randint(0, len(responses)-1)])
    else:
        await message.channel.send('Unknow option! Use: sano -help.')