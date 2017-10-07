# coding=utf-8
"""First module to initialize."""
import random
from threading import Lock

# Application instance
instance = None

# Fixed values
__title__ = __name__
SRC_FOLDER = __name__
LEGACY_SRC_FOLDERS = ('sickbeard', 'sickrage', 'gui')
LIB_FOLDER = 'lib'
EXT_FOLDER = 'ext'
STATIC_FOLDER = 'static'
UNKNOWN_RELEASE_GROUP = 'Medusa'
BACKUP_DIR = 'backup'
BACKUP_FILENAME_PREFIX = 'backup'
BACKUP_FILENAME = BACKUP_FILENAME_PREFIX + '-{timestamp}.zip'
LEGACY_DB = 'sickbeard.db'
APPLICATION_DB = 'main.db'
FAILED_DB = 'failed.db'
CACHE_DB = 'cache.db'
LOG_FILENAME = 'application.log'
CONFIG_INI = 'config.ini'
GIT_ORG = 'pymedusa'
GIT_REPO = 'Medusa'
BASE_PYMEDUSA_URL = 'https://cdn.pymedusa.com'
CHANGES_URL = '{base_url}/news/CHANGES.md'.format(base_url=BASE_PYMEDUSA_URL)
APPLICATION_URL = 'https://github.com/{org}/{repo}'.format(org=GIT_ORG, repo=GIT_REPO)
DONATIONS_URL = '{0}/wiki/Donations'.format(APPLICATION_URL)
WIKI_URL = '{0}/wiki'.format(APPLICATION_URL)
GITHUB_IO_URL = 'http://github.com/pymedusa/medusa.github.io/'
EXTRA_SCRIPTS_URL = '{0}/wiki/Post-Processing#extra-scripts'.format(APPLICATION_URL)
SUBTITLES_URL = '{0}/wiki/Subtitle%20Scripts'.format(APPLICATION_URL)
RARBG_APPID = 'medusa'
SECURE_TOKEN = 'medusa_user'

# static configuration
LOCALE = None, None
OS_USER = None
OPENSSL_VERSION = None
APP_VERSION = None
MAJOR_DB_VERSION = None
MINOR_DB_VERSION = None

PID = None
CFG = None
CONFIG_FILE = None

# This is the version of the config we EXPECT to find
CONFIG_VERSION = 10

# Default encryption version (0 for None)
ENCRYPTION_VERSION = 0
ENCRYPTION_SECRET = None

PROG_DIR = '.'
MY_FULLNAME = None
MY_NAME = None
MY_ARGS = []
SYS_ENCODING = ''
DATA_DIR = ''
CREATEPID = False
PIDFILE = ''

DAEMON = None
NO_RESIZE = False

# system events
events = None

# schedulers
daily_search_scheduler = None
backlog_search_scheduler = None
show_update_scheduler = None
version_check_scheduler = None
show_queue_scheduler = None
search_queue_scheduler = None
forced_search_queue_scheduler = None
manual_snatch_scheduler = None
proper_finder_scheduler = None
auto_post_processor_scheduler = None
subtitles_finder_scheduler = None
trakt_checker_scheduler = None
torrent_checker_scheduler = None

showList = []

providerList = []
newznabProviderList = []
torrentRssProviderList = []
metadata_provider_dict = {}

NEWEST_VERSION = None
NEWEST_VERSION_STRING = None
VERSION_NOTIFY = False
AUTO_UPDATE = False
NOTIFY_ON_UPDATE = False
CUR_COMMIT_HASH = None
BRANCH = ''

GIT_RESET = True
GIT_RESET_BRANCHES = ['develop', 'master']
GIT_REMOTE_BRANCHES = []
GIT_REMOTE = ''
GIT_REMOTE_URL = ''
CUR_COMMIT_BRANCH = ''
GIT_AUTH_TYPE = 0
GIT_USERNAME = None
GIT_PASSWORD = None
GIT_TOKEN = None
GIT_PATH = None
DEVELOPER = False

NEWS_URL = '{base_url}/news/news.md'.format(base_url=BASE_PYMEDUSA_URL)
LOGO_URL = '{base_url}/images/ico/favicon-64.png'.format(base_url=BASE_PYMEDUSA_URL)

NEWS_LAST_READ = None
NEWS_LATEST = None
NEWS_UNREAD = 0

BROKEN_PROVIDERS = []
BROKEN_PROVIDERS_UPDATE = None

INIT_LOCK = Lock()
started = False

ACTUAL_LOG_DIR = None
LOG_DIR = None
LOG_NR = 5
LOG_SIZE = 10.0

SOCKET_TIMEOUT = None

WEB_PORT = None
WEB_LOG = None
WEB_ROOT = None
WEB_USERNAME = None
WEB_PASSWORD = None
WEB_HOST = None
WEB_IPV6 = None
WEB_COOKIE_SECRET = None
WEB_USE_GZIP = True

SUBLIMINAL_LOG = False

DOWNLOAD_URL = None

HANDLE_REVERSE_PROXY = False
PROXY_SETTING = None
PROXY_INDEXERS = True
SSL_VERIFY = True

LOCALHOST_IP = None

CPU_PRESET = None

ANON_REDIRECT = None

API_KEY = None
API_ROOT = None

ENABLE_HTTPS = False
NOTIFY_ON_LOGIN = False
HTTPS_CERT = None
HTTPS_KEY = None

INDEXER_DEFAULT_LANGUAGE = None
EP_DEFAULT_DELETED_STATUS = None
LAUNCH_BROWSER = False
CACHE_DIR = None
ACTUAL_CACHE_DIR = None
ROOT_DIRS = []

TRASH_REMOVE_SHOW = False
TRASH_ROTATE_LOGS = False
SORT_ARTICLE = False
DEBUG = False
DBDEBUG = False
DISPLAY_ALL_SEASONS = True
DEFAULT_PAGE = 'home'
SEEDERS_LEECHERS_IN_NOTIFY = True


USE_LISTVIEW = False
METADATA_KODI = []
METADATA_KODI_12PLUS = []
METADATA_MEDIABROWSER = []
METADATA_PS3 = []
METADATA_WDTV = []
METADATA_TIVO = []
METADATA_MEDE8ER = []

QUALITY_DEFAULT = None
STATUS_DEFAULT = None
STATUS_DEFAULT_AFTER = None
FLATTEN_FOLDERS_DEFAULT = False
SUBTITLES_DEFAULT = False
INDEXER_DEFAULT = None
INDEXER_TIMEOUT = None
SCENE_DEFAULT = False
ANIME_DEFAULT = False
PROVIDER_ORDER = []

NAMING_MULTI_EP = False
NAMING_ANIME_MULTI_EP = False
NAMING_PATTERN = None
NAMING_ABD_PATTERN = None
NAMING_CUSTOM_ABD = False
NAMING_SPORTS_PATTERN = None
NAMING_CUSTOM_SPORTS = False
NAMING_ANIME_PATTERN = None
NAMING_CUSTOM_ANIME = False
NAMING_FORCE_FOLDERS = False
NAMING_STRIP_YEAR = False
NAMING_ANIME = None

USE_NZBS = False
USE_TORRENTS = False

NZB_METHOD = None
NZB_DIR = None
USENET_RETENTION = None
CACHE_TRIMMING = None
MAX_CACHE_AGE = None
TORRENT_METHOD = None
TORRENT_DIR = None
DOWNLOAD_PROPERS = False
CHECK_PROPERS_INTERVAL = None
PROPERS_SEARCH_DAYS = 2
REMOVE_FROM_CLIENT = False
ALLOW_HIGH_PRIORITY = False
SAB_FORCED = False
RANDOMIZE_PROVIDERS = False

AUTOPOSTPROCESSOR_FREQUENCY = None
DAILYSEARCH_FREQUENCY = None
UPDATE_FREQUENCY = None
BACKLOG_FREQUENCY = None
SHOWUPDATE_HOUR = None

DEFAULT_AUTOPOSTPROCESSOR_FREQUENCY = 10
DEFAULT_TORRENT_CHECKER_FREQUENCY = 60
DEFAULT_DAILYSEARCH_FREQUENCY = 40
DEFAULT_BACKLOG_FREQUENCY = 21
DEFAULT_UPDATE_FREQUENCY = 1
DEFAULT_SHOWUPDATE_HOUR = random.randint(2, 4)

MIN_AUTOPOSTPROCESSOR_FREQUENCY = 1
MIN_TORRENT_CHECKER_FREQUENCY = 30
MIN_DAILYSEARCH_FREQUENCY = 10
MIN_BACKLOG_FREQUENCY = 10
MIN_UPDATE_FREQUENCY = 1

BACKLOG_DAYS = 7

ADD_SHOWS_WO_DIR = False
CREATE_MISSING_SHOW_DIRS = False
RENAME_EPISODES = False
AIRDATE_EPISODES = False
FILE_TIMESTAMP_TIMEZONE = None
PROCESS_AUTOMATICALLY = False
NO_DELETE = False
KEEP_PROCESSED_DIR = False
PROCESS_METHOD = None
DELRARCONTENTS = False
MOVE_ASSOCIATED_FILES = False
POSTPONE_IF_SYNC_FILES = True
POSTPONE_IF_NO_SUBS = False
NFO_RENAME = True
TV_DOWNLOAD_DIR = None
UNPACK = False
SKIP_REMOVED_FILES = False
ALLOWED_EXTENSIONS = {'srt', 'nfo', 'sub', 'idx'}

NZBS = False
NZBS_UID = None
NZBS_HASH = None

OMGWTFNZBS = False
OMGWTFNZBS_USERNAME = None
OMGWTFNZBS_APIKEY = None

NEWZBIN = False
NEWZBIN_USERNAME = None
NEWZBIN_PASSWORD = None

SAB_USERNAME = None
SAB_PASSWORD = None
SAB_APIKEY = None
SAB_CATEGORY = None
SAB_CATEGORY_BACKLOG = None
SAB_CATEGORY_ANIME = None
SAB_CATEGORY_ANIME_BACKLOG = None
SAB_HOST = ''

NZBGET_USERNAME = None
NZBGET_PASSWORD = None
NZBGET_CATEGORY = None
NZBGET_CATEGORY_BACKLOG = None
NZBGET_CATEGORY_ANIME = None
NZBGET_CATEGORY_ANIME_BACKLOG = None
NZBGET_HOST = None
NZBGET_USE_HTTPS = False
NZBGET_PRIORITY = 100

TORRENT_USERNAME = None
TORRENT_PASSWORD = None
TORRENT_HOST = ''
TORRENT_PATH = ''
TORRENT_SEED_TIME = None
TORRENT_PAUSED = False
TORRENT_HIGH_BANDWIDTH = False
TORRENT_LABEL = ''
TORRENT_LABEL_ANIME = ''
TORRENT_VERIFY_CERT = False
TORRENT_RPCURL = 'transmission'
TORRENT_AUTH_TYPE = 'none'
TORRENT_SEED_LOCATION = None
TORRENT_CHECKER_FREQUENCY = None

USE_KODI = False
KODI_ALWAYS_ON = True
KODI_NOTIFY_ONSNATCH = False
KODI_NOTIFY_ONDOWNLOAD = False
KODI_NOTIFY_ONSUBTITLEDOWNLOAD = False
KODI_UPDATE_LIBRARY = False
KODI_UPDATE_FULL = False
KODI_UPDATE_ONLYFIRST = False
KODI_HOST = []
KODI_USERNAME = None
KODI_PASSWORD = None
KODI_LIBRARY_CLEAN_PENDING = False
KODI_CLEAN_LIBRARY = False

USE_PLEX_SERVER = False
PLEX_NOTIFY_ONSNATCH = False
PLEX_NOTIFY_ONDOWNLOAD = False
PLEX_NOTIFY_ONSUBTITLEDOWNLOAD = False
PLEX_UPDATE_LIBRARY = False
PLEX_SERVER_HOST = []
PLEX_SERVER_TOKEN = None
PLEX_CLIENT_HOST = []
PLEX_SERVER_USERNAME = None
PLEX_SERVER_PASSWORD = None

USE_PLEX_CLIENT = False
PLEX_CLIENT_USERNAME = None
PLEX_CLIENT_PASSWORD = None
PLEX_SERVER_HTTPS = None

USE_EMBY = False
EMBY_HOST = None
EMBY_APIKEY = None

USE_GROWL = False
GROWL_NOTIFY_ONSNATCH = False
GROWL_NOTIFY_ONDOWNLOAD = False
GROWL_NOTIFY_ONSUBTITLEDOWNLOAD = False
GROWL_HOST = ''
GROWL_PASSWORD = None

USE_FREEMOBILE = False
FREEMOBILE_NOTIFY_ONSNATCH = False
FREEMOBILE_NOTIFY_ONDOWNLOAD = False
FREEMOBILE_NOTIFY_ONSUBTITLEDOWNLOAD = False
FREEMOBILE_ID = ''
FREEMOBILE_APIKEY = ''

USE_TELEGRAM = False
TELEGRAM_NOTIFY_ONSNATCH = False
TELEGRAM_NOTIFY_ONDOWNLOAD = False
TELEGRAM_NOTIFY_ONSUBTITLEDOWNLOAD = False
TELEGRAM_ID = ''
TELEGRAM_APIKEY = ''

USE_PROWL = False
PROWL_NOTIFY_ONSNATCH = False
PROWL_NOTIFY_ONDOWNLOAD = False
PROWL_NOTIFY_ONSUBTITLEDOWNLOAD = False
PROWL_API = []
PROWL_PRIORITY = 0
PROWL_MESSAGE_TITLE = 'Medusa'

USE_TWITTER = False
TWITTER_NOTIFY_ONSNATCH = False
TWITTER_NOTIFY_ONDOWNLOAD = False
TWITTER_NOTIFY_ONSUBTITLEDOWNLOAD = False
TWITTER_USERNAME = None
TWITTER_PASSWORD = None
TWITTER_PREFIX = None
TWITTER_DMTO = None
TWITTER_USEDM = False

USE_BOXCAR2 = False
BOXCAR2_NOTIFY_ONSNATCH = False
BOXCAR2_NOTIFY_ONDOWNLOAD = False
BOXCAR2_NOTIFY_ONSUBTITLEDOWNLOAD = False
BOXCAR2_ACCESSTOKEN = None

USE_PUSHOVER = False
PUSHOVER_NOTIFY_ONSNATCH = False
PUSHOVER_NOTIFY_ONDOWNLOAD = False
PUSHOVER_NOTIFY_ONSUBTITLEDOWNLOAD = False
PUSHOVER_USERKEY = None
PUSHOVER_APIKEY = None
PUSHOVER_DEVICE = []
PUSHOVER_SOUND = None

USE_LIBNOTIFY = False
LIBNOTIFY_NOTIFY_ONSNATCH = False
LIBNOTIFY_NOTIFY_ONDOWNLOAD = False
LIBNOTIFY_NOTIFY_ONSUBTITLEDOWNLOAD = False

USE_NMJ = False
NMJ_HOST = None
NMJ_DATABASE = None
NMJ_MOUNT = None

ANIMESUPPORT = False
USE_ANIDB = False
ANIDB_USERNAME = None
ANIDB_PASSWORD = None
ANIDB_USE_MYLIST = False
ADBA_CONNECTION = None
ANIME_SPLIT_HOME = False

USE_SYNOINDEX = False

USE_NMJv2 = False
NMJv2_HOST = None
NMJv2_DATABASE = None
NMJv2_DBLOC = None

USE_SYNOLOGYNOTIFIER = False
SYNOLOGYNOTIFIER_NOTIFY_ONSNATCH = False
SYNOLOGYNOTIFIER_NOTIFY_ONDOWNLOAD = False
SYNOLOGYNOTIFIER_NOTIFY_ONSUBTITLEDOWNLOAD = False

USE_SLACK = False
SLACK_NOTIFY_SNATCH = None
SLACK_NOTIFY_DOWNLOAD = None
SLACK_NOTIFY_SUBTITLEDOWNLOAD = None
SLACK_WEBHOOK = None

USE_TRAKT = False
TRAKT_USERNAME = None
TRAKT_ACCESS_TOKEN = None
TRAKT_REFRESH_TOKEN = None
TRAKT_REMOVE_WATCHLIST = False
TRAKT_REMOVE_SERIESLIST = False
TRAKT_REMOVE_SHOW_FROM_APPLICATION = False
TRAKT_SYNC_WATCHLIST = False
TRAKT_METHOD_ADD = None
TRAKT_START_PAUSED = False
TRAKT_USE_RECOMMENDED = False
TRAKT_SYNC = False
TRAKT_SYNC_REMOVE = False
TRAKT_DEFAULT_INDEXER = None
TRAKT_TIMEOUT = None
TRAKT_BLACKLIST_NAME = None

USE_PYTIVO = False
PYTIVO_NOTIFY_ONSNATCH = False
PYTIVO_NOTIFY_ONDOWNLOAD = False
PYTIVO_NOTIFY_ONSUBTITLEDOWNLOAD = False
PYTIVO_UPDATE_LIBRARY = False
PYTIVO_HOST = ''
PYTIVO_SHARE_NAME = ''
PYTIVO_TIVO_NAME = ''

USE_NMA = False
NMA_NOTIFY_ONSNATCH = False
NMA_NOTIFY_ONDOWNLOAD = False
NMA_NOTIFY_ONSUBTITLEDOWNLOAD = False
NMA_API = []
NMA_PRIORITY = 0

USE_PUSHALOT = False
PUSHALOT_NOTIFY_ONSNATCH = False
PUSHALOT_NOTIFY_ONDOWNLOAD = False
PUSHALOT_NOTIFY_ONSUBTITLEDOWNLOAD = False
PUSHALOT_AUTHORIZATIONTOKEN = None

USE_PUSHBULLET = False
PUSHBULLET_NOTIFY_ONSNATCH = False
PUSHBULLET_NOTIFY_ONDOWNLOAD = False
PUSHBULLET_NOTIFY_ONSUBTITLEDOWNLOAD = False
PUSHBULLET_API = None
PUSHBULLET_DEVICE = None

USE_EMAIL = False
EMAIL_NOTIFY_ONSNATCH = False
EMAIL_NOTIFY_ONDOWNLOAD = False
EMAIL_NOTIFY_ONSUBTITLEDOWNLOAD = False
EMAIL_HOST = None
EMAIL_PORT = 25
EMAIL_TLS = False
EMAIL_USER = None
EMAIL_PASSWORD = None
EMAIL_FROM = None
EMAIL_LIST = []
EMAIL_SUBJECT = None

HOME_LAYOUT = None
HISTORY_LAYOUT = None
HISTORY_LIMIT = 0
DISPLAY_SHOW_SPECIALS = False
COMING_EPS_LAYOUT = None
COMING_EPS_DISPLAY_PAUSED = False
COMING_EPS_SORT = None
COMING_EPS_MISSED_RANGE = None
FUZZY_DATING = False
TRIM_ZERO = False
DATE_PRESET = None
TIME_PRESET = None
TIME_PRESET_W_SECONDS = None
TIMEZONE_DISPLAY = None
THEME_NAME = None
POSTER_SORTBY = None
POSTER_SORTDIR = None
FANART_BACKGROUND = None
FANART_BACKGROUND_OPACITY = None
SELECTED_ROOT = None
BACKLOG_PERIOD = None
BACKLOG_STATUS = None

USE_SUBTITLES = False
SUBTITLES_LANGUAGES = []
SUBTITLES_DIR = ''
SUBTITLES_SERVICES_LIST = []
SUBTITLES_SERVICES_ENABLED = []
SUBTITLES_HISTORY = False
SUBTITLES_PERFECT_MATCH = False
IGNORE_EMBEDDED_SUBS = False
ACCEPT_UNKNOWN_EMBEDDED_SUBS = False
SUBTITLES_STOP_AT_FIRST = False
SUBTITLES_HEARING_IMPAIRED = False
SUBTITLES_FINDER_FREQUENCY = 1
SUBTITLES_MULTI = False
SUBTITLES_EXTRA_SCRIPTS = []
SUBTITLES_PRE_SCRIPTS = []
SUBTITLES_KEEP_ONLY_WANTED = False
SUBTITLES_ERASE_CACHE = False

ADDIC7ED_USER = None
ADDIC7ED_PASS = None

ITASA_USER = None
ITASA_PASS = None

LEGENDASTV_USER = None
LEGENDASTV_PASS = None

OPENSUBTITLES_USER = None
OPENSUBTITLES_PASS = None

USE_FAILED_DOWNLOADS = False
DELETE_FAILED = False

EXTRA_SCRIPTS = []

IGNORE_WORDS = ['german', 'french', 'core2hd', 'dutch', 'swedish', 'reenc', 'MrLss', 'dubbed']

PREFERRED_WORDS = []

UNDESIRED_WORDS = ['internal', 'xvid']

TRACKERS_LIST = ['udp://tracker.coppersurfer.tk:6969/announce',
                 'udp://tracker.leechers-paradise.org:6969/announce',
                 'udp://tracker.zer0day.to:1337/announce', 'udp://tracker.opentrackr.org:1337/announce',
                 'http://tracker.opentrackr.org:1337/announce', 'udp://p4p.arenabg.com:1337/announce',
                 'http://p4p.arenabg.com:1337/announce', 'udp://explodie.org:6969/announce',
                 'udp://9.rarbg.com:2710/announce', 'http://explodie.org:6969/announce',
                 'http://tracker.dler.org:6969/announce', 'udp://public.popcorn-tracker.org:6969/announce',
                 'udp://tracker.internetwarriors.net:1337/announce', 'udp://ipv4.tracker.harry.lu:80/announce',
                 'http://ipv4.tracker.harry.lu:80/announce', 'udp://mgtracker.org:2710/announce',
                 'http://mgtracker.org:6969/announce', 'udp://tracker.mg64.net:6969/announce',
                 'http://tracker.mg64.net:6881/announce', 'http://torrentsmd.com:8080/announce']

REQUIRE_WORDS = []
IGNORED_SUBS_LIST = ['dk', 'fin', 'heb', 'kor', 'nor', 'nordic', 'pl', 'swe']
IGNORE_UND_SUBS = False
SYNC_FILES = ['!sync', 'lftp-pget-status', 'part', 'bts', '!qb', '!qB']

CALENDAR_UNPROTECTED = False
CALENDAR_ICONS = False
NO_RESTART = False

TMDB_API_KEY = 'edc5f123313769de83a71e157758030b'
# TRAKT_API_KEY = 'd4161a7a106424551add171e5470112e4afdaf2438e6ef2fe0548edc75924868'

TRAKT_API_KEY = '5c65f55e11d48c35385d9e8670615763a605fad28374c8ae553a7b7a50651ddd'
TRAKT_API_SECRET = 'b53e32045ac122a445ef163e6d859403301ffe9b17fb8321d428531b69022a82'
TRAKT_PIN_URL = 'https://trakt.tv/pin/4562'
TRAKT_OAUTH_URL = 'https://trakt.tv/'
TRAKT_API_URL = 'https://api.trakt.tv/'

FANART_API_KEY = '9b3afaf26f6241bdb57d6cc6bd798da7'

SHOWS_RECENT = []

__INITIALIZED__ = False

NEWZNAB_PROVIDERS = []

TORRENTRSS_PROVIDERS = []

RECENTLY_DELETED = set()

RECENTLY_POSTPROCESSED = {}

RELEASES_IN_PP = []

PRIVACY_LEVEL = 'normal'

PROPERS_SEARCH_INTERVAL = {'15m': 15, '45m': 45, '90m': 90, '4h': 4 * 60, 'daily': 24 * 60}

PROPERS_INTERVAL_LABELS = {'daily': '24 hours',
                           '4h': '4 hours',
                           '90m': '90 mins',
                           '45m': '45 mins',
                           '15m': '15 mins'
                           }

# Plex fallback settings
FALLBACK_PLEX_ENABLE = True
FALLBACK_PLEX_NOTIFICATIONS = True
FALLBACK_PLEX_TIMEOUT = 3
FALLBACK_PLEX_API_URL = 'https://tvdb2.plex.tv'
TVDB_API_KEY = '0629B785CE550C8D'
