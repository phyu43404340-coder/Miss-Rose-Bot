from tg_bot.sample_config import Config

class Development(Config):
    LOGGER = True
    
    # REQUIRED
    API_KEY = "8788172810:AAG9cQaEuF1R61aDK3n46HyGf6CumXNsOIQ"
    OWNER_ID = 6440394225
    OWNER_USERNAME = "logic_dex"
    
    # RECOMMENDED - Neon.tech PostgreSQL
    SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_lgu6fSby3Yxi@ep-green-voice-aie7oa9e-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    MESSAGE_DUMP = -1003529420898
    
    # OPTIONAL
    SUDO_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 2
    ALLOW_EXCL = True
    BMERNU_SCUT_SRELFTI = None
    
    # WEBHOOK setting
    WEBHOOK = True
    URL = "https://web-production-2cd2b.up.railway.app"
    PORT = 8080
