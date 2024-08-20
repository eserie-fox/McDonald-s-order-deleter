import pyautogui
import time

paths = ['C:\\Users\\dell\\Desktop\\m1.png','C:\\Users\\dell\\Desktop\\m2.png','C:\\Users\\dell\\Desktop\\m3.png','C:\\Users\\dell\\Desktop\\m4.png','C:\\Users\\dell\\Desktop\\m5.png','C:\\Users\\dell\\Desktop\\m6.png','C:\\Users\\dell\\Desktop\\m7.png','C:\\Users\\dell\\Desktop\\m8.png','C:\\Users\\dell\\Desktop\\m9.png','C:\\Users\\dell\\Desktop\\m10.png']
confirmPath = 'C:\\Users\\dell\\Desktop\\confirm.png'
delta=pyautogui.Point(2950,-250)


def clearOrder(pos):
	print('found one: ',pos)
	pyautogui.click(pos+delta)
	time.sleep(1)
	confirmLoc = pyautogui.locateOnScreen(confirmPath)
	pyautogui.click(pyautogui.center(confirmLoc))
	time.sleep(2)

failCnt=0

while True:
	ok=False
	for path in paths:
		try:
			loc = pyautogui.locateOnScreen(path)
			clearOrder(pyautogui.center(loc))
			ok=True
			failCnt=0
		except pyautogui.ImageNotFoundException:
			pass
	if not ok:
		pyautogui.scroll(-500)
		failCnt+=1
		if failCnt > 100:
			break

		