import os
import sys
import time
import random
import threading
import shutil
from datetime import datetime
from typing import List, Dict, Optional
import warnings
warnings.filterwarnings('ignore')

# ==================== COLOR SYSTEM ====================

class GoblinColors:
    """Goblin themed color system"""

    # Goblin Base Colors
    GOBLIN_GREEN = '\033[38;5;46m'
    GOBLIN_DARK = '\033[38;5;22m'
    GOBLIN_GOLD = '\033[38;5;178m'
    GOBLIN_POISON = '\033[38;5;90m'
    GOBLIN_BLOOD = '\033[38;5;196m'
    GOBLIN_MOSS = '\033[38;5;64m'
    GOBLIN_SWAMP = '\033[38;5;28m'
    GOBLIN_SHADOW = '\033[38;5;235m'

    # Neon Accents
    NEON_GREEN = '\033[38;5;46m'
    NEON_CYAN = '\033[38;5;51m'
    NEON_PURPLE = '\033[38;5;129m'
    NEON_RED = '\033[38;5;196m'
    NEON_ORANGE = '\033[38;5;208m'
    NEON_YELLOW = '\033[38;5;226m'
    NEON_PINK = '\033[38;5;199m'
    NEON_BLUE = '\033[38;5;75m'
    NEON_LIME = '\033[38;5;118m'
    NEON_GOLD = '\033[38;5;178m'

    # Platform Colors
    IG = '\033[38;5;205m'
    THREADS = '\033[38;5;51m'
    FB = '\033[38;5;27m'
    TT = '\033[38;5;196m'

    # Base Colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

# ==================== ORIGINAL BANNER ====================

BANNER_ART = r'''
              .o######0o.
            o####" "######0.    (## m#o
            ####(    ######0  ._ ##.##"nn
            0####o   ###" ## (##o.######"
    o00o.    0#####o,##. ,#"  "#######(
  .0#####0.   0###########0     ########
 .0#######0.   "0#########"  _.o###'"00"
.0###########o._ ""################       _  .
0####" "#########################0      .0#0n0
#####.   ""#####################"    _  0#####
0#####.     "###################._.o##o.#####"
"0#####..##mn ""#############################
  "0#######""_    ""##################"#####"
     ""####m###m      ""############"   ####
    .########"""         .########"     "##"
    ####"##"###o        (0######"        ""
    "##".###,##     .o#o ""####.
         "##"      .0############.
                 .n##RADIUS#######
    AUTHOR : SYLHETYHACKVENGER (THE-ERROR808)               
'''

# ==================== BANNER RENDERER ====================

class BannerRenderer:
    @staticmethod
    def render_goblin_banner() -> str:
        lines = BANNER_ART.split('\n')
        result = []
        colors = [
            GoblinColors.GOBLIN_GREEN,
            GoblinColors.NEON_GREEN,
            GoblinColors.GOBLIN_GOLD,
            GoblinColors.GOBLIN_POISON,
            GoblinColors.GOBLIN_MOSS,
            GoblinColors.GOBLIN_SWAMP,
            GoblinColors.NEON_GOLD,
            GoblinColors.NEON_LIME,
        ]
        for i, line in enumerate(lines):
            if not line.strip():
                result.append(line)
                continue
            color = colors[i % len(colors)]
            result.append(color + line + GoblinColors.RESET)
        return '\n'.join(result)

# ==================== COMPLETE DORK GENERATOR ====================

class CompleteDorkGenerator:
    """Generate COMPLETE dork commands for all platforms with ALL tracking categories"""

    def __init__(self, username: str):
        self.username = username
        self.commands = {}

    def generate_all(self) -> Dict[str, List[str]]:
        """Generate all dorks"""
        self.commands = {
            'instagram': self._instagram_complete(),
            'threads': self._threads_complete(),
            'facebook': self._facebook_complete(),
            'tiktok': self._tiktok_complete()
        }
        return self.commands

    def _instagram_complete(self) -> List[str]:
        """COMPLETE Instagram dorks - ALL tracking categories"""
        cmds = []
        base = f'site:instagram.com "{self.username}"'

        # ====== 1. BASIC IDENTIFICATION ======
        cmds.extend([
            f'site:instagram.com "{self.username}"',
            f'site:instagram.com "@{self.username}"',
            f'site:instagram.com ("{self.username}" OR "@{self.username}")',
            f'site:instagram.com inurl:{self.username}',
            f'site:instagram.com intitle:"{self.username}"',
            f'site:instagram.com "{self.username}" "profile"',
            f'site:instagram.com "{self.username}" "account"',
            f'site:instagram.com "{self.username}" "user"',
        ])

        # ====== 2. PERSONAL INFORMATION ======
        personal = [
            'name', 'full name', 'first name', 'last name', 'age', 'birthday', 'birthdate',
            'gender', 'pronouns', 'she/her', 'he/him', 'they/them', 'nationality',
            'ethnicity', 'religion', 'language', 'bilingual', 'polyglot'
        ]
        for p in personal:
            cmds.append(f'{base} "{p}"')

        # ====== 3. CONTACT INFORMATION ======
        contact = [
            'email', 'phone', 'whatsapp', 'telegram', 'signal', 'discord', 'contact',
            'call', 'text', 'message', 'dm', 'direct message', 'inbox', 'mail',
            'gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'hotmail.com',
            'icloud.com', 'aol.com', 'mail.com', 'yandex.com', 'zoho.com'
        ]
        for c in contact:
            cmds.append(f'{base} {c}')

        # ====== 4. LOCATION TRACKING - COMPLETE ======
        locations = [
            # Current Location
            'location', 'current location', 'live in', 'based in', 'from', 'hometown',
            'city', 'state', 'country', 'region', 'area', 'neighborhood',

            # Specific Places
            'address', 'street', 'zip code', 'postal code', 'coordinates',
            'latitude', 'longitude', 'map', 'google maps',

            # Check-ins
            'check in', 'checked in', 'at', 'visiting', 'traveling to',
            'vacation', 'holiday', 'trip', 'tourist',

            # Popular Locations
            'new york', 'los angeles', 'london', 'paris', 'tokyo', 'sydney',
            'toronto', 'berlin', 'moscow', 'dubai', 'singapore',

            # Venues
            'restaurant', 'cafe', 'coffee shop', 'bar', 'club', 'gym',
            'fitness', 'studio', 'office', 'work', 'school', 'university',
            'college', 'library', 'park', 'beach', 'mall', 'store',

            # Travel
            'airport', 'flight', 'hotel', 'resort', 'airbnb', 'hostel',
            'road trip', 'roadtrip', 'adventure', 'explore',

            # Weather/Environment
            'weather', 'sunny', 'rainy', 'snow', 'beach', 'mountain',
            'lake', 'river', 'forest', 'desert', 'island'
        ]
        for l in locations:
            cmds.append(f'{base} {l}')

        # ====== 5. SOCIAL ACTIVITIES ======
        social = [
            'friends', 'best friend', 'bff', 'squad', 'crew', 'family',
            'mom', 'dad', 'brother', 'sister', 'son', 'daughter',
            'partner', 'boyfriend', 'girlfriend', 'husband', 'wife',
            'date', 'dating', 'relationship', 'married', 'single',
            'party', 'celebration', 'birthday', 'anniversary',
            'wedding', 'engagement', 'baby', 'pregnancy', 'kids',
            'pet', 'dog', 'cat', 'puppy', 'kitten'
        ]
        for s in social:
            cmds.append(f'{base} {s}')

        # ====== 6. PROFESSIONAL & EDUCATION ======
        professional = [
            'work', 'job', 'career', 'profession', 'occupation', 'employed',
            'company', 'agency', 'firm', 'startup', 'entrepreneur',
            'ceo', 'founder', 'director', 'manager', 'developer',
            'engineer', 'designer', 'artist', 'musician', 'writer',
            'teacher', 'student', 'graduate', 'alumni', 'phd',
            'university', 'college', 'school', 'high school', 'major',
            'degree', 'bachelor', 'master', 'doctorate', 'internship'
        ]
        for p in professional:
            cmds.append(f'{base} {p}')

        # ====== 7. INTERESTS & HOBBIES ======
        interests = [
            'hobby', 'interest', 'passion', 'obsessed', 'addicted',
            'gaming', 'gamer', 'guitar', 'piano', 'music', 'song',
            'dance', 'singing', 'art', 'drawing', 'painting', 'photography',
            'sports', 'fitness', 'yoga', 'running', 'cycling', 'swimming',
            'reading', 'books', 'writing', 'poetry', 'film', 'movies',
            'travel', 'food', 'cooking', 'baking', 'fashion', 'shopping',
            'tech', 'coding', 'programming', 'ai', 'crypto', 'blockchain'
        ]
        for i in interests:
            cmds.append(f'{base} {i}')

        # ====== 8. CONTENT TYPES ======
        content = [
            'profile', 'posts', 'photo', 'video', 'reel', 'stories', 'igtv',
            'highlight', 'tagged', 'mention', 'feed', 'story', 'archive',
            'post', 'picture', 'pic', 'selfie', 'portrait', 'landscape',
            'memes', 'meme', 'funny', 'humor', 'jokes'
        ]
        for c in content:
            cmds.append(f'{base} {c}')

        # ====== 9. ENGAGEMENT ======
        engagement = [
            'liked', 'comments', 'shared', 'saved', 'viewed', 'likes',
            'comment', 'share', 'save', 'view', 'engagement', 'interaction',
            'react', 'reply', 'response', 'feedback', 'opinion'
        ]
        for e in engagement:
            cmds.append(f'{base} "{e}"')

        # ====== 10. BUSINESS & MARKETING ======
        business = [
            'business', 'brand', 'sponsored', 'shop', 'product', 'store',
            'company', 'agency', 'marketing', 'advertising', 'promotion',
            'collab', 'partnership', 'affiliate', 'influencer', 'creator',
            'selling', 'buy', 'order', 'discount', 'sale', 'offer',
            'promo code', 'coupon', 'deal', 'bargain', 'wholesale'
        ]
        for b in business:
            cmds.append(f'{base} {b}')

        # ====== 11. VERIFICATION & STATUS ======
        verification = [
            'verified', 'official', 'authentic', 'real', 'genuine', 'legit',
            'trusted', 'credible', 'reliable', 'established', 'professional'
        ]
        for v in verification:
            cmds.append(f'{base} {v}')

        # ====== 12. FILE TYPES ======
        file_types = [
            'jpg', 'png', 'gif', 'mp4', 'jpeg', 'webp', 'avi', 'mov',
            'svg', 'pdf', 'doc', 'txt', 'zip', 'rar', 'exe'
        ]
        for f in file_types:
            cmds.append(f'{base} filetype:{f}')

        # ====== 13. TIME-BASED SEARCHES ======
        time_searches = [
            'after:2020-01-01', 'after:2021-01-01', 'after:2022-01-01',
            'after:2023-01-01', 'after:2024-01-01', 'after:2025-01-01',
            'after:2026-01-01', 'before:2020-01-01', 'before:2021-01-01',
            'before:2022-01-01', 'before:2023-01-01', 'before:2024-01-01'
        ]
        for t in time_searches:
            cmds.append(f'{base} {t}')

        # ====== 14. URL STRUCTURES ======
        urls = [
            f'site:instagram.com/{self.username}',
            f'site:instagram.com/p/ "{self.username}"',
            f'site:instagram.com/reel/ "{self.username}"',
            f'site:instagram.com/stories/ "{self.username}"',
            f'site:instagram.com/tv/ "{self.username}"',
            f'site:instagram.com/guide/ "{self.username}"',
            f'site:instagram.com/s/ "{self.username}"',
            f'site:instagram.com/explore/ "{self.username}"'
        ]
        cmds.extend(urls)

        # ====== 15. BIO & LINKS ======
        bio_links = [
            'bio', 'biography', 'about', 'description', 'intro',
            'link', 'http', 'https', 'website', 'url', 'click', 'tap',
            '.com', '.org', '.net', '.io', '.co', '.uk', '.us',
            'linktree', 'linktr.ee', 'bit.ly', 'tinyurl', 'bio.link'
        ]
        for b in bio_links:
            cmds.append(f'{base} {b}')

        # ====== 16. EMOTIONS & SENTIMENT ======
        sentiments = [
            'love', 'hate', 'good', 'bad', 'amazing', 'terrible',
            'awesome', 'horrible', 'great', 'awful', 'perfect', 'worst',
            'happy', 'sad', 'excited', 'anxious', 'grateful', 'blessed',
            'depressed', 'lonely', 'stressed', 'relaxed', 'peaceful',
            'angry', 'frustrated', 'proud', 'ashamed', 'guilty'
        ]
        for s in sentiments:
            cmds.append(f'{base} "{s}"')

        # ====== 17. HASHTAGS ======
        hashtags = [
            f'{base} "#"',
            f'{base} "#{self.username}"',
            f'{base} "#{self.username}love"',
            f'{base} "#{self.username}fan"',
            f'{base} "#{self.username}official"',
            f'{base} "#{self.username}gram"',
            f'{base} "#{self.username}life"',
            f'{base} "#{self.username}style"',
            f'{base} "#{self.username}fashion"',
            f'{base} "#{self.username}photography"'
        ]
        cmds.extend(hashtags)

        # ====== 18. ACTIVITIES & EVENTS ======
        activities = [
            'event', 'party', 'concert', 'festival', 'exhibition',
            'workshop', 'seminar', 'conference', 'meeting', 'interview',
            'date', 'lunch', 'dinner', 'breakfast', 'brunch',
            'workout', 'exercise', 'training', 'practice', 'rehearsal',
            'performance', 'show', 'premiere', 'opening', 'launch'
        ]
        for a in activities:
            cmds.append(f'{base} {a}')

        # ====== 19. ACHIEVEMENTS & AWARDS ======
        achievements = [
            'achievement', 'award', 'prize', 'recognition', 'honor',
            'winner', 'champion', 'victory', 'success', 'accomplishment',
            'graduate', 'certification', 'license', 'qualification'
        ]
        for a in achievements:
            cmds.append(f'{base} {a}')

        # ====== 20. QUOTES & CAPTIONS ======
        quotes = [
            '"life"', '"dream"', '"goals"', '"success"', '"motivation"',
            '"inspiration"', '"believe"', '"achieve"', '"persevere"',
            '"strength"', '"courage"', '"wisdom"', '"knowledge"'
        ]
        for q in quotes:
            cmds.append(f'{base} {q}')

        # ====== 21. BRANDS & PARTNERSHIPS ======
        brands = [
            'nike', 'adidas', 'gucci', 'prada', 'chanel', 'dior',
            'apple', 'samsung', 'sony', 'microsoft', 'google',
            'netflix', 'spotify', 'amazon', 'disney', 'marvel',
            'starbucks', 'mcdonalds', 'coca cola', 'pepsi'
        ]
        for b in brands:
            cmds.append(f'{base} {b}')

        # ====== 22. SPECIFIC SEARCH PATTERNS ======
        specific = [
            f'{base} "follow"',
            f'{base} "like"',
            f'{base} "comment"',
            f'{base} "dm"',
            f'{base} "collab"',
            f'{base} "sponsor"',
            f'{base} "ad"',
            f'{base} "promo"',
            f'{base} "discount"',
            f'{base} "offer"',
            f'{base} "sale"',
            f'{base} "event"',
            f'{base} "workshop"',
            f'{base} "tutorial"',
            f'{base} "review"',
            f'{base} "testimonial"',
            f'{base} "recommend"',
            f'{base} "refer"',
            f'{base} "support"',
            f'{base} "donate"',
            f'{base} "volunteer"',
            f'{base} "contribute"'
        ]
        cmds.extend(specific)

        # ====== 23. FAMILY & RELATIONSHIPS ======
        family = [
            'family', 'relative', 'cousin', 'aunt', 'uncle', 'grandparent',
            'grandma', 'grandpa', 'niece', 'nephew', 'godparent',
            'stepmom', 'stepdad', 'half-brother', 'half-sister',
            'fiance', 'fiancee', 'engaged', 'wedding', 'anniversary'
        ]
        for f in family:
            cmds.append(f'{base} {f}')

        # ====== 24. DAILY ROUTINE ======
        routine = [
            'morning', 'afternoon', 'evening', 'night', 'daily',
            'routine', 'schedule', 'habit', 'weekday', 'weekend',
            'breakfast', 'lunch', 'dinner', 'snack', 'coffee',
            'workout', 'yoga', 'meditation', 'journal', 'reading'
        ]
        for r in routine:
            cmds.append(f'{base} {r}')

        # ====== 25. TRAVEL & EXPLORATION ======
        travel = [
            'travel', 'trip', 'journey', 'adventure', 'exploration',
            'backpacking', 'hiking', 'camping', 'sightseeing', 'tour',
            'beach', 'mountain', 'lake', 'river', 'waterfall',
            'sunset', 'sunrise', 'nature', 'landscape', 'panorama'
        ]
        for t in travel:
            cmds.append(f'{base} {t}')

        return list(set(cmds))

    def _threads_complete(self) -> List[str]:
        """COMPLETE Threads dorks"""
        cmds = []
        base = f'site:threads.net "{self.username}"'

        # Basic
        cmds.extend([
            f'site:threads.net "{self.username}"',
            f'site:threads.net "@{self.username}"',
            f'site:threads.net ("{self.username}" OR "@{self.username}")',
            f'site:threads.net inurl:{self.username}',
        ])

        # Personal Info
        personal = ['name', 'age', 'birthday', 'gender', 'location', 'city', 'country']
        for p in personal:
            cmds.append(f'{base} {p}')

        # Contact
        contact = ['email', 'phone', 'contact', 'gmail.com', 'yahoo.com']
        for c in contact:
            cmds.append(f'{base} {c}')

        # Location Tracking
        locations = ['location', 'city', 'state', 'country', 'address', 'zip code', 'check in', 'visiting', 'travel']
        for l in locations:
            cmds.append(f'{base} {l}')

        # Content
        content = ['profile', 'posts', 'thread', 'reply', 'mention', 'tagged', 'feed', 'conversation', 'discussion']
        for c in content:
            cmds.append(f'{base} {c}')

        # Engagement
        engagement = ['likes', 'replies', 'reposts', 'quotes', 'share', 'comment', 'react']
        for e in engagement:
            cmds.append(f'{base} "{e}"')

        # Business
        business = ['business', 'brand', 'company', 'agency', 'work', 'job', 'career']
        for b in business:
            cmds.append(f'{base} {b}')

        # Verification
        for v in ['verified', 'official']:
            cmds.append(f'{base} {v}')

        # File types
        for f in ['jpg', 'png', 'jpeg', 'gif']:
            cmds.append(f'{base} filetype:{f}')

        # Time
        for d in ['after:2023-01-01', 'after:2024-01-01', 'after:2025-01-01']:
            cmds.append(f'{base} {d}')

        # URLs
        cmds.extend([
            f'site:threads.net/{self.username}',
            f'site:threads.net/t/ "{self.username}"',
            f'site:threads.net/post/ "{self.username}"',
        ])

        # Bio/Links
        for b in ['bio', 'link', 'http', 'https', '.com']:
            cmds.append(f'{base} {b}')

        # Emotions
        for s in ['love', 'hate', 'good', 'bad', 'great', 'awful', 'happy', 'sad']:
            cmds.append(f'{base} "{s}"')

        # Hashtags
        cmds.extend([
            f'{base} "#"',
            f'{base} "#{self.username}"',
        ])

        # Social
        social = ['friends', 'family', 'partner', 'date', 'party', 'celebration']
        for s in social:
            cmds.append(f'{base} {s}')

        # Interests
        interests = ['music', 'art', 'sports', 'fitness', 'travel', 'food', 'tech']
        for i in interests:
            cmds.append(f'{base} {i}')

        return list(set(cmds))

    def _facebook_complete(self) -> List[str]:
        """COMPLETE Facebook dorks"""
        cmds = []
        base = f'site:facebook.com "{self.username}"'

        # Basic
        cmds.extend([
            f'site:facebook.com "{self.username}"',
            f'site:facebook.com "@{self.username}"',
            f'site:facebook.com ("{self.username}" OR "@{self.username}")',
            f'site:facebook.com inurl:{self.username}',
            f'site:facebook.com intitle:"{self.username}"',
        ])

        # Personal Info
        personal = [
            'name', 'full name', 'age', 'birthday', 'gender', 'nationality',
            'religion', 'language', 'pronouns', 'relationship', 'single', 'married'
        ]
        for p in personal:
            cmds.append(f'{base} "{p}"')

        # Contact
        contact = ['email', 'phone', 'whatsapp', 'messenger', 'gmail.com', 'yahoo.com', 'hotmail.com']
        for c in contact:
            cmds.append(f'{base} {c}')

        # Location Tracking - COMPLETE
        locations = [
            'location', 'current location', 'live in', 'from', 'hometown',
            'city', 'state', 'country', 'address', 'zip code',
            'check in', 'checked in', 'visiting', 'travel',
            'restaurant', 'cafe', 'school', 'university', 'work', 'office'
        ]
        for l in locations:
            cmds.append(f'{base} {l}')

        # Content
        content = ['profile', 'posts', 'photo', 'video', 'status', 'story', 'live', 'page', 'group', 'event', 'album']
        for c in content:
            cmds.append(f'{base} {c}')

        # Engagement
        engagement = ['likes', 'comments', 'shares', 'reactions', 'love', 'haha', 'wow', 'sad', 'angry']
        for e in engagement:
            cmds.append(f'{base} "{e}"')

        # Business
        business = ['business', 'brand', 'sponsored', 'ad', 'page', 'company', 'agency', 'shop', 'store', 'work']
        for b in business:
            cmds.append(f'{base} {b}')

        # Verification
        for v in ['verified', 'official']:
            cmds.append(f'{base} {v}')

        # File types
        for f in ['jpg', 'png', 'mp4', 'jpeg', 'gif']:
            cmds.append(f'{base} filetype:{f}')

        # Time
        for d in ['after:2023-01-01', 'after:2024-01-01', 'after:2025-01-01']:
            cmds.append(f'{base} {d}')

        # URLs
        cmds.extend([
            f'site:facebook.com/{self.username}',
            f'site:facebook.com/profile.php "{self.username}"',
            f'site:facebook.com/posts/ "{self.username}"',
            f'site:facebook.com/groups/ "{self.username}"',
            f'site:facebook.com/events/ "{self.username}"',
        ])

        # About
        about = ['about', 'bio', 'info', 'contact', 'website', 'details', 'description']
        for a in about:
            cmds.append(f'{base} {a}')

        # Emotions
        for s in ['love', 'hate', 'good', 'bad', 'great', 'awful', 'happy', 'sad']:
            cmds.append(f'{base} "{s}"')

        # Education
        education = ['school', 'university', 'college', 'graduate', 'alumni', 'degree']
        for e in education:
            cmds.append(f'{base} {e}')

        # Family
        family = ['family', 'mom', 'dad', 'brother', 'sister', 'son', 'daughter', 'partner']
        for f in family:
            cmds.append(f'{base} {f}')

        # Interests
        interests = ['hobby', 'music', 'art', 'sports', 'travel', 'food', 'gaming']
        for i in interests:
            cmds.append(f'{base} {i}')

        # Activities
        activities = ['event', 'party', 'concert', 'festival', 'workshop', 'conference']
        for a in activities:
            cmds.append(f'{base} {a}')

        cmds.append(f'{base} "#"')

        return list(set(cmds))

    def _tiktok_complete(self) -> List[str]:
        """COMPLETE TikTok dorks"""
        cmds = []
        base = f'site:tiktok.com "{self.username}"'

        # Basic
        cmds.extend([
            f'site:tiktok.com "{self.username}"',
            f'site:tiktok.com "@{self.username}"',
            f'site:tiktok.com ("{self.username}" OR "@{self.username}")',
            f'site:tiktok.com inurl:{self.username}',
        ])

        # Personal Info
        personal = ['name', 'age', 'birthday', 'gender', 'location', 'city', 'country']
        for p in personal:
            cmds.append(f'{base} {p}')

        # Contact
        contact = ['email', 'phone', 'instagram', 'twitter', 'youtube', 'gmail.com']
        for c in contact:
            cmds.append(f'{base} {c}')

        # Location Tracking
        locations = ['location', 'city', 'state', 'country', 'address', 'check in', 'travel', 'beach', 'mountain']
        for l in locations:
            cmds.append(f'{base} {l}')

        # Content
        content = ['profile', 'video', 'post', 'tagged', 'mention', 'live', 'story', 'series']
        for c in content:
            cmds.append(f'{base} {c}')

        # Engagement
        engagement = ['likes', 'comments', 'shares', 'saved', 'views', 'duet', 'stitch']
        for e in engagement:
            cmds.append(f'{base} "{e}"')

        # Business
        business = ['business', 'brand', 'sponsored', 'creator', 'influencer', 'company', 'agency']
        for b in business:
            cmds.append(f'{base} {b}')

        # Verification
        for v in ['verified', 'official']:
            cmds.append(f'{base} {v}')

        # File types
        for f in ['mp4', 'jpg', 'png', 'jpeg', 'gif']:
            cmds.append(f'{base} filetype:{f}')

        # Time
        for d in ['after:2023-01-01', 'after:2024-01-01', 'after:2025-01-01']:
            cmds.append(f'{base} {d}')

        # URLs
        cmds.extend([
            f'site:tiktok.com/@{self.username}',
            f'site:tiktok.com/video/ "{self.username}"',
            f'site:tiktok.com/music/ "{self.username}"',
            f'site:tiktok.com/sound/ "{self.username}"',
        ])

        # Bio/Links
        for b in ['bio', 'link', 'http', 'https', '.com']:
            cmds.append(f'{base} {b}')

        # Music & Sounds
        for m in ['music', 'sound', 'song', 'audio', 'track']:
            cmds.append(f'{base} {m}')

        # Effects
        for e in ['effect', 'filter', 'transition']:
            cmds.append(f'{base} {e}')

        # Emotions
        for s in ['love', 'hate', 'good', 'bad', 'viral', 'trending', 'funny', 'happy', 'sad']:
            cmds.append(f'{base} "{s}"')

        # Hashtags
        cmds.extend([
            f'{base} "#"',
            f'{base} "#{self.username}"',
            f'{base} challenge',
            f'{base} duet',
            f'{base} stitch',
            f'{base} trend',
            f'{base} dance',
            f'{base} tutorial',
            f'{base} review',
            f'{base} unboxing',
            f'{base} reaction',
            f'{base} "POV"',
            f'{base} "fyp"',
            f'{base} "foryou"',
        ])

        # Interests
        interests = ['art', 'music', 'dance', 'sports', 'fitness', 'food', 'travel', 'gaming']
        for i in interests:
            cmds.append(f'{base} {i}')

        # Activities
        activities = ['challenge', 'trend', 'viral', 'popular', 'funny', 'dance', 'comedy']
        for a in activities:
            cmds.append(f'{base} {a}')

        return list(set(cmds))

# ==================== PROGRESS BAR ====================

class ProgressBar:
    def __init__(self, total: int, width: int = 50):
        self.total = total
        self.current = 0
        self.width = width
        self.running = True
        self._thread = None
        self.description = ""

    def start(self, description: str = ""):
        self.description = description
        def animate():
            while self.running and self.current < self.total:
                progress = self.current / self.total if self.total > 0 else 0
                filled = int(self.width * progress)
                bar = '█' * filled + '░' * (self.width - filled)

                if progress < 0.3:
                    color = GoblinColors.GOBLIN_BLOOD
                elif progress < 0.6:
                    color = GoblinColors.GOBLIN_GOLD
                elif progress < 0.9:
                    color = GoblinColors.GOBLIN_GREEN
                else:
                    color = GoblinColors.NEON_GREEN

                sys.stdout.write('\r\033[K')
                if self.description:
                    sys.stdout.write(f"{GoblinColors.GOBLIN_MOSS}{self.description}{GoblinColors.RESET} ")
                sys.stdout.write(f"{color}│{bar}│ {int(progress * 100)}%{GoblinColors.RESET}")
                sys.stdout.flush()
                time.sleep(0.05)

        self._thread = threading.Thread(target=animate, daemon=True)
        self._thread.start()

    def update(self, increment: int = 1):
        self.current = min(self.current + increment, self.total)

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join(timeout=0.1)
        print()

# ==================== SAVE MANAGER ====================

class SaveManager:
    @staticmethod
    def save_dorks(username: str, commands: Dict[str, List[str]]) -> List[str]:
        files = []
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        for platform, cmds in commands.items():
            filename = f"dorks_{platform}_{username}_{timestamp}.txt"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("═" * 80 + "\n")
                    f.write(f"  GOBLIN TSUNAMI - COMPLETE {platform.upper()} TRACKING\n")
                    f.write(f"  Username: @{username}\n")
                    f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"  Total Dorks: {len(cmds)}\n")
                    f.write("═" * 80 + "\n\n")
                    f.write("  COMPREHENSIVE TRACKING DORKS\n")
                    f.write("─" * 80 + "\n\n")

                    for i, cmd in enumerate(cmds, 1):
                        f.write(f"{i:4}. {cmd}\n")

                files.append(filename)
            except Exception:
                pass

        filename = f"dorks_all_{username}_{timestamp}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("═" * 80 + "\n")
                f.write(f"  GOBLIN TSUNAMI - COMPLETE ALL PLATFORMS\n")
                f.write(f"  Username: @{username}\n")
                f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"  Total: {sum(len(c) for c in commands.values())}\n")
                f.write("═" * 80 + "\n\n")

                f.write("  TABLE OF CONTENTS\n")
                f.write("─" * 80 + "\n")
                for platform, cmds in commands.items():
                    f.write(f"  📱 {platform.upper()}: {len(cmds)} dorks\n")
                f.write("─" * 80 + "\n\n")

                for platform, cmds in commands.items():
                    f.write(f"\n  {platform.upper()} ({len(cmds)} commands)\n")
                    f.write("─" * 80 + "\n\n")
                    for i, cmd in enumerate(cmds, 1):
                        f.write(f"{i:4}. {cmd}\n")

            files.append(filename)
        except Exception:
            pass

        return files

# ==================== PAGINATOR ====================

class Paginator:
    def __init__(self, items: List[str], page_size: int = 25):
        self.items = items
        self.page_size = page_size
        self.total_pages = (len(items) + page_size - 1) // page_size if items else 1
        self.current_page = 0

    def get_page(self) -> List[str]:
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def next(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            return True
        return False

    def prev(self):
        if self.current_page > 0:
            self.current_page -= 1
            return True
        return False

    def get_info(self) -> str:
        return f"Page {self.current_page + 1}/{self.total_pages} ({len(self.items)} total)"

# ==================== MAIN APPLICATION ====================

class GoblinTsunami:
    def __init__(self):
        self.save_manager = SaveManager()
        self.paginator = None

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def render_header(self):
        self.clear_screen()
        print(GoblinColors.GOBLIN_GREEN + "=" * 80 + GoblinColors.RESET)
        print(BannerRenderer.render_goblin_banner())
        print(GoblinColors.GOBLIN_GOLD + "=" * 80 + GoblinColors.RESET)
        print(f"{GoblinColors.GOBLIN_GREEN}🐉 GOBLIN TSUNAMI - COMPLETE PERSON TRACKING{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_MOSS}📸 Instagram  🧵 Threads  📘 Facebook  🎵 TikTok{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}🔥 COMPLETE TRACKING - LOCATION - ACTIVITIES - ALL CATEGORIES{GoblinColors.RESET}")
        print(GoblinColors.GOBLIN_GREEN + "=" * 80 + GoblinColors.RESET)
        print()

    def get_username(self) -> str:
        print(f"{GoblinColors.GOBLIN_GREEN}┌{'─' * 78}┐{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}│{GoblinColors.RESET}  {GoblinColors.BOLD}{GoblinColors.GOBLIN_GOLD}ENTER TARGET USERNAME{GoblinColors.RESET}  {GoblinColors.GOBLIN_GREEN}│{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}└{'─' * 78}┘{GoblinColors.RESET}")
        username = input(f"\n{GoblinColors.NEON_GREEN}➜ {GoblinColors.WHITE}Username: {GoblinColors.RESET}").strip()
        return username

    def generate_dorks(self, username: str) -> Dict[str, List[str]]:
        print(f"\n{GoblinColors.GOBLIN_GREEN}⏳ Generating COMPLETE tracking dorks for @{username}...{GoblinColors.RESET}")

        generator = CompleteDorkGenerator(username)
        commands = {}

        platforms = ['instagram', 'threads', 'facebook', 'tiktok']
        progress = ProgressBar(len(platforms))
        progress.start("Generating Comprehensive Dorks")

        for i, platform in enumerate(platforms, 1):
            commands[platform] = getattr(generator, f'_{platform}_complete')()
            progress.current = i
            time.sleep(0.05)

        progress.stop()
        print()

        return commands

    def display_comprehensive_dorks(self, commands: Dict[str, List[str]]):
        platforms = {
            'instagram': ('📸 Instagram', GoblinColors.IG),
            'threads': ('🧵 Threads', GoblinColors.THREADS),
            'facebook': ('📘 Facebook', GoblinColors.FB),
            'tiktok': ('🎵 TikTok', GoblinColors.TT)
        }

        for platform, (name, color) in platforms.items():
            cmds = commands[platform]
            total = len(cmds)

            print(f"\n{color}{'═' * 80}{GoblinColors.RESET}")
            print(f"{color}{GoblinColors.BOLD}{name} - {total} COMPLETE TRACKING DORKS{GoblinColors.RESET}")
            print(f"{color}{'═' * 80}{GoblinColors.RESET}")

            self.paginator = Paginator(cmds, page_size=25)
            showing_all = True

            while showing_all:
                self.clear_screen()
                self.render_header()

                print(f"\n{color}{'═' * 80}{GoblinColors.RESET}")
                print(f"{color}{GoblinColors.BOLD}{name} - {total} DORKS ({self.paginator.get_info()}){GoblinColors.RESET}")
                print(f"{color}{'═' * 80}{GoblinColors.RESET}")

                page_items = self.paginator.get_page()
                for i, cmd in enumerate(page_items, self.paginator.current_page * self.paginator.page_size + 1):
                    print(f"{color}{i:4}.{GoblinColors.RESET} {cmd}")

                print(f"\n{color}{'─' * 80}{GoblinColors.RESET}")
                print(f"{GoblinColors.GOBLIN_GOLD}{GoblinColors.BOLD}📄 {self.paginator.get_info()}{GoblinColors.RESET}")
                print(f"{color}{'─' * 80}{GoblinColors.RESET}")
                print(f"{GoblinColors.GOBLIN_MOSS}Controls: [N]ext  [P]revious  [Q]uit this platform{GoblinColors.RESET}")

                choice = input(f"\n{GoblinColors.NEON_GREEN}➜ {GoblinColors.WHITE}Choice: {GoblinColors.RESET}").strip().lower()

                if choice == 'n':
                    if not self.paginator.next():
                        print(f"\n{GoblinColors.GOBLIN_BLOOD}📄 Already on last page!{GoblinColors.RESET}")
                        time.sleep(0.5)
                elif choice == 'p':
                    if not self.paginator.prev():
                        print(f"\n{GoblinColors.GOBLIN_BLOOD}📄 Already on first page!{GoblinColors.RESET}")
                        time.sleep(0.5)
                elif choice == 'q':
                    showing_all = False
                else:
                    print(f"\n{GoblinColors.GOBLIN_BLOOD}❌ Invalid choice! Use N, P, or Q{GoblinColors.RESET}")
                    time.sleep(0.5)

            print(f"\n{color}{'─' * 80}{GoblinColors.RESET}")
            print(f"{GoblinColors.GOBLIN_GREEN}✅ {name} - {total} dorks reviewed{GoblinColors.RESET}")
            print(f"{color}{'─' * 80}{GoblinColors.RESET}")

            if platform != 'tiktok':
                time.sleep(1)

    def display_summary(self, commands: Dict[str, List[str]]):
        total = sum(len(c) for c in commands.values())

        print(f"\n{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}{GoblinColors.BOLD}📊 COMPLETE TRACKING SUMMARY{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")

        platforms = {
            'instagram': (GoblinColors.IG, 'Instagram'),
            'threads': (GoblinColors.THREADS, 'Threads'),
            'facebook': (GoblinColors.FB, 'Facebook'),
            'tiktok': (GoblinColors.TT, 'TikTok')
        }

        for platform, (color, name) in platforms.items():
            count = len(commands.get(platform, []))
            bar_length = min(50, count // 3)
            bar = '█' * bar_length + '░' * (50 - bar_length)
            print(f"  {color}{name:12}{GoblinColors.RESET} {color}│{bar}│ {count:4} dorks{GoblinColors.RESET}")

        print(f"\n  {GoblinColors.GOBLIN_GREEN}{GoblinColors.BOLD}Total Unique Dorks:{GoblinColors.RESET} {total}")
        print(f"  {GoblinColors.GOBLIN_GOLD}{GoblinColors.BOLD}Average per Platform:{GoblinColors.RESET} {total // 4}")
        print(f"  {GoblinColors.GOBLIN_MOSS}{GoblinColors.BOLD}Categories Covered:{GoblinColors.RESET} 25+ Tracking Categories")
        print(f"{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")

    def display_saved_files(self, files: List[str]):
        print(f"\n{GoblinColors.GOBLIN_GREEN}{GoblinColors.BOLD}✅ FILES SAVED{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}{'─' * 80}{GoblinColors.RESET}")
        for file in files:
            file_size = os.path.getsize(file) if os.path.exists(file) else 0
            size_str = f"{file_size:,} bytes" if file_size < 1024 * 1024 else f"{file_size / (1024 * 1024):.2f} MB"
            print(f"  {GoblinColors.GOBLIN_GREEN}✓{GoblinColors.RESET} {file} ({size_str})")
        print(f"{GoblinColors.GOBLIN_GOLD}{'─' * 80}{GoblinColors.RESET}")
        print(f"  {GoblinColors.GOBLIN_GREEN}Total:{GoblinColors.RESET} {len(files)} files saved")
        print(f"{GoblinColors.GOBLIN_GOLD}{'─' * 80}{GoblinColors.RESET}")

    def run(self):
        try:
            self.render_header()

            username = self.get_username()

            if not username:
                print(f"\n{GoblinColors.GOBLIN_BLOOD}❌ Username required!{GoblinColors.RESET}")
                time.sleep(2)
                return

            commands = self.generate_dorks(username)
            self.display_comprehensive_dorks(commands)
            self.display_summary(commands)

            print(f"\n{GoblinColors.GOBLIN_GOLD}┌{'─' * 78}┐{GoblinColors.RESET}")
            print(f"{GoblinColors.GOBLIN_GOLD}│{GoblinColors.RESET}  {GoblinColors.BOLD}💾 SAVE COMPLETE TRACKING RESULTS?{GoblinColors.RESET}  {GoblinColors.GOBLIN_GOLD}│{GoblinColors.RESET}")
            print(f"{GoblinColors.GOBLIN_GOLD}└{'─' * 78}┘{GoblinColors.RESET}")

            save_choice = input(f"\n{GoblinColors.NEON_GREEN}➜ {GoblinColors.WHITE}Save all dorks to files? (y/n): {GoblinColors.RESET}").strip().lower()

            if save_choice == 'y':
                print(f"\n{GoblinColors.GOBLIN_GOLD}💾 Saving complete tracking results...{GoblinColors.RESET}")
                progress = ProgressBar(5)
                progress.start("Saving")

                files = self.save_manager.save_dorks(username, commands)

                progress.current = 5
                progress.stop()

                self.display_saved_files(files)
            else:
                print(f"\n{GoblinColors.GOBLIN_MOSS}⏭️ Skipped saving files{GoblinColors.RESET}")

            print(f"\n{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")
            print(f"{GoblinColors.GOBLIN_GREEN}{GoblinColors.BOLD}✅ COMPLETE{GoblinColors.RESET}")
            print(f"{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")
            print(f"  {GoblinColors.WHITE}Username:{GoblinColors.RESET} @{username}")
            print(f"  {GoblinColors.WHITE}Total Dorks:{GoblinColors.RESET} {sum(len(c) for c in commands.values())}")
            print(f"  {GoblinColors.WHITE}Platforms:{GoblinColors.RESET} 4")
            print(f"  {GoblinColors.WHITE}Categories:{GoblinColors.RESET} 25+ Tracking Categories")

            if save_choice == 'y':
                print(f"  {GoblinColors.WHITE}Files Saved:{GoblinColors.RESET} {len(files)}")
                total_size = sum(os.path.getsize(f) for f in files if os.path.exists(f))
                size_str = f"{total_size:,} bytes" if total_size < 1024 * 1024 else f"{total_size / (1024 * 1024):.2f} MB"
                print(f"  {GoblinColors.WHITE}Total Size:{GoblinColors.RESET} {size_str}")
            else:
                print(f"  {GoblinColors.WHITE}Files Saved:{GoblinColors.RESET} 0 (skipped)")

            print(f"{GoblinColors.GOBLIN_GOLD}{'═' * 80}{GoblinColors.RESET}")

            input(f"\n{GoblinColors.GOBLIN_MOSS}Press Enter to exit...{GoblinColors.RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{GoblinColors.GOBLIN_BLOOD}⚠️ Operation cancelled{GoblinColors.RESET}")
            time.sleep(1)
        except Exception as e:
            print(f"\n{GoblinColors.GOBLIN_BLOOD}❌ Error: {e}{GoblinColors.RESET}")
            import traceback
            traceback.print_exc()
            time.sleep(5)

# ==================== MAIN ====================

if __name__ == "__main__":
    app = GoblinTsunami()
    app.run()
