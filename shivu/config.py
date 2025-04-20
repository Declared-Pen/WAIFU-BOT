class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7776071513"
    sudo_users = "6312154011", "5559464565"
    GROUP_ID = -1002374696109
    TOKEN = "7813169206:AAGysB2nOrVjeqdqlLmcg6Cdat84y1TLTs0"
    mongo_url = "mongodb+srv://itachii130506:idjVit5zIoSOL3Gv@cluster0.vmsab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_your_waifu_support"
    UPDATE_CHAT = "Collect_your_waifu_support"
    BOT_USERNAME = "Collect_your_waifu_bot"
    CHARA_CHANNEL_ID = "-1002374696109"
    api_id = 28682516
    api_hash = "bb43fa00569d8f4de75aad6bdeb3650d"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
