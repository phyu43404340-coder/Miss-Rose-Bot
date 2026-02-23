from tg_bot.sample_config import Config

class Development(Config):
    LOGGER = True
    
    # REQUIRED
    API_KEY = "8788172810:AAG9cQaEuF1R61aDK3n46HyGf6CumXNsOIQ"
    OWNER_ID = 6440394225
    OWNER_USERNAME = "logic_dex"
    
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://avnadmin:AVNS_y6q98elxsgXzYloNLMB@pg-14067a43-phyu43404340-1cc5.c.aivencloud.com:17798/defaultdb?sslmode=require"
    MESSAGE_DUMP = -1003529420898
    
    # OPTIONAL
    SUDO_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 4
    ALLOW_EXCL = True
    BMERNU_SCUT_SRELFTI = None  ##### ဒီစာကြောင်းကိုထည့်ပါ #####
    
    # WEBHOOK setting
    WEBHOOK = True
    URL = "https://web-production-2cd2b.up.railway.app"
    PORT = 8080
