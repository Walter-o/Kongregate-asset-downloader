from backend import kongdl
import sys

#kongdl.main(author="player_03", game="run-3")
'''
testCases = [
    ["oddgoo","amberial-axis"],
    ["player_03","run-3"],
    ["player_03","run-2"],
    ["player_03","run"],
    ["armorgames","crush-the-castle-2-pp"]
]

for author, game in testCases:
    print(kongdl.getContentTypes(author, game))

exit("breakPoint")
'''





def processInput(input):
    print("")
    if "kongregate.com" in input:
        if "?" in input or "#" in input:
            print("Please clean your url of \nfragments (#) and\n"
                  + "queries (?) \nbefore feeding it to me :c")
        else:
            cleanUrl = kongdl.cleanGameUrl(input)
            kongdl.main(cleanUrl["author"],
                        cleanUrl["game"])
            sys.exit()
    elif "/cmds" == input:
        print("Commands:\n"
            + "{url} - Just paste an url in here and it will download.\n"
            + "/vars - Shows some variables.\n"
            + "/cmds - This command.\n"
            + "/info - Credits, info etc.\n"
            + "/docs - Documentation for the downloaded files.")
    elif "/vars" == input:
        print("Zlib compression enabled: %s"%kongdl.ZLIB_COMPRESS)
        print("Also download thumbnails: %s"%kongdl.ENABLE_THUMBS)
    elif "/info" == input:
        print("Credits:\n"
              + "Kongregate level data / asset downlader\n"
              + "By Walter\n\n"
              + "Made in about 2 days, 2019/12/9 - 2019/13/9\n\n"
              + "Info:\n"
              + "After copying my kongregate asset downloader template a few times\n"
              + "i thought it was time for a good downloader to exist. One that goes\n"
              + "to hell and back to get all data possible, descriptions, author names,\n"
              + "Everything. The .json pages on kongregate don't give the full data.")
    elif "/docs" == input:
        print("rating: (Optional) Average rating for level, float between 0-5\n"
            + "plays:  How many times a level has been played\n"
            + "name:   Level name\n"
            + "author: Kongregate username of the level creator\n"
            + "data:   The actual level data / asset data\n"
            + "type:   Type of asset, usually there's only 1 or 2\n"
            + "id:     Asset ID. There's a very high chance id's are unique\n"
            + "desc:   (Optional) Description of a level\n"
            + "thumb:  (Optional) Thumbnail of level\n")
    else:
        print("I don't know that command, try /cmds")
    print("")

try:
    cleanUrl = kongdl.cleanGameUrl(sys.argv[1])
except:
    pass
else:
    kongdl.main(cleanUrl["author"],
                cleanUrl["game"])
    exit("Downloaded with CLI")


print('''
Welcome to Walter's Kongregate asset downloader v2.00\n
Type: /cmds for list of commands
You can start off by providing a game url.
Perfect example: https://www.kongregate.com/games/player_03/run-3\n
''')
while True:
    processInput(raw_input("Input: "))