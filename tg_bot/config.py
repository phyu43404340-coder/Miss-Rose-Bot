
from tg_bot.sample_config import Config

class Development(Config):
    LOGGER = True
    
    # REQUIRED - ဒါတွေကိုပြောင်းရမယ်
    API_KEY = "8788172810:AAG9cQaEuF1R61aDK3n46HyGf6CumXNsOIQ"  # သင့် BotFather token
    OWNER_ID = 6440394225  # သင့် Telegram ID (ကိန်းပြည့်)
    OWNER_USERNAME = "logic_dex"  # သင့် Telegram username (@ မပါ)
    
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://avnadmin:AVNS_y6q98elxsgXzYloNLMB@pg-14067a43-phyu43404340-1cc5.c.aivencloud.com:17798/defaultdb?sslmode=require"  # Railway DB URL
    MESSAGE_DUMP = -1003529420898  # သင့် log group ID (အနုတ်လက္ခဏာနဲ့)
    
    # OPTIONAL
    SUDO_USERS = []  # Sudo users IDs
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    
    # WEBHOOK setting (Railway အတွက်)
    WEBHOOK = True
    URL = "https://web-production-2cd2b.up.railway.app"  # သင့် Railway app URL
    PORT = 8080  # Railway က port 8080 ကိုသုံးတယ်
