# Telegram API credentials (get from my.telegram.org)
API_ID = "25489830"
API_HASH = "b3df97daea65252260b2c2513a94ee5a"
BOT_TOKEN = "8230766671:AAFl96_m6TgmdjverB1arDToO09rRLyVv78"

# Rate limiting settings (in seconds)
ADMIN_DELAY = 1.5      # Delay between admin checks
FORWARD_DELAY = 2.0    # Delay between message forwards
BATCH_DELAY = 0.5      # Delay between files in a batch
DELETE_DELAY = 0.3     # Delay between message deletions

# Database settin

# Job limits
MAX_BATCH_SIZE = 20
MAX_RECURRING_TIME = 1440  # 24 hours in minutes
MAX_DELETE_TIME = 10080    # 7 days in minutes

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
ADMIN_IDS = [6082136901]
FORCE_SUB_CHANNEL_ID = "-1002706901945"
# MongoDB configuration
MONGODB_URI = 'mongodb+srv://valentina:valentina@cluster0.igx2yx7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' # or your MongoDB connection string
DATABASE_NAME = 'autopost'
