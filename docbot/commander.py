from .utils.sheets import microchip_lookup


def microchip(animal_name):
    microchip = microchip_lookup(animal_name)
    print(microchip)
    return {
        "response_type": "ephemeral",
        "text": "Microchip Lookup for %s" % animal_name,
        "attachments": [
            {
                "text": microchip
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
    if command == "/microchip":
        return microchip(text)
    if command == "/docbot":
        return help()
