import pyautogui
import keyboard
import Classes.mykeyboard as mykeyboard
from time import sleep

IMG_SIZES = {
  'bubble': (76, 76)
  , 'fishing_location': (100, 100)
}

MINIGAME_REGION = (951, 487, 17, 347)

def main():
  #start fishing
  start_fishing()

def start_fishing():
  while True:
    #search fishing location
    oFishingLocation = find_fishing_location()

    #set fishing rod to random fishing position
    oFishingLocation = fish(oFishingLocation)

    #wait for fish
    wait_bubble(oFishingLocation)

    #solv minigame if exists
    minigame()

    #wait for next fish
    sleep(5)

def wait_bubble(oFishingLocation):
  oRegion = (oFishingLocation.x-100, oFishingLocation.y-100, oFishingLocation.x+150, oFishingLocation.y+150)
  while True:
    oBubble = pyautogui.locateOnScreen('img/bubble.png', confidence=0.8, region=oRegion)
    if(oBubble):
      mykeyboard.press_key('f11')
      return True

def minigame():
  global MINIGAME_REGION

  sleep(2)

  oFish = True
  while oFish != None:
    oBar = pyautogui.locateOnScreen('img/bar.png', region=MINIGAME_REGION)
    oFish = pyautogui.locateOnScreen('img/fish.png', confidence=0.8, region=MINIGAME_REGION, grayscale=True)
    if oBar != None and oFish != None:
      print((oBar.top, oFish.top))
      if oBar.top > oFish.top:
        mykeyboard.key_down('space')
      else:
        mykeyboard.release_key('space')
    else:
      mykeyboard.key_down('space')
      mykeyboard.release_key('space')
      return True

def fish(oFishingLocation):
  oCenter = pyautogui.center(oFishingLocation+IMG_SIZES['fishing_location'])
  pyautogui.moveTo(oCenter)
  mykeyboard.press_key('f11')
  return oCenter

def find_fishing_location():
  while True:
    oFishingLocation = pyautogui.locateOnScreen('img/fishing_location.png', confidence=0.8)
    if(oFishingLocation):
      return oFishingLocation

if __name__ == '__main__':
  print('press "h" to start fishing')
  keyboard.wait('h')
  main()

