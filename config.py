"""VELOCITY BOSNIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY BOSNIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "BOSNIAN"
HANDLE = "@velocitybosnian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "bs",
    "name": "Bosnian",
    "native_name": "Bosanski",
    "history_key": "bosnian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "bs-BA-GoranNeural",
    "native_fallback_voice": "bs-BA-VesnaNeural",
    "native_engine": "edge",
    "native_lang_code": "bs",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "BOSANSKI",
    "translit_label": "SAY IT LIKE",
    "greeting": "Zdravo!",
    "encouragement": "Odlično!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Pozdravi", "hand", "#1CB0F6"),
    ("Basic Phrases", "Osnovne Fraze", "chat", "#58CC02"),
    ("Common Expressions", "Uobičajeni Izrazi", "chat", "#1CB0F6"),
    ("Travel", "Putovanje", "plane", "#1CB0F6"),
    ("Restaurant", "Restoran", "fork", "#FF7A00"),
    ("Shopping", "Kupovina", "bag", "#E056A0"),
    ("Emergency", "Hitno", "siren", "#FF4B4B"),
    ("Family Terms", "Porodični Termini", "heart", "#E056A0"),
    ("Numbers", "Brojevi", "hash", "#A560E8"),
    ("Time", "Vrijeme", "clock", "#00A889"),
    ("Motivation", "Motivacija", "rocket", "#A560E8"),
    ("Love", "Ljubav", "heart", "#FF4B4B"),
    ("Success", "Uspjeh", "trophy", "#F5A700"),
    ("Wisdom", "Mudrost", "book", "#A560E8"),
    ("Happiness", "Sreća", "smile", "#F5A700"),
    ("Self Improvement", "Samopoboljšanje", "leaf", "#58CC02"),
    ("Gratitude", "Zahvalnost", "heart", "#FF7A00"),
    ("Friendship", "Prijateljstvo", "users", "#00A889"),
    ("Hope", "Nada", "sun", "#FF7A00"),
    ("Creativity", "Kreativnost", "palette", "#E056A0"),
    ("Inner Peace", "Unutrašnji Mir", "lotus", "#00A889"),
    ("Confidence", "Samopouzdanje", "shield", "#1CB0F6"),
    ("Perseverance", "Ustrajnost", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiracija", "sparkles", "#A560E8"),
    ("Positive Life", "Pozitivan Život", "sun", "#58CC02"),
    ("Courage", "Hrabrost", "shield", "#FF4B4B"),
    ("Kindness", "Ljubaznost", "heart", "#E056A0"),
    ("Patience", "Strpljenje", "hourglass", "#00A889"),
    ("Forgiveness", "Oproštaj", "hands", "#FF7A00"),
    ("Strength", "Snaga", "dumbbell", "#FF4B4B"),
    ("Joy", "Radost", "smile", "#F5A700"),
    ("Balance", "Ravnoteža", "scale", "#00A889"),
    ("Growth", "Rast", "sprout", "#58CC02"),
    ("Purpose", "Svrha", "target", "#A560E8"),
    ("Mindfulness", "Svjesnost", "lotus", "#00A889"),
    ("Daily Routine", "Dnevna rutina", "calendar", "#1CB0F6"),
    ("Weather", "Vrijeme", "cloud", "#1CB0F6"),
    ("Feelings", "Osjećanja", "smile", "#E056A0"),
    ("Food", "Hrana", "fork", "#FF7A00"),
    ("Health", "Zdravlje", "heart", "#58CC02"),
    ("Work", "Posao", "briefcase", "#1CB0F6"),
    ("Technology", "Tehnologija", "chip", "#A560E8"),
    ("Nature", "Priroda", "leaf", "#58CC02"),
    ("Animals", "Životinje", "paw", "#FF7A00"),
    ("Colors", "Boje", "palette", "#E056A0"),
    ("Directions", "Smjerovi", "compass", "#1CB0F6"),
    ("Body Parts", "Dijelovi tijela", "hand", "#00A889"),
    ("Clothes", "Odjeća", "shirt", "#E056A0"),
    ("Music", "Muzika", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Praznici", "gift", "#FF4B4B"),
    ("Education", "Obrazovanje", "book", "#1CB0F6"),
    ("Culture", "Kultura", "globe", "#00A889"),
    ("Finance", "Finansije", "coin", "#58CC02"),
    ("Relationships", "Odnosi", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnbosnian",
    "#bosnianlessons",
    "#bosnianforbeginners",
    "#languagelearning",
    "#bosnianvocabulary",
    "#velocitybosnian",
    "#dailybosnian",
    "#bosnian",
    "#learnlanguages",
    "#speakbosnian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
