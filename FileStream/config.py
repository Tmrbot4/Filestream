from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "23171051"))
    API_HASH = str(env.get("API_HASH", "10331d5d712364f57ffdd23417f4513c"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7423068058:AAFqDSKWmLd7lRoNMYQagEwv7aI7irftkPY"))
    OWNER_ID = int(env.get('OWNER_ID', '6987799874'))
    TO_CHANNEL = int(env.get("TO_CHANNEL", "-1002178270630"))   # Logs channel for user logs
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://fehebaw351:nHbjrujWqgqLR58H@cluster0.lekn97z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    DATABASE_NAME = env.get("DATABASE_NAME", "cluste0")
    COLLECTION_NAME = env.get('COLLECTION_NAME', 'Data')
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "TMR_update_channel"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'store05'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', "-1001868502293")
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "10"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/e581dec86ccfdfbdbf3b9.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/e581dec86ccfdfbdbf3b9.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002178270630"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002178270630"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", "ssrfs-7ecfd11f630e.herokuapp.com"))
    URL = "https://continuous-alina-merafile-bdb28365.koyeb.app/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
