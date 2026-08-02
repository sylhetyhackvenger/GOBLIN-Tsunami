#!/usr/bin/env python3
import os
import sys
import time
import json
import random
import hashlib
import hmac
import base64
import urllib.parse
import webbrowser
import re
import threading
import signal
import pickle
import math
import copy
import traceback
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any, Union, Set
from dataclasses import dataclass, field, asdict
from collections import defaultdict, Counter, OrderedDict, deque
import warnings
import csv
import io
import zlib
import gzip
import binascii
warnings.filterwarnings('ignore')

# ==================== MINIMAL DEPENDENCIES ====================

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("📦 Installing minimal dependencies...")
    os.system("pip install requests beautifulsoup4")
    import requests
    from bs4 import BeautifulSoup

# ==================== COMPLETE COLOR SYSTEM ====================

class GoblinColors:
    """Complete color system - All original colors"""
    # Greens
    GOBLIN_GREEN = '\033[92m'
    DARK_GREEN = '\033[38;5;22m'
    MOSS_GREEN = '\033[38;5;64m'
    SWAMP_GREEN = '\033[38;5;28m'
    LIME_GREEN = '\033[38;5;118m'
    FOREST_GREEN = '\033[38;5;34m'
    OLIVE_GREEN = '\033[38;5;58m'
    NEO_GREEN = '\033[38;5;46m'
    VICTORY_GREEN = '\033[38;5;82m'
    
    # Browns
    MUD_BROWN = '\033[38;5;94m'
    LEATHER_BROWN = '\033[38;5;130m'
    DARK_BROWN = '\033[38;5;52m'
    CAVE_BROWN = '\033[38;5;95m'
    WOOD_BROWN = '\033[38;5;136m'
    
    # Earth tones
    RUST_ORANGE = '\033[38;5;166m'
    DIRT_YELLOW = '\033[38;5;142m'
    STONE_GRAY = '\033[38;5;239m'
    SAND = '\033[38;5;144m'
    
    # Accents
    GOBLIN_GOLD = '\033[38;5;178m'
    LEGACY_GOLD = '\033[38;5;220m'
    POISON_PURPLE = '\033[38;5;90m'
    DARK_PURPLE = '\033[38;5;55m'
    BLOOD_RED = '\033[91m'
    EYE_GLOW = '\033[38;5;226m'
    MAGENTA = '\033[38;5;199m'
    
    # Ocean
    DEEP_BLUE = '\033[38;5;18m'
    OCEAN_BLUE = '\033[38;5;27m'
    CYAN_WAVE = '\033[38;5;51m'
    LIGHT_CYAN = '\033[38;5;45m'
    MODERN_CYAN = '\033[38;5;51m'

    # ============================================================
    # 🛑 FIX: ADDED MISSING COLORS FROM ORIGINAL PRINT STATEMENTS
    # ============================================================
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'

# ==================== COMPLETE BANNER ====================

BANNER_ART = r'''
.o######0o.             0###########0.      .
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
'''

# ==================== COMPLETE BANNER SYSTEM ====================

class CompleteBanner:
    """Complete banner system - All effects"""
    
    def __init__(self):
        self.colors = GoblinColors
        self.lines = BANNER_ART.split('\n')[1:]
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def header(self, title="⚔ GOBLIN TSUNAMI ⚔"):
        print(f"{self.colors.MOSS_GREEN}╔{'═'*78}╗{self.colors.RESET}")
        print(f"{self.colors.MOSS_GREEN}║{self.colors.RESET}  {self.colors.GOBLIN_GREEN}{self.colors.BOLD}✦ {title} ✦{self.colors.RESET}{' ' * (70 - len(title))}{self.colors.MOSS_GREEN}║{self.colors.RESET}")
        print(f"{self.colors.MOSS_GREEN}╚{'═'*78}╝{self.colors.RESET}")
    
    def footer(self):
        print(f"{self.colors.CAVE_BROWN}╔{'═'*78}╗{self.colors.RESET}")
        print(f"{self.colors.CAVE_BROWN}║{self.colors.RESET}  {self.colors.GOBLIN_GOLD}☠ GOBLIN HORDE  |  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{self.colors.RESET}{' ' * 37}{self.colors.CAVE_BROWN}║{self.colors.RESET}")
        print(f"{self.colors.CAVE_BROWN}╚{'═'*78}╝{self.colors.RESET}")
    
    def effect_goblin_green(self):
        self.header("🐉 GOBLIN GREEN BANNER")
        print()
        for line in self.lines:
            if line.strip():
                print(f"{self.colors.GOBLIN_GREEN}{line}{self.colors.RESET}")
            else:
                print()
        self.footer()
    
    def effect_swamp_poison(self):
        self.header("☠ SWAMP POISON BANNER")
        print()
        colors = [self.colors.SWAMP_GREEN, self.colors.POISON_PURPLE, 
                  self.colors.MOSS_GREEN, self.colors.RUST_ORANGE,
                  self.colors.DARK_GREEN, self.colors.LIME_GREEN,
                  self.colors.OLIVE_GREEN, self.colors.MAGENTA]
        for i, line in enumerate(self.lines):
            if line.strip():
                print(f"{colors[i % len(colors)]}{line}{self.colors.RESET}")
            else:
                print()
        print(f"\n{self.colors.POISON_PURPLE}☠ Poison Swamp Mode{self.colors.RESET}")
        self.footer()
    
    def effect_treasure_hoard(self):
        self.header("✨ TREASURE HOARD BANNER")
        print()
        colors = [self.colors.GOBLIN_GOLD, self.colors.RUST_ORANGE, 
                  self.colors.DIRT_YELLOW, self.colors.LEATHER_BROWN,
                  self.colors.EYE_GLOW, self.colors.DARK_BROWN,
                  self.colors.WOOD_BROWN, self.colors.SAND]
        for i, line in enumerate(self.lines):
            if line.strip():
                print(f"{colors[i % len(colors)]}{line}{self.colors.RESET}")
            else:
                print()
        print(f"\n{self.colors.GOBLIN_GOLD}✨ Treasure Hoard Mode{self.colors.RESET}")
        self.footer()
    
    def effect_dark_cave(self):
        self.header("👁️ DARK CAVE BANNER")
        print()
        for line in self.lines:
            if line.strip():
                dark = ""
                for c in line:
                    if c != ' ' and random.random() < 0.1:
                        dark += f"{self.colors.EYE_GLOW}{c}{self.colors.RESET}"
                    else:
                        dark += f"{self.colors.STONE_GRAY}{c}{self.colors.RESET}"
                print(dark)
            else:
                print()
        print(f"\n{self.colors.EYE_GLOW}👁️ Dark Cave Mode{self.colors.RESET}")
        self.footer()
    
    def effect_battle_horde(self):
        self.header("⚔ BATTLE HORDE BANNER")
        print()
        colors = [self.colors.BLOOD_RED, self.colors.RUST_ORANGE, 
                  self.colors.GOBLIN_GREEN, self.colors.DIRT_YELLOW,
                  self.colors.CAVE_BROWN, self.colors.FOREST_GREEN,
                  self.colors.MUD_BROWN, self.colors.LEATHER_BROWN]
        for i, line in enumerate(self.lines):
            if line.strip():
                color = colors[i % len(colors)]
                battle = ""
                for c in line:
                    if c != ' ' and random.random() < 0.05:
                        battle += f"{self.colors.GOBLIN_GOLD}*{self.colors.RESET}"
                    else:
                        battle += f"{color}{c}{self.colors.RESET}"
                print(battle)
            else:
                print()
        print(f"\n{self.colors.BLOOD_RED}⚔ For GOBLIN HORDE!{self.colors.RESET}")
        self.footer()
    
    def effect_chaos_magic(self):
        self.header("🧙 CHAOS MAGIC BANNER")
        print()
        chars = ['☠', '♠', '♣', '♦', '♥', '⚔', '▣', '◈', '✦', '✧', '★', '⬡']
        colors = [self.colors.POISON_PURPLE, self.colors.BLOOD_RED, 
                  self.colors.SWAMP_GREEN, self.colors.GOBLIN_GOLD,
                  self.colors.RUST_ORANGE, self.colors.MAGENTA,
                  self.colors.LIME_GREEN, self.colors.EYE_GLOW]
        for line in self.lines:
            if line.strip():
                chaos = ""
                for c in line:
                    if c != ' ' and random.random() < 0.1:
                        chaos += f"{random.choice(colors)}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        chaos += f"{random.choice([self.colors.GOBLIN_GREEN, self.colors.MOSS_GREEN, self.colors.DARK_GREEN])}{c}{self.colors.RESET}"
                print(chaos)
            else:
                print()
        print(f"\n{self.colors.POISON_PURPLE}🧙 Chaos Magic Activated!{self.colors.RESET}")
        self.footer()
    
    def effect_boxed_banner(self):
        self.header("📦 BOXED GOBLIN BANNER")
        print()
        max_len = max((len(line) for line in self.lines if line.strip()), default=0)
        w = max_len + 6
        print(f"{self.colors.MOSS_GREEN}╔{'═'*w}╗{self.colors.RESET}")
        print(f"{self.colors.MOSS_GREEN}║{self.colors.RESET}  {self.colors.GOBLIN_GREEN}{self.colors.BOLD}☠ GOBLIN BANNER ☠{self.colors.RESET}  {self.colors.MOSS_GREEN}║{self.colors.RESET}")
        print(f"{self.colors.MOSS_GREEN}╟{'─'*w}╢{self.colors.RESET}")
        for line in self.lines:
            if line.strip():
                pad = w - len(line) - 2
                lp = pad // 2
                rp = pad - lp
                color = random.choice([self.colors.GOBLIN_GREEN, self.colors.SWAMP_GREEN, 
                                       self.colors.RUST_ORANGE, self.colors.GOBLIN_GOLD])
                print(f"{self.colors.MOSS_GREEN}║{self.colors.RESET}  {' '*lp}{color}{line}{self.colors.RESET}{' '*rp}  {self.colors.MOSS_GREEN}║{self.colors.RESET}")
            else:
                print(f"{self.colors.MOSS_GREEN}║{self.colors.RESET}  {' '*w}  {self.colors.MOSS_GREEN}║{self.colors.RESET}")
        print(f"{self.colors.MOSS_GREEN}╚{'═'*w}╝{self.colors.RESET}")
        self.footer()
    
    def effect_typing_animation(self):
        self.header("⌨️ TYPING GOBLIN BANNER")
        print()
        for line in self.lines:
            if line.strip():
                for c in line:
                    color = random.choice([self.colors.GOBLIN_GREEN, self.colors.MOSS_GREEN, 
                                          self.colors.SWAMP_GREEN, self.colors.RUST_ORANGE,
                                          self.colors.GOBLIN_GOLD, self.colors.LIME_GREEN,
                                          self.colors.POISON_PURPLE])
                    print(color + c + self.colors.RESET, end='', flush=True)
                    time.sleep(0.005)
                print()
                time.sleep(0.05)
            else:
                print()
                time.sleep(0.02)
        self.footer()
    
    def effect_rotating_colors(self):
        self.clear()
        self.header("🔄 ROTATING GOBLIN BANNER")
        colors = [self.colors.GOBLIN_GREEN, self.colors.SWAMP_GREEN, 
                  self.colors.MOSS_GREEN, self.colors.RUST_ORANGE,
                  self.colors.GOBLIN_GOLD, self.colors.DARK_GREEN,
                  self.colors.POISON_PURPLE, self.colors.LIME_GREEN,
                  self.colors.FOREST_GREEN, self.colors.DIRT_YELLOW,
                  self.colors.OLIVE_GREEN, self.colors.LEATHER_BROWN,
                  self.colors.MUD_BROWN, self.colors.SAND,
                  self.colors.CAVE_BROWN, self.colors.WOOD_BROWN]
        try:
            for rotation in range(16):
                self.clear()
                self.header("🔄 ROTATING GOBLIN BANNER")
                print()
                for i, line in enumerate(self.lines):
                    if line.strip():
                        print(f"{colors[(i + rotation) % len(colors)]}{line}{self.colors.RESET}")
                    else:
                        print()
                print(f"\n{self.colors.EYE_GLOW}🔄 Rotating... {rotation+1}/16{self.colors.RESET}")
                time.sleep(0.3)
        except KeyboardInterrupt:
            print(f"\n{self.colors.GOBLIN_GOLD}Goblin says: 'Stop dat!'{self.colors.RESET}")
        self.footer()
    
    def effect_treasure_sparkle(self):
        self.header("✨ SPARKLE GOBLIN BANNER")
        print()
        chars = ['✦', '✧', '★', '♦', '◈', '⬡', '◇', '♢', '✤', '❋']
        for line in self.lines:
            if line.strip():
                sparkle = ""
                for c in line:
                    if c != ' ' and random.random() < 0.06:
                        sparkle += f"{random.choice([self.colors.GOBLIN_GOLD, self.colors.EYE_GLOW, self.colors.RUST_ORANGE, self.colors.LIME_GREEN, self.colors.MAGENTA])}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        sparkle += f"{random.choice([self.colors.GOBLIN_GREEN, self.colors.MOSS_GREEN, self.colors.DARK_GREEN])}{c}{self.colors.RESET}"
                print(sparkle)
            else:
                print()
        print(f"\n{self.colors.GOBLIN_GOLD}💰 Treasure Sparkle Mode{self.colors.RESET}")
        self.footer()
    
    def effect_goblin_preview(self):
        self.header("🎨 GOBLIN ART PREVIEW")
        print(f"\n{self.colors.GOBLIN_GOLD}Goblin Banner Elements:{self.colors.RESET}\n")
        elements = [(".o######0o.", "Goblin Crown/Flower"),
                    ("0###########0", "Goblin Cage/Container"),
                    ('" "', "Goblin Quotes (Sneaky)"),
                    ("(## m#o ####(", "Goblin Decorative Runes"),
                    ("nn", "Goblin Letters"),
                    ("_", "Goblin Underline (Sneaky)"),
                    ("RADIUS", "THE GOBLIN NAME")]
        for element, description in elements:
            print(f"{self.colors.GOBLIN_GREEN}{element:20}{self.colors.RESET} → {self.colors.GOBLIN_GOLD}{description}{self.colors.RESET}")
        self.footer()
    
    def effect_rainbow(self):
        self.header("🌈 RAINBOW GOBLIN BANNER")
        print()
        colors = [self.colors.BLOOD_RED, self.colors.RUST_ORANGE, self.colors.GOBLIN_GOLD,
                  self.colors.LIME_GREEN, self.colors.OCEAN_BLUE, self.colors.POISON_PURPLE,
                  self.colors.MAGENTA]
        for line in self.lines:
            if line.strip():
                rainbow = ""
                for i, c in enumerate(line):
                    if c != ' ':
                        rainbow += f"{colors[i % len(colors)]}{c}{self.colors.RESET}"
                    else:
                        rainbow += " "
                print(rainbow)
            else:
                print()
        print(f"\n{self.colors.MAGENTA}🌈 Rainbow Magic!{self.colors.RESET}")
        self.footer()
    
    def effect_neon_glow(self):
        self.header("💡 NEON GOBLIN BANNER")
        print()
        colors = [self.colors.NEO_GREEN, self.colors.CYAN_WAVE, self.colors.MAGENTA,
                  self.colors.EYE_GLOW, self.colors.GOBLIN_GOLD, self.colors.LIME_GREEN]
        for line in self.lines:
            if line.strip():
                neon = ""
                for c in line:
                    if c != ' ':
                        neon += f"{random.choice(colors)}{self.colors.BOLD}{c}{self.colors.RESET}"
                    else:
                        neon += " "
                print(neon)
            else:
                print()
        print(f"\n{self.colors.NEO_GREEN}💡 Neon Glow Mode{self.colors.RESET}")
        self.footer()
    
    def effect_mosaic(self):
        self.header("🎨 MOSAIC GOBLIN BANNER")
        print()
        chars = ['█', '▓', '▒', '░', '▄', '▀', '■', '□']
        colors = [self.colors.GOBLIN_GREEN, self.colors.MOSS_GREEN, self.colors.SWAMP_GREEN,
                  self.colors.RUST_ORANGE, self.colors.GOBLIN_GOLD, self.colors.POISON_PURPLE]
        for line in self.lines:
            if line.strip():
                mosaic = ""
                for c in line:
                    if c != ' ':
                        mosaic += f"{random.choice(colors)}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        mosaic += " "
                print(mosaic)
            else:
                print()
        print(f"\n{self.colors.GOBLIN_GOLD}🎨 Mosaic Mode{self.colors.RESET}")
        self.footer()
    
    def effect_snake(self):
        self.header("🐍 SNAKE GOBLIN BANNER")
        print()
        colors = [self.colors.FOREST_GREEN, self.colors.SWAMP_GREEN, self.colors.MOSS_GREEN,
                  self.colors.DARK_GREEN, self.colors.OLIVE_GREEN, self.colors.LIME_GREEN]
        for line in self.lines:
            if line.strip():
                snake = ""
                for i, c in enumerate(line):
                    if c != ' ':
                        snake += f"{colors[i % len(colors)]}{c}{self.colors.RESET}"
                    else:
                        snake += " "
                print(snake)
            else:
                print()
        print(f"\n{self.colors.FOREST_GREEN}🐍 Snake Mode{self.colors.RESET}")
        self.footer()
    
    def effect_cyber(self):
        self.header("💻 CYBER GOBLIN BANNER")
        print()
        chars = ['0', '1', '0', '1', '█', '▓', '▒', '░']
        colors = [self.colors.CYAN_WAVE, self.colors.NEO_GREEN, self.colors.MODERN_CYAN,
                  self.colors.GOBLIN_GREEN]
        for line in self.lines:
            if line.strip():
                cyber = ""
                for c in line:
                    if c != ' ':
                        cyber += f"{random.choice(colors)}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        cyber += " "
                print(cyber)
            else:
                print()
        print(f"\n{self.colors.CYAN_WAVE}💻 Cyber Mode{self.colors.RESET}")
        self.footer()
    
    def effect_fire(self):
        self.header("🔥 FIRE GOBLIN BANNER")
        print()
        colors = [self.colors.BLOOD_RED, self.colors.RUST_ORANGE, self.colors.GOBLIN_GOLD,
                  self.colors.DIRT_YELLOW, self.colors.EYE_GLOW]
        for line in self.lines:
            if line.strip():
                fire = ""
                for c in line:
                    if c != ' ':
                        r = random.random()
                        if r < 0.2: color = colors[0]
                        elif r < 0.4: color = colors[1]
                        elif r < 0.6: color = colors[2]
                        elif r < 0.8: color = colors[3]
                        else: color = colors[4]
                        fire += f"{color}{c}{self.colors.RESET}"
                    else:
                        fire += " "
                print(fire)
            else:
                print()
        print(f"\n{self.colors.BLOOD_RED}🔥 Fire Mode{self.colors.RESET}")
        self.footer()
    
    def effect_ice(self):
        self.header("❄️ ICE GOBLIN BANNER")
        print()
        colors = [self.colors.DEEP_BLUE, self.colors.OCEAN_BLUE, self.colors.CYAN_WAVE,
                  self.colors.LIGHT_CYAN, self.colors.GOBLIN_GREEN]
        for line in self.lines:
            if line.strip():
                ice = ""
                for c in line:
                    if c != ' ':
                        ice += f"{random.choice(colors)}{c}{self.colors.RESET}"
                    else:
                        ice += " "
                print(ice)
            else:
                print()
        print(f"\n{self.colors.CYAN_WAVE}❄️ Ice Mode{self.colors.RESET}")
        self.footer()
    
    def effect_halloween(self):
        self.header("🎃 HALLOWEEN GOBLIN BANNER")
        print()
        colors = [self.colors.RUST_ORANGE, self.colors.POISON_PURPLE, self.colors.BLOOD_RED,
                  self.colors.GOBLIN_GOLD, self.colors.EYE_GLOW, self.colors.MAGENTA]
        chars = ['🎃', '👻', '💀', '🧛', '🧟', '🦇', '🕷️']
        for line in self.lines:
            if line.strip():
                halloween = ""
                for c in line:
                    if c != ' ' and random.random() < 0.03:
                        halloween += f"{random.choice(colors)}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        halloween += f"{random.choice(colors)}{c}{self.colors.RESET}"
                print(halloween)
            else:
                print()
        print(f"\n{self.colors.RUST_ORANGE}🎃 Halloween Mode{self.colors.RESET}")
        self.footer()
    
    def effect_stealth(self):
        self.header("🥷 STEALTH GOBLIN BANNER")
        print()
        chars = ['▪', '▫', '▬', '▭', '▮', '▯', '▰', '▱']
        for line in self.lines:
            if line.strip():
                stealth = ""
                for c in line:
                    if c != ' ':
                        if random.random() < 0.2:
                            stealth += f"{self.colors.EYE_GLOW}{c}{self.colors.RESET}"
                        else:
                            stealth += f"{self.colors.STONE_GRAY}{random.choice(chars)}{self.colors.RESET}"
                    else:
                        stealth += " "
                print(stealth)
            else:
                print()
        print(f"\n{self.colors.STONE_GRAY}🥷 Stealth Mode{self.colors.RESET}")
        self.footer()
    
    def startup_animation(self):
        self.clear()
        print(f"{self.colors.MOSS_GREEN}🐉 Summoning Goblin Banner Renderer...{self.colors.RESET}")
        for i in range(101):
            bar = '█' * (i // 2) + '░' * (50 - i // 2)
            print(f"\r[{self.colors.GOBLIN_GREEN}{bar}{self.colors.RESET}] {i}%", end='', flush=True)
            time.sleep(0.02)
        print(f"\n{self.colors.GOBLIN_GOLD}✓ Goblins ready! 🏴‍☠️{self.colors.RESET}")
        time.sleep(0.5)
    
    def exit_animation(self):
        self.clear()
        print(f"""
{self.colors.GOBLIN_GREEN}╔══════════════════════════════════════════╗
║  {self.colors.GOBLIN_GOLD}🐉 GOBLIN SAYS GOODBYE! 🐉{self.colors.GOBLIN_GREEN}  ║
╚══════════════════════════════════════════╝{self.colors.RESET}

{self.colors.MOSS_GREEN}  ☠ May your treasure be plentiful! ☠{self.colors.RESET}
{self.colors.GOBLIN_GOLD}     🏴‍☠️  ARRR!  🏴‍☠️{self.colors.RESET}
""")
        time.sleep(1)
    
    def save_banner(self):
        fname = f"goblin_banner_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(fname, 'w') as f:
                f.write("="*80 + "\n")
                f.write("🐉 GOBLIN TSUNAMI BANNER\n")
                f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*80 + "\n\n")
                for line in self.lines:
                    f.write(line + "\n")
                f.write("\n" + "="*80 + "\n")
                f.write("☠ End of Goblin Banner ☠\n")
                f.write("="*80 + "\n")
            print(f"{self.colors.GOBLIN_GREEN}✓ Banner saved to: {fname}{self.colors.RESET}")
            return True
        except Exception as e:
            print(f"{self.colors.BLOOD_RED}✗ Error saving: {e}{self.colors.RESET}")
            return False
    
    def show_help(self):
        self.header("🐉 GOBLIN HELP 🐉")
        print(f"""
{self.colors.GOBLIN_GREEN}{self.colors.BOLD}ABOUT:{self.colors.RESET}
This tool displays your ASCII art banner with GOBLIN THEMED colors!

{self.colors.GOBLIN_GOLD}{self.colors.BOLD}GOBLIN FEATURES (20+ EFFECTS):{self.colors.RESET}
  • {self.colors.GOBLIN_GREEN}Goblin Green Theme{self.colors.RESET} - Classic goblin colors
  • {self.colors.SWAMP_GREEN}Swamp Poison Theme{self.colors.RESET} - Toxic swamp vibes
  • {self.colors.GOBLIN_GOLD}Treasure Hoard Theme{self.colors.RESET} - Gold and riches
  • {self.colors.STONE_GRAY}Dark Cave Theme{self.colors.RESET} - Eyes glowing in dark
  • {self.colors.BLOOD_RED}Battle Theme{self.colors.RESET} - For the goblin horde!
  • {self.colors.POISON_PURPLE}Chaos Magic Theme{self.colors.RESET} - Unstable goblin magic
  • {self.colors.MAGENTA}Rainbow Theme{self.colors.RESET} - Colorful rainbow effect
  • {self.colors.NEO_GREEN}Neon Theme{self.colors.RESET} - Bright neon glow
  • {self.colors.GOBLIN_GOLD}Mosaic Theme{self.colors.RESET} - Pixel art style
  • {self.colors.FOREST_GREEN}Snake Theme{self.colors.RESET} - Snake pattern
  • {self.colors.CYAN_WAVE}Cyber Theme{self.colors.RESET} - Digital matrix style
  • {self.colors.BLOOD_RED}Fire Theme{self.colors.RESET} - Burning flames
  • {self.colors.CYAN_WAVE}Ice Theme{self.colors.RESET} - Frozen style
  • {self.colors.RUST_ORANGE}Halloween Theme{self.colors.RESET} - Spooky decorations
  • {self.colors.STONE_GRAY}Stealth Theme{self.colors.RESET} - Ninja style
  
{self.colors.EYE_GLOW}{self.colors.BOLD}TIPS:{self.colors.RESET}
  • Don't anger the goblins! (They bite)
  • Share treasure with your goblin friends
  • Keep the banner safe from adventurers
  
{self.colors.GOBLIN_GOLD}☠ GOBLIN SAYS: "HAVE FUN!" ☠{self.colors.RESET}
""")
        self.footer()
    
    def menu(self):
        effects = [
            ("1", "Goblin Green", self.effect_goblin_green),
            ("2", "Swamp Poison", self.effect_swamp_poison),
            ("3", "Treasure Hoard", self.effect_treasure_hoard),
            ("4", "Dark Cave", self.effect_dark_cave),
            ("5", "Battle Horde", self.effect_battle_horde),
            ("6", "Chaos Magic", self.effect_chaos_magic),
            ("7", "Boxed Banner", self.effect_boxed_banner),
            ("8", "Typing Animation", self.effect_typing_animation),
            ("9", "Rotating Colors", self.effect_rotating_colors),
            ("10", "Treasure Sparkle", self.effect_treasure_sparkle),
            ("11", "Rainbow", self.effect_rainbow),
            ("12", "Neon Glow", self.effect_neon_glow),
            ("13", "Mosaic", self.effect_mosaic),
            ("14", "Snake Pattern", self.effect_snake),
            ("15", "Cyber Matrix", self.effect_cyber),
            ("16", "Fire", self.effect_fire),
            ("17", "Ice", self.effect_ice),
            ("18", "Halloween", self.effect_halloween),
            ("19", "Stealth", self.effect_stealth),
            ("20", "ALL Effects", self.effect_all),
            ("21", "Save Banner", self.save_banner),
            ("22", "Help", self.show_help),
            ("23", "Exit", None)
        ]
        
        while True:
            self.clear()
            print(f"""
{self.colors.GOBLIN_GREEN}   ╔══════════════════════════════════════════════════════════╗{self.colors.RESET}
{self.colors.GOBLIN_GREEN}   ║{self.colors.RESET}  {self.colors.BOLD}{self.colors.MOSS_GREEN}🐉 GOBLIN BANNER RENDERER 🐉{self.colors.RESET}  {self.colors.GOBLIN_GREEN}║{self.colors.RESET}
{self.colors.GOBLIN_GREEN}   ╚══════════════════════════════════════════════════════════╝{self.colors.RESET}
{self.colors.CAVE_BROWN}   ╔══════════════════════════════════════════════════════════╗{self.colors.RESET}
""")
            for num, name, _ in effects:
                print(f"{self.colors.CAVE_BROWN}   ║{self.colors.RESET}  {self.colors.GOBLIN_GREEN}{num:>2}.{self.colors.RESET} {name:<25} {self.colors.CAVE_BROWN}║{self.colors.RESET}")
            print(f"{self.colors.CAVE_BROWN}   ╚══════════════════════════════════════════════════════════╝{self.colors.RESET}")
            
            choice = input(f"{self.colors.GOBLIN_GOLD}Goblin asks: 'What ya want, mate? (1-23): {self.colors.RESET}").strip()
            
            for num, name, func in effects:
                if choice == num and func:
                    self.clear()
                    func()
                    if choice not in ['23', '21', '22']:
                        input(f"{self.colors.GOBLIN_GOLD}Press Enter...{self.colors.RESET}")
                    break
            else:
                if choice == "23":
                    self.exit_animation()
                    break
                print(f"{self.colors.BLOOD_RED}Goblin says: 'Dat ain't right!'{self.colors.RESET}")
                time.sleep(1)
    
    def effect_all(self):
        all_effects = [
            ("Goblin Green", self.effect_goblin_green),
            ("Swamp Poison", self.effect_swamp_poison),
            ("Treasure Hoard", self.effect_treasure_hoard),
            ("Dark Cave", self.effect_dark_cave),
            ("Battle Horde", self.effect_battle_horde),
            ("Chaos Magic", self.effect_chaos_magic),
            ("Boxed Banner", self.effect_boxed_banner),
            ("Typing Animation", self.effect_typing_animation),
            ("Rotating Colors", self.effect_rotating_colors),
            ("Treasure Sparkle", self.effect_treasure_sparkle),
            ("Rainbow", self.effect_rainbow),
            ("Neon Glow", self.effect_neon_glow),
            ("Mosaic", self.effect_mosaic),
            ("Snake Pattern", self.effect_snake),
            ("Cyber Matrix", self.effect_cyber),
            ("Fire", self.effect_fire),
            ("Ice", self.effect_ice),
            ("Halloween", self.effect_halloween),
            ("Stealth", self.effect_stealth)
        ]
        for name, func in all_effects:
            self.clear()
            print(f"{self.colors.GOBLIN_GOLD}▶ Goblin shows: {self.colors.BOLD}{name}{self.colors.RESET}\n")
            func()
            input(f"{self.colors.GOBLIN_GREEN}Press Enter for next...{self.colors.RESET}")

# ==================== DATA CLASSES ====================

@dataclass
class ProfileData:
    """Complete profile data"""
    username: str = ""
    user_id: str = ""
    numeric_id: str = ""
    full_name: str = ""
    biography: str = ""
    external_url: str = ""
    is_private: bool = False
    is_verified: bool = False
    is_business: bool = False
    is_professional: bool = False
    follower_count: int = 0
    following_count: int = 0
    post_count: int = 0
    profile_pic_url: str = ""
    profile_pic_hd: str = ""
    category: str = ""
    business_email: Optional[str] = None
    business_phone: Optional[str] = None
    public_email: str = ""
    public_phone: str = ""
    obfuscated_email: str = ""
    obfuscated_phone: str = ""
    account_type: str = "personal"
    bio_links: List[str] = field(default_factory=list)
    hashtags_used: List[str] = field(default_factory=list)
    mentions: List[str] = field(default_factory=list)
    avg_likes: float = 0.0
    avg_comments: float = 0.0
    engagement_rate: float = 0.0
    avg_saves: float = 0.0
    avg_shares: float = 0.0
    avg_views: float = 0.0
    posts: List[Dict] = field(default_factory=list)
    stories: List[Dict] = field(default_factory=list)
    highlights: List[Dict] = field(default_factory=list)
    tagged_posts: List[Dict] = field(default_factory=list)
    reels: List[Dict] = field(default_factory=list)
    igtv: List[Dict] = field(default_factory=list)
    threads_profile: Optional[Dict] = None
    sentiment_score: float = 0.0
    sentiment_label: str = 'neutral'
    topics: List[str] = field(default_factory=list)
    brand_affinity: List[str] = field(default_factory=list)
    growth_rate: float = 0.0
    growth_trend: str = 'stable'
    best_posting_time: Optional[str] = None
    best_posting_day: Optional[str] = None
    content_categories: List[str] = field(default_factory=list)
    engagement_patterns: Dict = field(default_factory=dict)
    audience_insights: Dict = field(default_factory=dict)
    predicted_growth: Dict = field(default_factory=dict)
    viral_score: float = 0.0
    content_quality_score: float = 0.0
    post_sentiments: List[Dict] = field(default_factory=list)
    hashtag_network: Dict = field(default_factory=dict)
    mention_network: Dict = field(default_factory=dict)
    location_data: List[Dict] = field(default_factory=list)
    music_data: List[Dict] = field(default_factory=list)
    liked_posts: List[Dict] = field(default_factory=list)
    saved_posts: List[Dict] = field(default_factory=list)
    direct_messages: List[Dict] = field(default_factory=list)
    
    def to_dict(self):
        return asdict(self)

@dataclass
class MatchResult:
    username: str = ""
    full_name: str = ""
    user_id: str = ""
    match_level: str = ""
    confidence_score: float = 0.0
    name_match: bool = False
    email_match: bool = False
    phone_match: bool = False
    name_f: int = 0
    email_f: int = 0
    phone_f: int = 0

@dataclass
class DorkResult:
    query: str = ""
    url: str = ""
    platform: str = ""
    keywords: List[str] = field(default_factory=list)
    username: str = ""
    results_found: int = 0
    urls_found: List[str] = field(default_factory=list)
    status: str = ""

@dataclass
class EngineResult:
    engine_name: str
    username: str
    profile: Optional[ProfileData] = None
    matches: List[MatchResult] = field(default_factory=list)
    dorks: List[DorkResult] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    obfuscated_data: Dict = field(default_factory=dict)
    execution_time: float = 0.0
    score: float = 0.0
    status: str = "RUNNING"
    error: Optional[str] = None

@dataclass
class FullAttackResult:
    username: str
    session_id: str
    custom_keywords: List[str]
    timestamp: str
    legacy: EngineResult
    modern: EngineResult
    winner: str
    combined_score: float
    all_dorks: List[DorkResult]
    all_keywords: List[str]
    summary: Dict

# ==================== COMPLETE LEGACY ENGINE ====================

class LegacyEngine:
    """100% COMPLETE Original Instagram Intelligence Engine"""
    
    def __init__(self, session_id: str = None):
        self.session_id = session_id
        self.session = requests.Session()
        self.IG_SIG_KEY = 'e6358aeede676184b9fe702b30f4fd35e71744605e39d2181a34cede076b3c33'
        self.SIG_KEY_VERSION = '4'
        self.user_agents = self._generate_user_agents()
        self.rate_limit_counter = 0
        self.cache = {}
        self.request_timestamps = deque(maxlen=200)
        self.max_requests_per_minute = 150
        
    def _generate_user_agents(self) -> List[str]:
        ua_list = []
        insta_versions = ['101.0.0.15.120', '135.0.0.20.56', '150.0.0.30.12', 
                         '200.0.0.25.10', '250.0.0.15.8', '300.0.0.20.5']
        for version in insta_versions:
            ua_list.append(f'Instagram {version} (iPhone; iOS 15_0; en_US)')
            ua_list.append(f'Instagram {version} (Android; 11; en_US)')
        ua_list.extend([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ])
        return ua_list
    
    def _get_headers(self) -> Dict:
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'X-IG-App-ID': '936619743392459',
            'X-IG-Device-ID': f"android-{''.join(random.choices('0123456789abcdef', k=16))}"
        }
        if self.session_id:
            headers['Cookie'] = f'sessionid={self.session_id}; csrftoken=;'
        return headers
    
    def _rate_limit_check(self):
        self.request_timestamps.append(time.time())
        if len(self.request_timestamps) == self.max_requests_per_minute:
            oldest = self.request_timestamps[0]
            now = time.time()
            if now - oldest < 60:
                delay = 60 - (now - oldest) + random.uniform(1, 5)
                print(f"{GoblinColors.YELLOW}⏳ Rate limit: waiting {delay:.2f}s{GoblinColors.RESET}")
                time.sleep(delay)
                self.request_timestamps.clear()
    
    def _request(self, url: str, method: str = 'GET', params: Dict = None, 
                 data: Dict = None, retry: int = 0) -> Optional[Dict]:
        try:
            self._rate_limit_check()
            self.rate_limit_counter += 1
            
            if self.rate_limit_counter % 5 == 0:
                time.sleep(random.uniform(0.5, 1.5))
            
            headers = self._get_headers()
            
            if method.upper() == 'GET':
                response = self.session.get(url, headers=headers, params=params, timeout=30)
            else:
                response = self.session.post(url, headers=headers, params=params, json=data, timeout=30)
            
            if response.status_code == 200:
                if 'application/json' in response.headers.get('content-type', ''):
                    return response.json()
                return response.text
            elif response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"{GoblinColors.YELLOW}Rate limited. Waiting {retry_after}s...{GoblinColors.RESET}")
                time.sleep(retry_after + random.uniform(0, 10))
                if retry < 3:
                    return self._request(url, method, params, data, retry + 1)
            elif retry < 3:
                time.sleep(2 ** retry)
                return self._request(url, method, params, data, retry + 1)
        except Exception as e:
            if retry < 3:
                time.sleep(2 ** retry)
                return self._request(url, method, params, data, retry + 1)
            print(f"{GoblinColors.BLOOD_RED}❌ Request error: {str(e)}{GoblinColors.RESET}")
        return None
    
    def getUserId(self, username: str) -> Dict:
        try:
            response = self._request(f'https://www.instagram.com/{username}/?__a=1')
            if response:
                user_id = response.get("logging_page_id", "").strip("profilePage_")
                return {"id": user_id, "error": None} if user_id else {"id": None, "error": "User not found"}
        except:
            pass
        return {"id": None, "error": "Rate limit or error"}
    
    def getInfo(self, username: str) -> Dict:
        userId = self.getUserId(username)
        if userId["error"] is not None:
            return {"user": None, "error": userId["error"]}
        try:
            response = self._request(f'https://i.instagram.com/api/v1/users/{userId["id"]}/info/')
            if response:
                infoUser = response["user"]
                infoUser["userID"] = userId["id"]
                return {"user": infoUser, "error": None}
        except:
            pass
        return {"user": None, "error": "Rate limit or error"}
    
    def advanced_lookup(self, username: str) -> Dict:
        def generate_signature(data):
            return 'ig_sig_key_version=' + self.SIG_KEY_VERSION + '&signed_body=' + \
                   hmac.new(self.IG_SIG_KEY.encode('utf-8'), 
                           data.encode('utf-8'), 
                           hashlib.sha256).hexdigest() + '.' + urllib.parse.quote_plus(data)
        data = generate_signature(json.dumps({
            'login_attempt_count': '0',
            'directly_sign_in': 'true',
            'source': 'default',
            'q': username,
            'ig_sig_key_version': self.SIG_KEY_VERSION
        }))
        headers = {
            "Accept-Language": "en-US",
            "User-Agent": "Instagram 101.0.0.15.120",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        try:
            response = self.session.post('https://i.instagram.com/api/v1/users/lookup/', headers=headers, data=data)
            if response.status_code == 200:
                return {"user": response.json(), "error": None}
        except:
            pass
        return {"user": None, "error": "rate limit"}
    
    def dumpor(self, name: str) -> Dict:
        url = "https://dumpor.com/search?query=" + name.replace(" ", "+")
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'})
            soup = BeautifulSoup(response.text, 'html.parser')
            accounts = soup.findAll('a', {"class": "profile-name-link"})
            return {"user": [account.text for account in accounts], "error": None}
        except:
            return {"user": None, "error": "rate limit"}
    
    def check_match(self, infos: Dict, target_name: str, target_email: str, target_phone: str) -> MatchResult:
        name_f = email_f = phone_f = 0
        if target_name and infos.get('full_name'):
            if infos['full_name'].lower() == target_name.lower():
                name_f = 1
        if target_email and infos.get('public_email'):
            public_email = infos['public_email']
            if public_email:
                if (public_email[0] == target_email[0] and 
                    public_email.split('@')[0][-1] == target_email.split('@')[0][-1] and
                    public_email.split('@')[1] == target_email.split('@')[1]):
                    email_f = 1
        if target_phone and infos.get('public_phone_number'):
            public_phone = str(infos['public_phone_number'])
            if public_phone:
                if (public_phone.split()[0] == target_phone.split()[0] and
                    public_phone[-2:] == target_phone[-2:]):
                    phone_f = 1
        total = name_f + email_f + phone_f
        if total == 3:
            level, score = "HIGH", 1.0
        elif total == 2:
            level, score = "MEDIUM", 0.7
        elif total == 1:
            level, score = "LOW", 0.3
        else:
            level, score = "NONE", 0.0
        return MatchResult(
            username=infos.get('username', ''),
            full_name=infos.get('full_name', ''),
            user_id=infos.get('userID', ''),
            match_level=level,
            confidence_score=score,
            name_match=name_f == 1,
            email_match=email_f == 1,
            phone_match=phone_f == 1,
            name_f=name_f,
            email_f=email_f,
            phone_f=phone_f
        )
    
    def display_original_match(self, infos: Dict, match: MatchResult):
        print(f"\n{GoblinColors.CYAN}Information about      : {infos.get('username', 'Unknown')}{GoblinColors.RESET}")
        if match.name_f == 1:
            print(f"{GoblinColors.GOBLIN_GREEN}Full Name              : {infos.get('full_name', 'N/A')} ✓{GoblinColors.RESET}")
        else:
            print(f"Full Name              : {infos.get('full_name', 'N/A')}")
        print(f"User ID                : {infos.get('userID', 'N/A')}")
        print(f"Verified               : {infos.get('is_verified', False)}")
        print(f"Is business Account    : {infos.get('is_business', False)}")
        print(f"Is private Account     : {infos.get('is_private', False)}")
        print(f"Followers              : {infos.get('follower_count', 0)}")
        print(f"Following              : {infos.get('following_count', 0)}")
        print(f"Number of posts        : {infos.get('media_count', 0)}")
        print(f"External URL           : {infos.get('external_url', 'N/A')}")
        print(f"Biography              : {infos.get('biography', 'N/A')[:200]}")
        if infos.get('public_email'):
            if match.email_f == 1:
                print(f"{GoblinColors.GOBLIN_GREEN}Public email           : {infos['public_email']} ✓{GoblinColors.RESET}")
            else:
                print(f"Public email           : {infos['public_email']}")
        if infos.get('public_phone_number'):
            if match.phone_f == 1:
                print(f"{GoblinColors.GOBLIN_GREEN}Public phone number    : {infos['public_phone_number']} ✓{GoblinColors.RESET}")
            else:
                print(f"Public phone           : {infos['public_phone_number']}")
        if match.match_level == "HIGH":
            print(f"{GoblinColors.CYAN}[*] {GoblinColors.GOBLIN_GREEN}Profile ID {infos.get('userID', 'N/A')} match level: HIGH{GoblinColors.RESET}")
        elif match.match_level == "MEDIUM":
            print(f"{GoblinColors.CYAN}[*] {GoblinColors.GOBLIN_GOLD}Profile ID {infos.get('userID', 'N/A')} match level: MEDIUM{GoblinColors.RESET}")
        elif match.match_level == "LOW":
            print(f"{GoblinColors.CYAN}[*] {GoblinColors.BLOOD_RED}Profile ID {infos.get('userID', 'N/A')} match level: LOW{GoblinColors.RESET}")
        print("-" * 30)
    
    def get_numeric_id(self, username: str) -> Optional[str]:
        methods = [
            self._get_id_from_web,
            self._get_id_from_api,
            self._get_id_from_lookup,
            self._get_id_from_graphql
        ]
        for method in methods:
            try:
                result = method(username)
                if result and str(result).isdigit():
                    return str(result)
            except:
                continue
        return None
    
    def _get_id_from_web(self, username: str) -> Optional[str]:
        try:
            response = self.session.get(f'https://www.instagram.com/{username}/', headers=self._get_headers())
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script')
                for script in scripts:
                    if script.string:
                        if 'profilePage_' in script.string:
                            match = re.search(r'profilePage_(\d+)', script.string)
                            if match:
                                return match.group(1)
                        if '"user_id"' in script.string:
                            match = re.search(r'"user_id":"(\d+)"', script.string)
                            if match:
                                return match.group(1)
        except:
            pass
        return None
    
    def _get_id_from_api(self, username: str) -> Optional[str]:
        try:
            response = self._request('https://i.instagram.com/api/v1/users/web_profile_info/', params={'username': username})
            if response:
                return response.get('data', {}).get('user', {}).get('id')
        except:
            pass
        return None
    
    def _get_id_from_lookup(self, username: str) -> Optional[str]:
        try:
            data = json.dumps({'q': username, 'ig_sig_key_version': self.SIG_KEY_VERSION})
            signed = self._generate_signature(data)
            response = self.session.post('https://i.instagram.com/api/v1/users/lookup/', data=signed, headers=self._get_headers())
            if response.status_code == 200:
                return response.json().get('user', {}).get('pk')
        except:
            pass
        return None
    
    def _get_id_from_graphql(self, username: str) -> Optional[str]:
        try:
            params = {
                'query_hash': '2c4c5e8e7f7c4d7a9e9b5d9c4f9e8d7f',
                'variables': json.dumps({'username': username})
            }
            response = self._request('https://www.instagram.com/graphql/query/', params=params)
            if response:
                return response.get('data', {}).get('user', {}).get('id')
        except:
            pass
        return None
    
    def _generate_signature(self, data: str) -> str:
        signed_body = hmac.new(
            self.IG_SIG_KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256
        ).hexdigest() + '.' + urllib.parse.quote_plus(data)
        return f'ig_sig_key_version={self.SIG_KEY_VERSION}&signed_body={signed_body}'
    
    def _extract_keywords(self, username: str, custom_keywords: List[str] = None, profile_data: Dict = None) -> List[str]:
        keywords = set()
        keywords.add(username)
        keywords.update(re.split(r'[._-]', username))
        if profile_data:
            if profile_data.get('full_name'):
                keywords.update(profile_data['full_name'].split())
            if profile_data.get('biography'):
                bio = profile_data['biography']
                keywords.update(re.findall(r'\b\w{3,}\b', bio))
                keywords.update(re.findall(r'#\w+', bio))
                keywords.update(re.findall(r'@\w+', bio))
            if profile_data.get('external_url'):
                domain = re.sub(r'https?://', '', profile_data['external_url']).split('/')[0]
                keywords.add(domain)
            if profile_data.get('hashtags_used'):
                keywords.update(profile_data['hashtags_used'])
            if profile_data.get('mentions'):
                keywords.update(profile_data['mentions'])
        if custom_keywords:
            keywords.update(custom_keywords)
        default_keywords = ['suspicious', 'location', 'event', 'business', 'meeting', 
                           'activity', 'deal', 'investment', 'client', 'partner',
                           'confidential', 'private', 'secret', 'exclusive', 'invite']
        keywords.update(default_keywords)
        return list(dict.fromkeys([k.lower().strip() for k in keywords if k and len(k) > 2]))[:25]
    
    def _build_dorks(self, username: str, keywords: List[str]) -> List[DorkResult]:
        dorks = []
        base = f'site:instagram.com "{username}"'
        dork_types = [
            ('profile', base),
            ('posts', f'{base} (post OR photo OR video OR reel)'),
            ('hashtags', f'{base} (#* OR hashtag*)'),
            ('mentions', f'{base} (@* OR mention*)'),
            ('location', f'{base} location*'),
            ('business', f'{base} (business OR company OR brand OR shop)'),
            ('email', f'{base} email*'),
            ('phone', f'{base} phone*'),
            ('url', f'{base} (url* OR link*)'),
            ('verification', f'{base} (verified OR official OR authentic)'),
            ('following', f'{base} (following OR followers)'),
            ('stories', f'{base} story*'),
            ('reels', f'{base} (reel* OR video*)'),
            ('igtv', f'{base} igtv*')
        ]
        for name, query in dork_types:
            dorks.append(DorkResult(
                query=query,
                url=f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}",
                platform='google',
                keywords=[] # FIXED: Passed empty list instead of faulty slicing
            ))
        if keywords:
            for keyword in keywords[:8]:
                query = f'{base} ("{keyword}")'
                dorks.append(DorkResult(
                    query=query,
                    url=f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}",
                    platform='google',
                    keywords=[]
                ))
        return dorks
    
    def _calculate_score(self, result: EngineResult) -> float:
        score = 0.0
        if result.profile:
            score += 2.0
            if result.profile.is_verified: score += 1.0
            if result.profile.is_business: score += 0.5
            if result.profile.follower_count > 1000: score += 0.5
            if result.profile.follower_count > 10000: score += 0.5
            if result.profile.post_count > 10: score += 0.5
            if result.profile.post_count > 50: score += 0.5
            if result.profile.public_email: score += 0.3
            if result.profile.public_phone: score += 0.3
            if result.profile.obfuscated_email: score += 0.2
            if result.profile.obfuscated_phone: score += 0.2
        score += len(result.keywords) * 0.2
        score += len(result.dorks) * 0.05
        if result.matches:
            for m in result.matches:
                if m.match_level == 'HIGH': score += 2.0
                elif m.match_level == 'MEDIUM': score += 1.0
                else: score += 0.5
        if result.obfuscated_data: score += 1.0
        return min(score, 10.0)
    
    def run(self, username: str, custom_keywords: List[str] = None,
            target_name: str = "", target_email: str = "", target_phone: str = "") -> EngineResult:
        start_time = time.time()
        result = EngineResult(engine_name="LEGACY", username=username, status="RUNNING")
        try:
            print(f"{GoblinColors.CYAN}📊 Step 1: Fetching profile data (Original getInfo)...{GoblinColors.RESET}")
            user_info = self.getInfo(username)
            if user_info and user_info.get('user'):
                data = user_info['user']
                profile = ProfileData(username=username)
                profile.full_name = data.get('full_name', '')
                profile.biography = data.get('biography', '')
                profile.external_url = data.get('external_url', '')
                profile.is_private = data.get('is_private', False)
                profile.is_verified = data.get('is_verified', False)
                profile.is_business = data.get('is_business', False)
                profile.follower_count = data.get('follower_count', 0)
                profile.following_count = data.get('following_count', 0)
                profile.post_count = data.get('media_count', 0)
                profile.profile_pic_url = data.get('profile_pic_url', '')
                profile.user_id = data.get('userID', '')
                profile.public_email = data.get('public_email', '')
                profile.public_phone = data.get('public_phone_number', '')
                profile.category = data.get('category', '')
                profile.account_type = 'business' if profile.is_business else 'personal'
                numeric_id = self.get_numeric_id(username)
                if numeric_id:
                    profile.numeric_id = numeric_id
                if profile.biography:
                    profile.bio_links = re.findall(r'https?://[^\s]+', profile.biography)
                    profile.hashtags_used = re.findall(r'#\w+', profile.biography)
                    profile.mentions = re.findall(r'@\w+', profile.biography)
                result.profile = profile
                print(f"{GoblinColors.GOBLIN_GREEN}✅ Profile data fetched{GoblinColors.RESET}")
            
            print(f"{GoblinColors.CYAN}🔍 Step 2: Extracting obfuscated data (Original advanced_lookup)...{GoblinColors.RESET}")
            obfuscated = self.advanced_lookup(username)
            if obfuscated and obfuscated.get('user'):
                result.obfuscated_data = obfuscated['user']
                if result.profile:
                    result.profile.obfuscated_email = obfuscated['user'].get('obfuscated_email', '')
                    result.profile.obfuscated_phone = obfuscated['user'].get('obfuscated_phone', '')
                print(f"{GoblinColors.GOBLIN_GREEN}✅ Obfuscated data extracted{GoblinColors.RESET}")
            
            print(f"{GoblinColors.CYAN}📝 Step 3: Building keyword list...{GoblinColors.RESET}")
            keywords = self._extract_keywords(username, custom_keywords, 
                                             result.profile.to_dict() if result.profile else None)
            result.keywords = keywords
            print(f"{GoblinColors.GOBLIN_GREEN}✅ Extracted {len(keywords)} keywords{GoblinColors.RESET}")
            
            if target_name:
                print(f"{GoblinColors.CYAN}🔎 Step 4: Searching for matching accounts (Original dumpor)...{GoblinColors.RESET}")
                accounts = self.dumpor(target_name)
                if accounts and accounts.get('user'):
                    print(f"{GoblinColors.DIM}Found {len(accounts['user'])} accounts, checking matches...{GoblinColors.RESET}")
                    for account in accounts['user'][:10]:
                        clean = account[1:] if account.startswith('@') else account
                        info = self.getInfo(clean)
                        if info and info.get('user'):
                            match = self.check_match(info['user'], target_name, target_email, target_phone)
                            if match.match_level != "NONE":
                                result.matches.append(match)
                                self.display_original_match(info['user'], match)
                    print(f"{GoblinColors.GOBLIN_GREEN}✅ Account matching complete ({len(result.matches)} matches){GoblinColors.RESET}")
            
            print(f"{GoblinColors.CYAN}🔍 Step 5: Building dorks...{GoblinColors.RESET}")
            result.dorks = self._build_dorks(username, keywords)
            print(f"{GoblinColors.GOBLIN_GREEN}✅ Built {len(result.dorks)} dorks{GoblinColors.RESET}")
            
            result.score = self._calculate_score(result)
            result.status = "COMPLETED"
            print(f"{GoblinColors.GOBLIN_GREEN}✅ Score: {result.score:.2f}/10.0{GoblinColors.RESET}")
        except Exception as e:
            result.status = "ERROR"
            result.error = str(e)
            traceback.print_exc()
        result.execution_time = time.time() - start_time
        return result

# ==================== COMPLETE MODERN ENGINE (Requests-based) ====================

class ModernEngine:
    """COMPLETE Modern Engine - Playwright REPLACED with requests"""
    
    def __init__(self, session_id: str = None):
        self.session_id = session_id
        self.session = requests.Session()
        self.user_agents = self._generate_user_agents()
        self.sentiment_keywords = self._load_sentiment_keywords()
        self.rate_limit_counter = 0
        self.request_timestamps = deque(maxlen=200)
        self.max_requests_per_minute = 150
        
    def _generate_user_agents(self) -> List[str]:
        ua_list = []
        for version in ['101.0.0.15.120', '135.0.0.20.56', '150.0.0.30.12']:
            ua_list.append(f'Instagram {version} (iPhone; iOS 15_0; en_US)')
            ua_list.append(f'Instagram {version} (Android; 11; en_US)')
        ua_list.extend([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        ])
        return ua_list
    
    def _load_sentiment_keywords(self) -> Dict:
        return {
            'positive': ['love', 'great', 'amazing', 'awesome', 'beautiful', 'happy', 'good', 'wonderful'],
            'negative': ['hate', 'bad', 'terrible', 'awful', 'sad', 'angry', 'disappointed', 'worst'],
            'neutral': ['okay', 'fine', 'alright', 'neutral']
        }
    
    def _get_headers(self) -> Dict:
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'X-IG-App-ID': '936619743392459',
            'X-IG-Device-ID': f"android-{''.join(random.choices('0123456789abcdef', k=16))}"
        }
        if self.session_id:
            headers['Cookie'] = f'sessionid={self.session_id}; csrftoken=;'
        return headers
    
    def _rate_limit_check(self):
        self.request_timestamps.append(time.time())
        if len(self.request_timestamps) == self.max_requests_per_minute:
            oldest = self.request_timestamps[0]
            now = time.time()
            if now - oldest < 60:
                delay = 60 - (now - oldest) + random.uniform(1, 5)
                print(f"{GoblinColors.YELLOW}⏳ Rate limit: waiting {delay:.2f}s{GoblinColors.RESET}")
                time.sleep(delay)
                self.request_timestamps.clear()
    
    def _request(self, url: str, params: Dict = None, retry: int = 0) -> Optional[Dict]:
        try:
            self._rate_limit_check()
            self.rate_limit_counter += 1
            if self.rate_limit_counter % 5 == 0:
                time.sleep(random.uniform(0.5, 1.5))
            headers = self._get_headers()
            response = self.session.get(url, headers=headers, params=params, timeout=30)
            if response.status_code == 200:
                if 'application/json' in response.headers.get('content-type', ''):
                    return response.json()
                return response.text
            elif response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"{GoblinColors.YELLOW}Rate limited. Waiting {retry_after}s...{GoblinColors.RESET}")
                time.sleep(retry_after + random.uniform(0, 10))
                if retry < 3:
                    return self._request(url, params, retry + 1)
            elif retry < 3:
                time.sleep(2 ** retry)
                return self._request(url, params, retry + 1)
        except Exception as e:
            if retry < 3:
                time.sleep(2 ** retry)
                return self._request(url, params, retry + 1)
        return None
    
    def get_user_id(self, username: str) -> Optional[str]:
        methods = [
            self._get_id_from_web,
            self._get_id_from_api,
            self._get_id_from_lookup,
            self._get_id_from_graphql
        ]
        for method in methods:
            try:
                result = method(username)
                if result and str(result).isdigit():
                    return str(result)
            except:
                continue
        return None
    
    def _get_id_from_web(self, username: str) -> Optional[str]:
        try:
            response = self.session.get(f'https://www.instagram.com/{username}/', headers=self._get_headers())
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script')
                for script in scripts:
                    if script.string:
                        if 'profilePage_' in script.string:
                            match = re.search(r'profilePage_(\d+)', script.string)
                            if match:
                                return match.group(1)
        except:
            pass
        return None
    
    def _get_id_from_api(self, username: str) -> Optional[str]:
        try:
            response = self._request('https://i.instagram.com/api/v1/users/web_profile_info/', params={'username': username})
            if response:
                return response.get('data', {}).get('user', {}).get('id')
        except:
            pass
        return None
    
    def _get_id_from_lookup(self, username: str) -> Optional[str]:
        try:
            data = json.dumps({'q': username})
            headers = self._get_headers()
            headers['Content-Type'] = 'application/json'
            response = self.session.post('https://i.instagram.com/api/v1/users/lookup/', headers=headers, data=data)
            if response.status_code == 200:
                return response.json().get('user', {}).get('pk')
        except:
            pass
        return None
    
    def _get_id_from_graphql(self, username: str) -> Optional[str]:
        try:
            params = {
                'query_hash': '2c4c5e8e7f7c4d7a9e9b5d9c4f9e8d7f',
                'variables': json.dumps({'username': username})
            }
            response = self._request('https://www.instagram.com/graphql/query/', params=params)
            if response:
                return response.get('data', {}).get('user', {}).get('id')
        except:
            pass
        return None
    
    def get_profile(self, username: str) -> Optional[Dict]:
        user_id = self.get_user_id(username)
        if not user_id:
            return None
        try:
            response = self._request(f'https://i.instagram.com/api/v1/users/{user_id}/info/')
            if response:
                return response.get('user', {})
        except:
            pass
        return None
    
    def get_posts(self, user_id: str, limit: int = 50) -> List[Dict]:
        posts = []
        end_cursor = None
        fetched = 0
        while fetched < limit:
            params = {'id': user_id, 'first': min(50, limit - fetched)}
            if end_cursor:
                params['after'] = end_cursor
            response = self._request('https://i.instagram.com/api/v1/feed/user/', params=params)
            if response and isinstance(response, dict):
                items = response.get('items', [])
                posts.extend(items)
                fetched += len(items)
                end_cursor = response.get('next_max_id')
                if not end_cursor or len(items) == 0:
                    break
                time.sleep(random.uniform(0.5, 1.5))
            else:
                break
        return posts[:limit]
    
    def get_followers(self, user_id: str, limit: int = 50) -> List[Dict]:
        followers = []
        end_cursor = None
        fetched = 0
        while fetched < limit:
            params = {}
            if end_cursor:
                params['max_id'] = end_cursor
            response = self._request(f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/', params=params)
            if response and isinstance(response, dict):
                items = response.get('users', [])
                followers.extend(items)
                fetched += len(items)
                end_cursor = response.get('next_max_id')
                if not end_cursor or len(items) == 0:
                    break
                time.sleep(random.uniform(0.5, 1.5))
            else:
                break
        return followers[:limit]
    
    def get_following(self, user_id: str, limit: int = 50) -> List[Dict]:
        following = []
        end_cursor = None
        fetched = 0
        while fetched < limit:
            params = {}
            if end_cursor:
                params['max_id'] = end_cursor
            response = self._request(f'https://i.instagram.com/api/v1/friendships/{user_id}/following/', params=params)
            if response and isinstance(response, dict):
                items = response.get('users', [])
                following.extend(items)
                fetched += len(items)
                end_cursor = response.get('next_max_id')
                if not end_cursor or len(items) == 0:
                    break
                time.sleep(random.uniform(0.5, 1.5))
            else:
                break
        return following[:limit]
    
    def get_stories(self, user_id: str) -> List[Dict]:
        response = self._request(f'https://i.instagram.com/api/v1/feed/user/{user_id}/story/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_highlights(self, user_id: str) -> List[Dict]:
        response = self._request(f'https://i.instagram.com/api/v1/highlights/{user_id}/highlights_tray/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_reels(self, user_id: str) -> List[Dict]:
        response = self._request(f'https://i.instagram.com/api/v1/clips/user/{user_id}/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_igtv(self, user_id: str) -> List[Dict]:
        response = self._request(f'https://i.instagram.com/api/v1/igtv/channel/{user_id}/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_tagged(self, user_id: str) -> List[Dict]:
        response = self._request(f'https://i.instagram.com/api/v1/usertags/{user_id}/feed/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_liked(self) -> List[Dict]:
        if not self.session_id:
            return []
        response = self._request('https://i.instagram.com/api/v1/feed/liked/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_saved(self) -> List[Dict]:
        if not self.session_id:
            return []
        response = self._request('https://i.instagram.com/api/v1/feed/saved/')
        if response and isinstance(response, dict):
            return response.get('items', [])
        return []
    
    def get_dms(self) -> List[Dict]:
        if not self.session_id:
            return []
        response = self._request('https://i.instagram.com/api/v1/direct_v2/inbox/')
        if response and isinstance(response, dict):
            return response.get('inbox', {}).get('threads', [])
        return []
    
    def calculate_engagement(self, posts: List[Dict]) -> Dict:
        if not posts:
            return {'avg_likes': 0, 'avg_comments': 0, 'avg_views': 0, 
                   'avg_saves': 0, 'avg_shares': 0, 'engagement_rate': 0}
        total_likes = sum(p.get('like_count', 0) for p in posts)
        total_comments = sum(p.get('comment_count', 0) for p in posts)
        total_views = sum(p.get('view_count', 0) for p in posts)
        total_saves = sum(p.get('save_count', 0) for p in posts)
        total_shares = sum(p.get('share_count', 0) for p in posts)
        count = len(posts)
        avg_likes = total_likes / count
        avg_comments = total_comments / count
        avg_views = total_views / count
        avg_saves = total_saves / count
        avg_shares = total_shares / count
        engagement_rate = ((avg_likes * 0.4 + avg_comments * 0.3 + 
                           avg_saves * 0.2 + avg_shares * 0.1) / 1000) * 100
        return {
            'avg_likes': avg_likes,
            'avg_comments': avg_comments,
            'avg_views': avg_views,
            'avg_saves': avg_saves,
            'avg_shares': avg_shares,
            'engagement_rate': engagement_rate,
            'post_count': count
        }
    
    def analyze_sentiment(self, text: str) -> Dict:
        if not text:
            return {'score': 0, 'label': 'neutral'}
        text_lower = text.lower()
        positive_score = sum(1 for w in self.sentiment_keywords['positive'] if w in text_lower)
        negative_score = sum(1 for w in self.sentiment_keywords['negative'] if w in text_lower)
        total = positive_score + negative_score
        if total == 0:
            return {'score': 0, 'label': 'neutral'}
        score = (positive_score - negative_score) / total
        label = 'positive' if score > 0.2 else 'negative' if score < -0.2 else 'neutral'
        return {'score': score, 'label': label}
    
    def extract_topics(self, posts: List[Dict]) -> List[str]:
        topics = defaultdict(int)
        topic_keywords = {
            'fashion': ['fashion', 'style', 'outfit', 'wear', 'dress', 'look', 'clothing'],
            'beauty': ['beauty', 'makeup', 'skincare', 'cosmetics', 'glow', 'hair'],
            'food': ['food', 'cooking', 'recipe', 'delicious', 'dinner', 'lunch', 'breakfast'],
            'travel': ['travel', 'trip', 'adventure', 'explore', 'vacation', 'wanderlust'],
            'fitness': ['fitness', 'workout', 'exercise', 'gym', 'healthy', 'fit', 'training'],
            'business': ['business', 'entrepreneur', 'startup', 'work', 'company', 'money'],
            'tech': ['tech', 'digital', 'app', 'software', 'innovation', 'gadget'],
            'art': ['art', 'creative', 'design', 'paint', 'draw', 'photography'],
            'music': ['music', 'song', 'album', 'concert', 'band', 'artist'],
            'sports': ['sports', 'game', 'team', 'player', 'champion', 'match'],
            'lifestyle': ['lifestyle', 'life', 'daily', 'routine', 'vibes', 'peace'],
            'family': ['family', 'baby', 'kids', 'mom', 'dad', 'love', 'home'],
            'education': ['education', 'learn', 'study', 'knowledge', 'skill', 'course']
        }
        for post in posts:
            caption = post.get('caption', {}).get('text', '').lower()
            for topic, keywords in topic_keywords.items():
                if any(kw in caption for kw in keywords):
                    topics[topic] += 1
        return [t for t, _ in sorted(topics.items(), key=lambda x: x[1], reverse=True)[:5]]
    
    def detect_brands(self, posts: List[Dict]) -> List[str]:
        brands = defaultdict(int)
        brand_keywords = {
            'Nike': ['nike', 'justdoit'],
            'Adidas': ['adidas', 'addidas'],
            'Apple': ['apple', 'iphone', 'macbook'],
            'Samsung': ['samsung', 'galaxy'],
            'Starbucks': ['starbucks', 'coffee'],
            'Amazon': ['amazon', 'prime'],
            'Netflix': ['netflix', 'streaming'],
            'Spotify': ['spotify', 'music'],
            'Tesla': ['tesla', 'electric car'],
            'Google': ['google', 'android'],
            'Facebook': ['facebook', 'meta'],
            'TikTok': ['tiktok', 'viral'],
            'YouTube': ['youtube', 'youtuber'],
            'Disney': ['disney', 'marvel'],
            'McDonalds': ['mcdonalds', 'mcd'],
            'Coca-Cola': ['coca-cola', 'coke'],
            'Pepsi': ['pepsi', 'pepsi cola'],
            'Gucci': ['gucci', 'gucci mane'],
            'Chanel': ['chanel', 'coco chanel'],
            'Louis Vuitton': ['louis vuitton', 'lv']
        }
        for post in posts:
            caption = post.get('caption', {}).get('text', '').lower()
            for brand, keywords in brand_keywords.items():
                if any(kw in caption for kw in keywords):
                    brands[brand] += 1
        return [b for b, _ in sorted(brands.items(), key=lambda x: x[1], reverse=True)[:5]]
    
    def calculate_viral_score(self, posts: List[Dict]) -> float:
        if not posts:
            return 0.0
        total_engagement = sum(p.get('like_count', 0) + p.get('comment_count', 0) + 
                              p.get('save_count', 0) for p in posts)
        avg_engagement = total_engagement / len(posts)
        viral_posts = 0
        for post in posts:
            likes = post.get('like_count', 0)
            comments = post.get('comment_count', 0)
            if likes > 1000 and comments > 100:
                viral_posts += 1
        viral_ratio = viral_posts / len(posts)
        score = min(1.0, (avg_engagement / 1000) * 0.7 + viral_ratio * 0.3)
        return score * 100
    
    def calculate_content_quality(self, posts: List[Dict]) -> float:
        if not posts:
            return 0.0
        quality_scores = []
        for post in posts:
            score = 0.0
            caption = post.get('caption', {}).get('text', '')
            caption_len = len(caption)
            if 50 <= caption_len <= 200:
                score += 0.3
            elif caption_len > 200:
                score += 0.2
            hashtags = re.findall(r'#\w+', caption)
            if len(hashtags) >= 5:
                score += 0.2
            media_type = 'image'
            if post.get('video_versions'):
                media_type = 'video'
            elif post.get('carousel_media'):
                media_type = 'carousel'
            if media_type in ['video', 'carousel']:
                score += 0.3
            likes = post.get('like_count', 0)
            comments = post.get('comment_count', 0)
            if likes > 0 and comments > 0:
                ratio = comments / likes
                if 0.05 <= ratio <= 0.3:
                    score += 0.2
            quality_scores.append(score)
        avg_score = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        return avg_score * 100
    
    def analyze_best_time(self, posts: List[Dict]) -> Dict:
        by_hour = defaultdict(list)
        by_day = defaultdict(list)
        for post in posts:
            timestamp = post.get('taken_at')
            if timestamp:
                try:
                    dt = datetime.fromtimestamp(timestamp)
                    engagement = post.get('like_count', 0) + post.get('comment_count', 0)
                    by_hour[dt.hour].append(engagement)
                    by_day[dt.strftime('%A')].append(engagement)
                except:
                    pass
        best_hour = None
        best_hour_avg = 0
        for hour, engagements in by_hour.items():
            if engagements:
                avg = sum(engagements) / len(engagements)
                if avg > best_hour_avg:
                    best_hour_avg = avg
                    best_hour = hour
        best_day = None
        best_day_avg = 0
        for day, engagements in by_day.items():
            if engagements:
                avg = sum(engagements) / len(engagements)
                if avg > best_day_avg:
                    best_day_avg = avg
                    best_day = day
        return {'best_hour': best_hour, 'best_day': best_day}
    
    def analyze_growth(self, profile: Dict, engagement: Dict) -> Dict:
        followers = profile.get('follower_count', 0)
        engagement_rate = engagement.get('engagement_rate', 0)
        if followers == 0:
            return {'rate': 0, 'trend': 'stable', 'predicted': {}}
        growth_rate = (engagement_rate * 0.3) * 0.01
        trend = 'rising' if growth_rate > 0.05 else 'declining' if growth_rate < -0.05 else 'stable'
        predicted = {
            '1_month': followers * (1 + growth_rate),
            '3_months': followers * (1 + growth_rate * 3),
            '6_months': followers * (1 + growth_rate * 6),
            '1_year': followers * (1 + growth_rate * 12)
        }
        return {'rate': growth_rate, 'trend': trend, 'predicted': predicted}
    
    def build_hashtag_network(self, posts: List[Dict]) -> Dict:
        network = defaultdict(list)
        for post in posts:
            caption = post.get('caption', {}).get('text', '')
            hashtags = re.findall(r'#\w+', caption)
            for i, h1 in enumerate(hashtags):
                for h2 in hashtags[i+1:]:
                    if h2 not in network[h1]:
                        network[h1].append(h2)
                    if h1 not in network[h2]:
                        network[h2].append(h1)
        return dict(network)
    
    def build_mention_network(self, posts: List[Dict]) -> Dict:
        network = defaultdict(list)
        for post in posts:
            caption = post.get('caption', {}).get('text', '')
            mentions = re.findall(r'@\w+', caption)
            for i, m1 in enumerate(mentions):
                for m2 in mentions[i+1:]:
                    if m2 not in network[m1]:
                        network[m1].append(m2)
                    if m1 not in network[m2]:
                        network[m2].append(m1)
        return dict(network)
    
    def extract_keywords(self, username: str, custom_keywords: List[str], profile: Dict) -> List[str]:
        keywords = set()
        keywords.add(username)
        keywords.update(re.split(r'[._-]', username))
        if profile:
            if profile.get('full_name'):
                keywords.update(profile['full_name'].split())
            if profile.get('biography'):
                bio = profile['biography']
                keywords.update(re.findall(r'\b\w{3,}\b', bio))
                keywords.update(re.findall(r'#\w+', bio))
                keywords.update(re.findall(r'@\w+', bio))
            if profile.get('external_url'):
                domain = re.sub(r'https?://', '', profile['external_url']).split('/')[0]
                keywords.add(domain)
        if custom_keywords:
            keywords.update(custom_keywords)
        default_keywords = ['suspicious', 'location', 'event', 'business', 'meeting', 
                           'activity', 'deal', 'investment', 'client', 'partner',
                           'confidential', 'private', 'secret', 'exclusive', 'invite']
        keywords.update(default_keywords)
        return list(dict.fromkeys([k.lower().strip() for k in keywords if k and len(k) > 2]))[:25]
    
    def build_dorks(self, username: str, keywords: List[str]) -> List[DorkResult]:
        dorks = []
        base = f'site:instagram.com "{username}"'
        dork_types = [
            ('profile', base),
            ('posts', f'{base} (post OR photo OR video OR reel)'),
            ('hashtags', f'{base} (#* OR hashtag*)'),
            ('mentions', f'{base} (@* OR mention*)'),
            ('location', f'{base} location*'),
            ('business', f'{base} (business OR company OR brand OR shop)'),
            ('email', f'{base} email*'),
            ('phone', f'{base} phone*'),
            ('url', f'{base} (url* OR link*)'),
            ('verification', f'{base} (verified OR official OR authentic)'),
            ('following', f'{base} (following OR followers)'),
            ('stories', f'{base} story*')
        ]
        for name, query in dork_types:
            dorks.append(DorkResult(
                query=query,
                url=f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}",
                platform='google',
                keywords=[]
            ))
        if keywords:
            for keyword in keywords[:8]:
                query = f'{base} ("{keyword}")'
                dorks.append(DorkResult(
                    query=query,
                    url=f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}",
                    platform='google',
                    keywords=[]
                ))
        return dorks
    
    def calculate_score(self, profile: Dict, posts: List[Dict], engagement: Dict) -> float:
        score = 0.0
        if profile:
            score += 2.0
            if profile.get('is_verified'): score += 1.0
            if profile.get('is_business'): score += 0.5
            if profile.get('follower_count', 0) > 1000: score += 0.5
            if profile.get('follower_count', 0) > 10000: score += 0.5
            if profile.get('media_count', 0) > 10: score += 0.5
            if profile.get('media_count', 0) > 50: score += 0.5
            if profile.get('public_email'): score += 0.3
            if profile.get('public_phone_number'): score += 0.3
        if posts:
            score += min(2.0, len(posts) * 0.04)
        if engagement:
            score += min(2.0, engagement.get('engagement_rate', 0) * 0.2)
        return min(score, 10.0)
    
    def run(self, username: str, custom_keywords: List[str] = None,
            target_name: str = "", target_email: str = "", target_phone: str = "") -> EngineResult:
        start_time = time.time()
        result = EngineResult(engine_name="MODERN", username=username, status="RUNNING")
        try:
            print(f"{GoblinColors.CYAN}🚀 Step 1: Getting user ID...{GoblinColors.RESET}")
            user_id = self.get_user_id(username)
            if not user_id:
                result.status = "ERROR"
                result.error = "Could not get user ID"
                return result
            print(f"{GoblinColors.CYAN}📊 Step 2: Fetching profile data...{GoblinColors.RESET}")
            profile = self.get_profile(username)
            if profile:
                profile_data = ProfileData(username=username)
                profile_data.user_id = user_id
                profile_data.numeric_id = user_id
                profile_data.full_name = profile.get('full_name', '')
                profile_data.biography = profile.get('biography', '')
                profile_data.external_url = profile.get('external_url', '')
                profile_data.is_private = profile.get('is_private', False)
                profile_data.is_verified = profile.get('is_verified', False)
                profile_data.is_business = profile.get('is_business', False)
                profile_data.follower_count = profile.get('follower_count', 0)
                profile_data.following_count = profile.get('following_count', 0)
                profile_data.post_count = profile.get('media_count', 0)
                profile_data.profile_pic_url = profile.get('profile_pic_url', '')
                profile_data.public_email = profile.get('public_email', '')
                profile_data.public_phone = profile.get('public_phone_number', '')
                profile_data.category = profile.get('category', '')
                if profile_data.biography:
                    profile_data.bio_links = re.findall(r'https?://[^\s]+', profile_data.biography)
                    profile_data.hashtags_used = re.findall(r'#\w+', profile_data.biography)
                    profile_data.mentions = re.findall(r'@\w+', profile_data.biography)
                result.profile = profile_data
                print(f"{GoblinColors.GOBLIN_GREEN}✅ Profile data fetched{GoblinColors.RESET}")
            print(f"{GoblinColors.CYAN}📸 Step 3: Extracting posts...{GoblinColors.RESET}")
            posts = self.get_posts(user_id, 50)
            if result.profile:
                result.profile.posts = posts
            print(f"{GoblinColors.CYAN}📈 Step 4: Calculating engagement...{GoblinColors.RESET}")
            engagement = self.calculate_engagement(posts)
            if result.profile:
                result.profile.avg_likes = engagement.get('avg_likes', 0)
                result.profile.avg_comments = engagement.get('avg_comments', 0)
                result.profile.engagement_rate = engagement.get('engagement_rate', 0)
                result.profile.avg_saves = engagement.get('avg_saves', 0)
                result.profile.avg_shares = engagement.get('avg_shares', 0)
                result.profile.avg_views = engagement.get('avg_views', 0)
            print(f"{GoblinColors.CYAN}📖 Step 5: Extracting stories...{GoblinColors.RESET}")
            stories = self.get_stories(user_id)
            if result.profile:
                result.profile.stories = stories
            print(f"{GoblinColors.CYAN}⭐ Step 6: Extracting highlights...{GoblinColors.RESET}")
            highlights = self.get_highlights(user_id)
            if result.profile:
                result.profile.highlights = highlights
            print(f"{GoblinColors.CYAN}🏷️ Step 7: Extracting tagged posts...{GoblinColors.RESET}")
            tagged = self.get_tagged(user_id)
            if result.profile:
                result.profile.tagged_posts = tagged
            print(f"{GoblinColors.CYAN}🎬 Step 8: Extracting reels...{GoblinColors.RESET}")
            reels = self.get_reels(user_id)
            if result.profile:
                result.profile.reels = reels
            print(f"{GoblinColors.CYAN}📺 Step 9: Extracting IGTV...{GoblinColors.RESET}")
            igtv = self.get_igtv(user_id)
            if result.profile:
                result.profile.igtv = igtv
            print(f"{GoblinColors.CYAN}👥 Step 10: Extracting followers...{GoblinColors.RESET}")
            followers = self.get_followers(user_id, 30)
            print(f"{GoblinColors.CYAN}👤 Step 11: Extracting following...{GoblinColors.RESET}")
            following = self.get_following(user_id, 30)
            if self.session_id:
                print(f"{GoblinColors.CYAN}💾 Step 12: Getting saved/liked/DMs...{GoblinColors.RESET}")
                liked = self.get_liked()
                saved = self.get_saved()
                dms = self.get_dms()
                if result.profile:
                    result.profile.liked_posts = liked
                    result.profile.saved_posts = saved
                    result.profile.direct_messages = dms
            print(f"{GoblinColors.CYAN}🧠 Step 13: Analyzing content...{GoblinColors.RESET}")
            topics = self.extract_topics(posts)
            if result.profile:
                result.profile.topics = topics
            brands = self.detect_brands(posts)
            if result.profile:
                result.profile.brand_affinity = brands
            best_time = self.analyze_best_time(posts)
            if result.profile and best_time:
                result.profile.best_posting_time = best_time.get('best_hour')
                result.profile.best_posting_day = best_time.get('best_day')
            viral_score = self.calculate_viral_score(posts)
            if result.profile:
                result.profile.viral_score = viral_score
            content_quality = self.calculate_content_quality(posts)
            if result.profile:
                result.profile.content_quality_score = content_quality
            hashtag_network = self.build_hashtag_network(posts)
            if result.profile:
                result.profile.hashtag_network = hashtag_network
            mention_network = self.build_mention_network(posts)
            if result.profile:
                result.profile.mention_network = mention_network
            growth = self.analyze_growth(profile, engagement) if profile else {}
            if result.profile:
                result.profile.growth_rate = growth.get('rate', 0)
                result.profile.growth_trend = growth.get('trend', 'stable')
                result.profile.predicted_growth = growth.get('predicted', {})
            result.keywords = self.extract_keywords(username, custom_keywords, profile)
            result.dorks = self.build_dorks(username, result.keywords)
            result.score = self.calculate_score(profile, posts, engagement)
            result.status = "COMPLETED"
            print(f"{GoblinColors.GOBLIN_GREEN}✅ Modern analysis complete! Score: {result.score:.2f}/10.0{GoblinColors.RESET}")
        except Exception as e:
            result.status = "ERROR"
            result.error = str(e)
            traceback.print_exc()
        result.execution_time = time.time() - start_time
        return result

# ==================== COMPLETE ATTACK SYSTEM ====================

class CompleteAttack:
    """Complete attack system with both engines"""
    
    def __init__(self, session_id: str = None):
        self.session_id = session_id
        self.legacy = LegacyEngine(session_id)
        self.modern = ModernEngine(session_id)
        self.all_dorks = []
        self.all_keywords = []
    
    def run(self, username: str, custom_keywords: List[str] = None,
            target_name: str = "", target_email: str = "", target_phone: str = "") -> FullAttackResult:
        print(f"\n{GoblinColors.GOBLIN_GOLD}🌊 GOBLIN TSUNAMI - COMPLETE ATTACK{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}🎯 Target: @{username}{GoblinColors.RESET}")
        print(f"{GoblinColors.DIRT_YELLOW}🔑 Keywords: {len(custom_keywords) if custom_keywords else 0}{GoblinColors.RESET}")
        print(f"{GoblinColors.POISON_PURPLE}⚔️ Engines: LEGACY + MODERN (Dual Attack){GoblinColors.RESET}\n")
        
        print(f"{GoblinColors.CYAN}⚡ Running LEGACY engine...{GoblinColors.RESET}")
        legacy_result = self.legacy.run(username, custom_keywords, target_name, target_email, target_phone)
        
        print(f"\n{GoblinColors.CYAN}⚡ Running MODERN engine...{GoblinColors.RESET}")
        modern_result = self.modern.run(username, custom_keywords, target_name, target_email, target_phone)
        
        self.all_keywords = list(dict.fromkeys(legacy_result.keywords + modern_result.keywords))
        self.all_dorks = legacy_result.dorks + modern_result.dorks
        
        winner = self._determine_winner(legacy_result, modern_result)
        
        attack_result = FullAttackResult(
            username=username,
            session_id=self.session_id[:8] + '...' if self.session_id else 'N/A',
            custom_keywords=custom_keywords or [],
            timestamp=datetime.now().isoformat(),
            legacy=legacy_result,
            modern=modern_result,
            winner=winner,
            combined_score=(legacy_result.score + modern_result.score) / 2,
            all_dorks=self.all_dorks,
            all_keywords=self.all_keywords,
            summary=self._generate_summary(legacy_result, modern_result, winner)
        )
        
        self._display_results(attack_result)
        self._save_results(attack_result)
        
        return attack_result
    
    def _determine_winner(self, legacy: EngineResult, modern: EngineResult) -> str:
        if legacy.status == "ERROR" and modern.status == "ERROR":
            return "DRAW - Both Failed"
        elif legacy.status == "ERROR":
            return "MODERN - Legacy Failed"
        elif modern.status == "ERROR":
            return "LEGACY - Modern Failed"
        elif legacy.score > modern.score:
            return "LEGACY 🏆"
        elif modern.score > legacy.score:
            return "MODERN 🏆"
        else:
            return "DRAW 🤝"
    
    def _generate_summary(self, legacy: EngineResult, modern: EngineResult, winner: str) -> Dict:
        return {
            'legacy_score': legacy.score,
            'modern_score': modern.score,
            'winner': winner,
            'legacy_time': legacy.execution_time,
            'modern_time': modern.execution_time,
            'legacy_status': legacy.status,
            'modern_status': modern.status,
            'score_difference': abs(legacy.score - modern.score)
        }
    
    def _display_results(self, result: FullAttackResult):
        print(f"\n{GoblinColors.GOBLIN_GOLD}{'='*80}{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}🌊 ATTACK COMPLETE - FULL RESULTS{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}{'='*80}{GoblinColors.RESET}")
        
        print(f"\n{GoblinColors.CYAN}🎯 Target: @{result.username}{GoblinColors.RESET}")
        print(f"{GoblinColors.CYAN}🔑 Keywords: {len(result.all_keywords)}{GoblinColors.RESET}")
        print(f"{GoblinColors.CYAN}🏆 Winner: {result.winner}{GoblinColors.RESET}")
        print(f"{GoblinColors.CYAN}📊 Combined Score: {result.combined_score:.2f}/10.0{GoblinColors.RESET}")
        print(f"{GoblinColors.CYAN}⏱️ Total Time: {result.legacy.execution_time + result.modern.execution_time:.2f}s{GoblinColors.RESET}")
        
        print(f"\n{GoblinColors.CYAN_WAVE}⚔️ BATTLE STATISTICS{GoblinColors.RESET}")
        print(f"{GoblinColors.DIM}{'-'*80}{GoblinColors.RESET}")
        print(f"{GoblinColors.DIM}Metric{' ':<30} LEGACY     MODERN{GoblinColors.RESET}")
        print(f"{GoblinColors.DIM}{'-'*80}{GoblinColors.RESET}")
        print(f"Score{' ':<34} {result.legacy.score:.2f}      {result.modern.score:.2f}")
        print(f"Execution Time{' ':<26} {result.legacy.execution_time:.2f}s    {result.modern.execution_time:.2f}s")
        print(f"Status{' ':<34} {result.legacy.status}     {result.modern.status}")
        print(f"Profile Data{' ':<29} {'✅' if result.legacy.profile else '❌'}      {'✅' if result.modern.profile else '❌'}")
        print(f"Keywords{' ':<32} {len(result.legacy.keywords):<6}     {len(result.modern.keywords):<6}")
        print(f"Dorks{' ':<35} {len(result.legacy.dorks):<6}     {len(result.modern.dorks):<6}")
        print(f"Matches{' ':<33} {len(result.legacy.matches):<6}     N/A")
        
        if result.modern.profile:
            print(f"Stories{' ':<33} N/A         {len(result.modern.profile.stories):<6}")
            print(f"Highlights{' ':<30} N/A         {len(result.modern.profile.highlights):<6}")
            print(f"Reels{' ':<35} N/A         {len(result.modern.profile.reels):<6}")
            print(f"IGTV{' ':<36} N/A         {len(result.modern.profile.igtv):<6}")
            print(f"Viral Score{' ':<29} N/A         {result.modern.profile.viral_score:.1f}%")
            print(f"Content Quality{' ':<26} N/A         {result.modern.profile.content_quality_score:.1f}%")
        
        if result.legacy.profile:
            print(f"\n{GoblinColors.LEGACY_GOLD}🔮 LEGACY PROFILE{GoblinColors.RESET}")
            p = result.legacy.profile
            print(f"  Username: @{p.username}")
            print(f"  Full Name: {p.full_name}")
            print(f"  Bio: {p.biography[:150]}...")
            print(f"  Followers: {p.follower_count:,}")
            print(f"  Following: {p.following_count:,}")
            print(f"  Posts: {p.post_count:,}")
            print(f"  Private: {'✅' if p.is_private else '❌'}")
            print(f"  Verified: {'✅' if p.is_verified else '❌'}")
            print(f"  Business: {'✅' if p.is_business else '❌'}")
            if p.public_email: print(f"  Public Email: {p.public_email}")
            if p.public_phone: print(f"  Public Phone: {p.public_phone}")
            if p.obfuscated_email: print(f"  Obfuscated Email: {p.obfuscated_email}")
            if p.obfuscated_phone: print(f"  Obfuscated Phone: {p.obfuscated_phone}")
        
        if result.modern.profile:
            print(f"\n{GoblinColors.MODERN_CYAN}🚀 MODERN PROFILE{GoblinColors.RESET}")
            p = result.modern.profile
            print(f"  Username: @{p.username}")
            print(f"  Full Name: {p.full_name}")
            print(f"  Bio: {p.biography[:150]}...")
            print(f"  Followers: {p.follower_count:,}")
            print(f"  Following: {p.following_count:,}")
            print(f"  Posts: {p.post_count:,}")
            print(f"  Private: {'✅' if p.is_private else '❌'}")
            print(f"  Verified: {'✅' if p.is_verified else '❌'}")
            print(f"  Business: {'✅' if p.is_business else '❌'}")
            if p.business_email: print(f"  Business Email: {p.business_email}")
            if p.business_phone: print(f"  Business Phone: {p.business_phone}")
            if p.avg_likes > 0: print(f"  Avg Likes: {p.avg_likes:.0f}")
            if p.avg_comments > 0: print(f"  Avg Comments: {p.avg_comments:.0f}")
            if p.avg_saves > 0: print(f"  Avg Saves: {p.avg_saves:.0f}")
            if p.avg_shares > 0: print(f"  Avg Shares: {p.avg_shares:.0f}")
            if p.avg_views > 0: print(f"  Avg Views: {p.avg_views:.0f}")
            if p.engagement_rate > 0: print(f"  Engagement Rate: {p.engagement_rate:.2f}%")
            if p.sentiment_label != 'neutral': print(f"  Sentiment: {p.sentiment_label.upper()}")
            if p.topics: print(f"  Topics: {', '.join(p.topics[:5])}")
            if p.brand_affinity: print(f"  Brands: {', '.join(p.brand_affinity[:5])}")
            if p.stories: print(f"  Stories: {len(p.stories)}")
            if p.highlights: print(f"  Highlights: {len(p.highlights)}")
            if p.tagged_posts: print(f"  Tagged Posts: {len(p.tagged_posts)}")
            if p.reels: print(f"  Reels: {len(p.reels)}")
            if p.igtv: print(f"  IGTV: {len(p.igtv)}")
            if p.best_posting_time: print(f"  Best Time: {p.best_posting_time}:00")
            if p.best_posting_day: print(f"  Best Day: {p.best_posting_day}")
            if p.growth_trend != 'stable': print(f"  Growth Trend: {p.growth_trend.upper()}")
            if p.viral_score > 0: print(f"  Viral Score: {p.viral_score:.1f}%")
            if p.content_quality_score > 0: print(f"  Content Quality: {p.content_quality_score:.1f}%")
            if p.hashtag_network: print(f"  Hashtag Network: {len(p.hashtag_network)} connections")
            if p.mention_network: print(f"  Mention Network: {len(p.mention_network)} connections")
        
        print(f"\n{GoblinColors.GOBLIN_GOLD}🔑 ALL KEYWORDS ({len(result.all_keywords)}){GoblinColors.RESET}")
        print(f"{GoblinColors.DIM}{', '.join([f'#{k}' for k in result.all_keywords[:20]])}{GoblinColors.RESET}")
        
        print(f"\n{GoblinColors.POISON_PURPLE}🔍 ALL DORKS ({len(result.all_dorks)}){GoblinColors.RESET}")
        for i, dork in enumerate(result.all_dorks[:10], 1):
            print(f"  {i}. {dork.platform}: {dork.query[:60]}...")
        
        if result.legacy.matches:
            print(f"\n{GoblinColors.NEO_GREEN}🎯 MATCHES FOUND{GoblinColors.RESET}")
            for match in result.legacy.matches[:5]:
                print(f"  @{match.username} - {match.match_level} ({match.confidence_score:.0%})")
        
        self._open_dorks(result)
        print(f"\n{GoblinColors.GOBLIN_GOLD}{'='*80}{GoblinColors.RESET}")
    
    def _open_dorks(self, result: FullAttackResult):
        print(f"\n{GoblinColors.GOBLIN_GOLD}🌐 Opening top dorks in browser...{GoblinColors.RESET}")
        for dork in result.all_dorks[:5]:
            try:
                webbrowser.open(dork.url)
                print(f"{GoblinColors.DIM}✓ {dork.platform}: {dork.query[:40]}...{GoblinColors.RESET}")
                time.sleep(0.5)
            except:
                pass
    
    def _save_results(self, result: FullAttackResult):
        fname = f"attack_{result.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        export = {
            'attack': {
                'username': result.username,
                'session_id': result.session_id,
                'custom_keywords': result.custom_keywords,
                'timestamp': result.timestamp,
                'winner': result.winner,
                'combined_score': result.combined_score,
                'summary': result.summary
            },
            'legacy': {
                'status': result.legacy.status,
                'score': result.legacy.score,
                'execution_time': result.legacy.execution_time,
                'profile': result.legacy.profile.to_dict() if result.legacy.profile else None,
                'keywords': result.legacy.keywords,
                'dorks': [d.__dict__ for d in result.legacy.dorks],
                'matches': [m.__dict__ for m in result.legacy.matches]
            },
            'modern': {
                'status': result.modern.status,
                'score': result.modern.score,
                'execution_time': result.modern.execution_time,
                'profile': result.modern.profile.to_dict() if result.modern.profile else None,
                'keywords': result.modern.keywords,
                'dorks': [d.__dict__ for d in result.modern.dorks]
            },
            'combined': {
                'all_keywords': result.all_keywords,
                'total_dorks': len(result.all_dorks)
            }
        }
        try:
            with open(fname, 'w') as f:
                json.dump(export, f, indent=2, default=str)
            print(f"\n{GoblinColors.GOBLIN_GREEN}💾 Results saved to: {fname}{GoblinColors.RESET}")
        except Exception as e:
            print(f"{GoblinColors.BLOOD_RED}❌ Save error: {e}{GoblinColors.RESET}")

# ==================== MAIN APPLICATION ====================

class MainApp:
    """Complete main application"""
    
    def __init__(self):
        self.banner = CompleteBanner()
        self.session_id = None
        self.username = None
        self.keywords = []
        self.target_name = ""
        self.target_email = ""
        self.target_phone = ""
    
    def display_welcome(self):
        self.banner.clear()
        self.banner.header("🌊 GOBLIN TSUNAMI - COMPLETE ULTIMATE")
        print()
        for line in BANNER_ART.split('\n')[1:]:
            if line.strip():
                for c in line:
                    color = random.choice([GoblinColors.GOBLIN_GREEN, GoblinColors.MOSS_GREEN,
                                          GoblinColors.SWAMP_GREEN, GoblinColors.RUST_ORANGE,
                                          GoblinColors.GOBLIN_GOLD, GoblinColors.POISON_PURPLE])
                    print(color + c + GoblinColors.RESET, end='', flush=True)
                    time.sleep(0.002)
                print()
                time.sleep(0.02)
            else:
                print()
                time.sleep(0.01)
        print()
        print(f"{GoblinColors.GOBLIN_GOLD}        ⚔ GOBLIN TSUNAMI - COMPLETE ULTIMATE ⚔{GoblinColors.RESET}")
        print(f"{GoblinColors.BLOOD_RED}{GoblinColors.BOLD}    Author: SYLHETYHACKVENGER (THE-ERROR808){GoblinColors.RESET}")
        print(f"{GoblinColors.DIRT_YELLOW}    Twitter: {GoblinColors.GOBLIN_GOLD}@blackeko5{GoblinColors.RESET}")
        print(f"{GoblinColors.DIRT_YELLOW}    Version: 15.0.0 - COMPLETE ULTIMATE{GoblinColors.RESET}")
        print(f"{GoblinColors.POISON_PURPLE}    🏴‍☠️ Goblin Horde - 2026 🏴‍☠️{GoblinColors.RESET}")
        print(f"{GoblinColors.EYE_GLOW}    👁️  {GoblinColors.BOLD}WATCHING THE IG WITH SESSION POWER...{GoblinColors.RESET}")
        print()
        self.banner.footer()
        print()
    
    def get_inputs(self):
        print(f"\n{GoblinColors.GOBLIN_GREEN}📋 INPUT REQUIRED{GoblinColors.RESET}")
        print(f"{GoblinColors.DIM}Provide the following information:{GoblinColors.RESET}\n")
        self.session_id = input(f"{GoblinColors.GOBLIN_GREEN}🔑 Enter Instagram Session ID{GoblinColors.RESET}\n{GoblinColors.DIM}(Press Enter to skip): {GoblinColors.RESET}").strip()
        self.username = input(f"{GoblinColors.GOBLIN_GREEN}🎯 Enter Target Username: {GoblinColors.RESET}").strip()
        print(f"{GoblinColors.DIM}💡 Default: intelligence,osint,session,stealth,confidential,private,secret,exclusive{GoblinColors.RESET}")
        kw = input(f"{GoblinColors.GOBLIN_GOLD}🔑 Enter Custom Keywords{GoblinColors.RESET}\n{GoblinColors.DIM}(Comma-separated): {GoblinColors.RESET}").strip()
        if kw:
            self.keywords = [k.strip() for k in kw.split(',') if k.strip()]
        else:
            self.keywords = ['intelligence', 'osint', 'session', 'stealth', 'confidential', 
                           'private', 'secret', 'exclusive', 'sensitive', 'restricted']
        self.target_name = input(f"{GoblinColors.DIM}👤 Target Full Name (optional): {GoblinColors.RESET}").strip()
        self.target_email = input(f"{GoblinColors.DIM}📧 Target Email (optional): {GoblinColors.RESET}").strip()
        self.target_phone = input(f"{GoblinColors.DIM}📱 Target Phone (optional): {GoblinColors.RESET}").strip()
    
    def display_plan(self):
        print()
        print(f"{GoblinColors.GOBLIN_GOLD}{'='*60}{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}📊 DATA COLLECTION PLAN{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}{'='*60}{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Profile Information{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Posts & Engagement{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Followers & Following{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Stories & Highlights{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Reels & IGTV{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Tagged Posts{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Engagement Analytics{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Topic Extraction{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Brand Detection{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Viral Score{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Content Quality{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Hashtag Network{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GREEN}✅ Mention Network{GoblinColors.RESET}")
        print(f"{GoblinColors.POISON_PURPLE}💡 WITH SESSION: Liked/Saved/DMs{GoblinColors.RESET}")
        print(f"{GoblinColors.GOBLIN_GOLD}{'='*60}{GoblinColors.RESET}")
    
    def run(self):
        while True:
            try:
                self.display_welcome()
                print(f"""
{GoblinColors.GOBLIN_GREEN}   ╔════════════════════════════════════════════╗{GoblinColors.RESET}
{GoblinColors.GOBLIN_GREEN}   ║{GoblinColors.RESET}  {GoblinColors.BOLD}{GoblinColors.MOSS_GREEN}🐉 MAIN MENU 🐉{GoblinColors.RESET}              {GoblinColors.GOBLIN_GREEN}║{GoblinColors.RESET}
{GoblinColors.GOBLIN_GREEN}   ╚════════════════════════════════════════════╝{GoblinColors.RESET}
{GoblinColors.CAVE_BROWN}   ╔════════════════════════════════════════════╗{GoblinColors.RESET}
{GoblinColors.CAVE_BROWN}   ║{GoblinColors.RESET}  {GoblinColors.GOBLIN_GREEN}1.{GoblinColors.RESET} Complete Attack              {GoblinColors.CAVE_BROWN}║{GoblinColors.RESET}
{GoblinColors.CAVE_BROWN}   ║{GoblinColors.RESET}  {GoblinColors.GOBLIN_GOLD}2.{GoblinColors.RESET} Banner Renderer               {GoblinColors.CAVE_BROWN}║{GoblinColors.RESET}
{GoblinColors.CAVE_BROWN}   ║{GoblinColors.RESET}  {GoblinColors.BLOOD_RED}3.{GoblinColors.RESET} Exit                          {GoblinColors.CAVE_BROWN}║{GoblinColors.RESET}
{GoblinColors.CAVE_BROWN}   ╚════════════════════════════════════════════╝{GoblinColors.RESET}
""")
                choice = input(f"{GoblinColors.GOBLIN_GOLD}Choice (1-3): {GoblinColors.RESET}").strip()
                if choice == '1':
                    self.get_inputs()
                    if not self.username:
                        print(f"{GoblinColors.BLOOD_RED}❌ Username required!{GoblinColors.RESET}")
                        time.sleep(1)
                        continue
                    self.display_plan()
                    confirm = input(f"{GoblinColors.GOBLIN_GOLD}Proceed with attack? (y/n): {GoblinColors.RESET}").strip().lower()
                    if confirm == 'y':
                        attack = CompleteAttack(self.session_id)
                        attack.run(self.username, self.keywords, self.target_name, self.target_email, self.target_phone)
                    else:
                        print(f"{GoblinColors.BLOOD_RED}Attack cancelled!{GoblinColors.RESET}")
                    input(f"{GoblinColors.GOBLIN_GOLD}Press Enter to continue...{GoblinColors.RESET}")
                elif choice == '2':
                    self.banner.menu()
                elif choice == '3':
                    self.banner.exit_animation()
                    break
                else:
                    print(f"{GoblinColors.BLOOD_RED}❌ Invalid choice!{GoblinColors.RESET}")
                    time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{GoblinColors.BLOOD_RED}🌊 Interrupted!{GoblinColors.RESET}")
                break
            except Exception as e:
                print(f"{GoblinColors.BLOOD_RED}❌ Error: {e}{GoblinColors.RESET}")
                traceback.print_exc()
                time.sleep(2)

# ==================== MAIN ====================

if __name__ == "__main__":
    app = MainApp()
    app.run()
