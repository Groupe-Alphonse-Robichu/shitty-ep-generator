from random import randrange

platforms = ["sur MacOS", "sur iPad", "sur iOS", "en Serverless"]
actions = ["Numérisation, classement et indexation automatique", "OCR", "Analyse"]
languages = ["en Swift", "avec AppleScript", "en Objective-C", "avec Electron"]
onObject = ["documents", "livres", "textes anciens"]
servers = ["avec AWS", "sur Azure"]
 ## Machine learning

"""Samples :
    Numérisation, classement et indexation automatique de documents sur MacOS.
    """

def selection():
    # Platform choice
    pl = randrange(len(platforms))
    platform = platforms[pl]
    if platform == "en Serverless": #en serverless
        platform += " " + servers[randrange(len(servers))] if randrange(2) == 1 else ""
    else:
        platform += " " + languages[randrange(len(languages))] if randrange(2) == 1 else ""
    
    # Action choice
    action = actions[randrange(len(actions))]
    obj = onObject[randrange(len(onObject))]
    
    return [action, obj, platform]


if __name__ == "__main__":
    selectList = selection()
    magicString = "{} de {} {}.".format(selectList[0], selectList[1], selectList[2])
    print(magicString)
