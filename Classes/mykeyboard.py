import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

key = {
  "F1": 0x3B,
  "F2": 0x3C,
  "F3": 0x3D,
  "F4": 0x3E,
  "F5": 0x3F,
  "F6": 0x40,
  "F7": 0x41,
  "F8": 0x42,
  "F9": 0x43,
  "F10": 0x44,
  "F11": 0x57,
  "F12": 0x58,
  "ENTER": 0x1C,
  "CTROL": 0x1D,
  "BACKSPACE": 0x0E,
  "CAPS": 0x3A,
  "NUNLOCK": 0x45,
  "TAB": 0x0F,
  "UP" : 0xC8,
  "LEFT" : 0xCB,
  "RIGHT" : 0xCD,
  "DOWN" : 0xD0,
  "ENTER" : 0x1C,
  "ESC" : 0x01,
  "SPACE": 0x39
}

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
  _fields_ = [
    ("wVk", ctypes.c_ushort),
    ("wScan", ctypes.c_ushort),
    ("dwFlags", ctypes.c_ulong),
    ("time", ctypes.c_ulong),
    ("dwExtraInfo", PUL)
  ]

class HardwareInput(ctypes.Structure):
  _fields_ = [
    ("uMsg", ctypes.c_ulong),
    ("wParamL", ctypes.c_short),
    ("wParamH", ctypes.c_ushort)
  ]

class MouseInput(ctypes.Structure):
  _fields_ = [
    ("dx", ctypes.c_long),
    ("dy", ctypes.c_long),
    ("mouseData", ctypes.c_ulong),
    ("dwFlags", ctypes.c_ulong),
    ("time", ctypes.c_ulong),
    ("dwExtraInfo", PUL)
  ]

class Input_I(ctypes.Union):
  _fields_ = [
    ("ki", KeyBdInput),
    ("mi", MouseInput),
    ("hi", HardwareInput)
  ]


class Input(ctypes.Structure):
  _fields_ = [
    ("type", ctypes.c_ulong),
    ("ii", Input_I)
  ]

# Actuals Functions
def key_down(hotkey):
  hexKeyCode = key[hotkey.upper()]
  extra = ctypes.c_ulong(0)
  ii_ = Input_I()
  ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
  x = Input(ctypes.c_ulong(1), ii_)
  ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hotkey):
  hexKeyCode = key[hotkey.upper()]
  extra = ctypes.c_ulong(0)
  ii_ = Input_I()
  ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
  x = Input(ctypes.c_ulong(1), ii_)
  ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def press_key(hotkey, delay=0.5):
  key_down(hotkey)
  time.sleep(delay)
  release_key(hotkey)