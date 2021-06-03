import pyautogui as pa
print(pa.size())#screen size
print(pa.position()) # current position of cursor
#pa.moveTo(10,10,duration=1.5) #Move cursor at particular co ordinate
#pa.moveRel(200,0,duration=2) #Move cursor relative
pa.click(708,33) # single click on those coordinate
#Doubleclick(),middileClick()