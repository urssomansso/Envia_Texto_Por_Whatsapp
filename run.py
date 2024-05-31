from tika import parser
import pyautogui
import pyperclip

raw = parser.from_file(filename="o-senhor-dos-aneis.pdf")

raw = raw["content"].rsplit("\n")
raw = [item for item in raw if item]


pyautogui.sleep(5)

for item in raw:
    pyperclip.copy(item)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "v")
