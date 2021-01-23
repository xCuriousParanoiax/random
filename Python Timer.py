from tkinter import *
import sys

# Do: "sudo apt install python3-tk" to install tkinter on linux


class Timer:
	def __init__(self):
		self.pause = False
		self.milliseconds = 1000000000000000

	def timer(self):
		if self.pause == False:
			self.milliseconds += 1
			display['text'] = self.time_calc(self.milliseconds)
		root.after(1, self.start)

	def start(self):
		self.timer()
		StartBtn.config(state=DISABLED)

	def stop(self):
		self.pause = True

	def reset(self):
		self.milliseconds = 0
		display['text'] = self.time_calc(self.milliseconds)

	def _continue(self):
		self.pause = False

	def time_calc(self, milliseconds, seconds=0, minutes=0, hours=0):
		seconds, milliseconds = divmod(milliseconds, 1000)
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}"


if __name__ == "__main__":

	root = Tk()
	root.title("Timer")
	root.wm_attributes("-topmost", 1)
	root.resizable(False, False)

	timer = Timer()

	display = Label(root, width=13, height=2, bg="black", fg="green", font=("Helvetica", 36))
	display.grid(column=1, columnspan=4)

	label = Label(root)
	label.grid(row=0, column=5)

	StartBtn = Button(label, text="Start", command=timer.start)
	StartBtn.grid(row=0, sticky= E + W)

	StopBtn = Button(label, text="Pause", command=timer.stop)
	StopBtn.grid(row=1, sticky= E + W)

	ResetBtn = Button(label, text= "Reset", command=timer.reset)
	ResetBtn.grid(row= 2, sticky= E + W)

	ContinueBtn = Button(label, text="Continue", command=timer._continue)
	ContinueBtn.grid(row=3, sticky= E + W)

	QtBtn = Button(label, text="Quit", command=quit)
	QtBtn.grid(row=4, sticky= E + W)

	root.mainloop()
