def microchip(animal_name):
    return {
        "response_type": "ephemeral",
        "text": "Microchip Lookup for %s" % animal_name,
        "attachments": [
            {
                "text": "Microchip for %s" % animal_name
            }
        ]
    }


def help():
    return {
        "response_type": "ephemeral",
        "text": "Please use one of these commands.",
        "attachments": [
            {
                "text": "/docbot"
            },
            {
                "text": "/microchip <animal name>"
            }
        ]
    }


def command_parse(command, text):
    print(command)
    if command == "/microchip":
        return microchip(text)
    if command == "/docbot":
        return help()
