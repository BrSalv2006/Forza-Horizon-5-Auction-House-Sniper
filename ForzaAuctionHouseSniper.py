import time, pyautogui
from threading import Thread
from tkinter import Label
import tkinter as tk
from win32 import win32gui, win32api
from mss import mss

def getpixelcolor(x,y):
	with mss() as sct:
		sct_img = sct.grab({"mon":1, "top":y, "left":x, "width":1, "height":1})
		color = sct_img.pixel(0,0)
		return(color)

def auctionhousesniping():
	def enterauctionhouse():
		consoleoutput.set("Entering Search")
		auctionsearch = getpixelcolor(auctionsearchx, auctionsearchy)
		while auctionsearch != (255,0,134):
			auctionsearch = getpixelcolor(auctionsearchx, auctionsearchy)
		pyautogui.press("enter")
		consoleoutput.set("Entering Auction House")
		searchloading = getpixelcolor(searchloadingx, searchloadingy)
		while searchloading != (247,247,247):
			searchloading = getpixelcolor(searchloadingx, searchloadingy)
		searchconfirm = getpixelcolor(searchconfirmx, searchconfirmy)
		while searchconfirm != (255,0,134):
			searchconfirm = getpixelcolor(searchconfirmx, searchconfirmy)
		pyautogui.press("enter")
		checkforauction()

	def checkforauction():
		consoleoutput.set("Checking for an auction")
		auctionloading = getpixelcolor(auctionloadingx, auctionloadingy)
		while auctionloading != (255,222,57):
			auctionloading = getpixelcolor(auctionloadingx, auctionloadingy)
		auctionavailable = getpixelcolor(auctionavailablex, auctionavailabley)
		if auctionavailable == (52,23,53):
			auctionsloading = getpixelcolor(auctionsloadingx, auctionsloadingy)
			consoleoutput.set("Waiting for auctions to load")
			while auctionsloading == (247,247,247):
				auctionsloading = getpixelcolor(auctionsloadingx, auctionsloadingy)
			attemptbuyout()
		else:
			returntostart()

	def attemptbuyout():
		consoleoutput.set("Opening shortcut menu")
		pyautogui.press("y")
		auctionoptions = getpixelcolor(auctionoptionsx, auctionoptionsy)
		auctionoptions1 = getpixelcolor(auctionoptions1x, auctionoptions1y)
		while auctionoptions != (52, 23, 53) and auctionoptions1 != (52, 23, 53):
			auctionoptions = getpixelcolor(auctionoptionsx, auctionoptionsy)
			auctionoptions1 = getpixelcolor(auctionoptions1x, auctionoptions1y)
		if auctionoptions == (52, 23, 53):
			x,y = buyoutoption2x, buyoutoption2y
		elif auctionoptions1 == (52, 23, 53):
			x,y = buyoutoptionx, buyoutoptiony
		buyoutoption = getpixelcolor(x, y)
		while buyoutoption != (255,0,134):
			pyautogui.press("down")
			buyoutoption = getpixelcolor(x, y)
		pyautogui.press("enter")
		buyoutconfirm = getpixelcolor(buyoutconfirmx, buyoutconfirmy)
		while buyoutconfirm != (255,0,134):
			buyoutconfirm = getpixelcolor(buyoutconfirmx, buyoutconfirmy)
		pyautogui.press("enter")
		buyoutoutcome()

	def buyoutoutcome():
		consoleoutput.set("Waiting for Buyout Outcome")
		time.sleep(.5)
		buyoutoutcomewait = getpixelcolor(buyoutoutcomex, buyoutoutcomey)
		while buyoutoutcomewait != (52,23,53):
			buyoutoutcomewait = getpixelcolor(buyoutoutcomex, buyoutoutcomey)
		buyoutoutcomewait = getpixelcolor(buyoutoutcomex, buyoutoutcomey)
		while buyoutoutcomewait == (52,23,53):
			buyoutoutcomewait = getpixelcolor(buyoutoutcomex, buyoutoutcomey)
		buyoutoutcomecheck = getpixelcolor(buyoutoutcomecheckx, buyoutoutcomechecky)
		while buyoutoutcomecheck != (52,23,53):
			buyoutoutcomecheck = getpixelcolor(buyoutoutcomecheckx, buyoutoutcomechecky)	
		buyoutsuccessful = getpixelcolor(buyoutsucessfullx, buyoutsucessfully)
		if buyoutsuccessful == (52,23,53):
			buyoutoutcomesuccessfull()
		else:
			buyoutoutcomefailed()

	def buyoutoutcomesuccessfull():
		pyautogui.press("enter")
		collectcar = getpixelcolor(collectcarx, collectcary)
		collectcar1 = getpixelcolor(collectcar1x, collectcar1y)
		collectcar2 = getpixelcolor(collectcar2x, collectcar2y)
		while collectcar != (255,0,134) and collectcar1 != (255,0,134) and collectcar2 != (255,0,134):
			consoleoutput.set("Collect car not selected")
			collectcar = getpixelcolor(collectcarx, collectcary)
			collectcar1 = getpixelcolor(collectcar1x, collectcar1y)
			collectcar2 = getpixelcolor(collectcar2x, collectcar2y)	
		consoleoutput.set("Collect car selected")
		pyautogui.press("enter")
		consoleoutput.set("Attempting to collect car")
		collectcar = getpixelcolor(collectcarx, collectcary)
		collectcar1 = getpixelcolor(collectcar1x, collectcar1y)
		collectcar2 = getpixelcolor(collectcar2x, collectcar2y)
		while collectcar == (255,0,134) or collectcar1 == (255,0,134) or collectcar2 == (255,0,134):
			collectcar = getpixelcolor(collectcarx, collectcary)
			collectcar1 = getpixelcolor(collectcar1x, collectcar1y)
			collectcar2 = getpixelcolor(collectcar2x, collectcar2y)
			pyautogui.press("enter")
		consoleoutput.set("Waiting for car to be collected")
		carcollected = getpixelcolor(carcollectedx, carcollectedy)
		while carcollected != (52, 23, 53):
			carcollected = getpixelcolor(carcollectedx, carcollectedy)
		consoleoutput.set("Car collected")
		pyautogui.press("enter")
		time.sleep(0.5)
		pyautogui.press("esc")
		returntostart()

	def buyoutoutcomefailed():
		consoleoutput.set("Buyout Failed")
		buyoutfailed = getpixelcolor(buyoutfailedx, buyoutfailedy)
		while buyoutfailed != (52,23,53):
			buyoutfailed = getpixelcolor(buyoutfailedx, buyoutfailedy)
		pyautogui.press("enter")
		time.sleep(0.5)
		pyautogui.press("esc")
		returntostart()

	def returntostart():
		consoleoutput.set("Returning to start")
		auctionloading = getpixelcolor(auctionloadingx, auctionloadingy)
		while auctionloading != (255,222,57):
			auctionloading = getpixelcolor(auctionloadingx, auctionloadingy)
		pyautogui.press("esc")
		time.sleep(0.75)
		enterauctionhouse()

	while win32gui.GetWindowText(win32gui.GetForegroundWindow()) != "Forza Horizon 5":
		consoleoutput.set("Waiting for Game Window")
	consoleoutput.set("Getting Monitor Info")
	MonitorWidth = win32api.GetSystemMetrics(0)
	MonitorHeight = win32api.GetSystemMetrics(1)
	auctionsearchx = int(0.171875 * MonitorWidth)
	auctionsearchy = int(0.2305555556 * MonitorHeight)
	searchconfirmx = int(0.3171875 * MonitorWidth)
	searchconfirmy = int(0.677777778 * MonitorHeight)
	searchloadingx = int(0.4703125 * MonitorWidth)
	searchloadingy = int(0.52962962963 * MonitorHeight)
	auctionloadingx = int(0.2140625 * MonitorWidth)
	auctionloadingy = int(0.159259259 * MonitorHeight)
	auctionavailablex = int(0.515625 * MonitorWidth)
	auctionavailabley = int(0.213888889 * MonitorHeight)
	auctionsloadingx = int(0.4546875 * MonitorWidth)
	auctionsloadingy = int(0.216666667 * MonitorHeight)
	auctionoptionsx = int(0.32864583333 * MonitorWidth)
	auctionoptionsy = int(0.3537037037 * MonitorHeight)
	auctionoptions1x = int(0.33020833333 * MonitorWidth)
	auctionoptions1y = int(0.41944444444 * MonitorHeight)
	buyoutoptionx = int(0.329166667 * MonitorWidth)
	buyoutoptiony = int(0.492592593 * MonitorHeight)
	buyoutoption2x = int(0.32916666666 * MonitorWidth)
	buyoutoption2y = int(0.47592592592 * MonitorHeight)
	buyoutconfirmx = int(0.3359375 * MonitorWidth)
	buyoutconfirmy = int(0.5638888 * MonitorHeight)
	buyoutoutcomex = int(0.33489583333 * MonitorWidth)
	buyoutoutcomey = int(0.40925925925 * MonitorHeight)
	buyoutoutcomecheckx = int(0.33020833333 * MonitorWidth)
	buyoutoutcomechecky = int(0.47685185185 * MonitorHeight)
	buyoutsucessfullx = int(0.3328125 * MonitorWidth)
	buyoutsucessfully = int(0.42592592592 * MonitorHeight)
	collectcarx = int(0.328645833 * MonitorWidth)
	collectcary = int(0.490740741 * MonitorHeight)
	collectcar1x = int(0.32291666666 * MonitorWidth)
	collectcar1y = int(0.46481481481 * MonitorHeight)
	collectcar2x = int(0.31818181818 * MonitorWidth)
	collectcar2y = int(0.46666666666 * MonitorHeight)
	carcollectedx = int(0.3296875 * MonitorWidth)
	carcollectedy = int(0.47685185185 * MonitorHeight)
	buyoutfailedx = int(0.33020833333 * MonitorWidth)
	buyoutfailedy = int(0.49259259259 * MonitorHeight)
	time.sleep(2)
	consoleoutput.set("Program Running")
	while True:
		enterauctionhouse()

root = tk.Tk()
consoleoutput = tk.StringVar()
consoleoutput.set("")
width, height= pyautogui.size()
root.title("Forza Horizon 5 Auction House Sniper")
root.overrideredirect(1)
root.geometry(("%dx%d" % (width, height)))
root.configure(bg='grey')
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "grey")
ConsoleOutput=Label(textvariable=consoleoutput, fg='#ffffff', bg='grey')
ConsoleOutput.grid(sticky="NE")
Script = Thread(target=auctionhousesniping)
Script.daemon = True
Script.start()
root.mainloop()