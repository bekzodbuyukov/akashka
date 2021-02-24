import pygame
import engine
from tkinter import *


# STATIC VARIABLES
ICONS_50_ROOT = 'media/icons/50/{}.png'
ICONS_100_ROOT = 'media/icons/100/{}.png'


# video_url = str(input('Video URL: '))
video_url = 'https://www.youtube.com/watch?v=1VAjZRnJIRk'
player = engine.Engine(video_url=video_url)


# setting root
root = Tk()
root.title('akashka')
root.geometry('550x100')


# Initialize Pygame Mixer
pygame.mixer.init()


# Making Control Bar
control_bar = Frame(root)
control_bar.pack(pady=20)


# Control Buttons' Images
previous_image = PhotoImage(file=ICONS_50_ROOT.format('previous'))
next_image = PhotoImage(file=ICONS_50_ROOT.format('next'))
play_image = PhotoImage(file=ICONS_50_ROOT.format('play'))
pause_image = PhotoImage(file=ICONS_50_ROOT.format('pause'))
replay_image = PhotoImage(file=ICONS_50_ROOT.format('replay'))
stop_image = PhotoImage(file=ICONS_50_ROOT.format('stop'))
volume_up_image = PhotoImage(file=ICONS_50_ROOT.format('volume_up'))
volume_down_image = PhotoImage(file=ICONS_50_ROOT.format('volume_down'))


# Control Buttons
previous_button = Button(control_bar, image=previous_image, borderwidth=0)
next_button = Button(control_bar, image=next_image,
                     borderwidth=0, command=player.next)
play_button = Button(control_bar, image=play_image,
                     borderwidth=0, command=player.play)
pause_button = Button(control_bar, image=pause_image,
                      borderwidth=0, command=player.pause)
stop_button = Button(control_bar, image=stop_image,
                     borderwidth=0, command=player.stop)
replay_button = Button(control_bar, image=replay_image,
                       borderwidth=0, command=player.replay)
volume_up_button = Button(control_bar, image=volume_up_image,
                          borderwidth=0, command=player.increase_volume)
volume_down_button = Button(control_bar, image=volume_down_image,
                            borderwidth=0, command=player.decrease_volume)
# fun_video = PhotoImage(file='media/fun/angry_bird.gif',
#                        format='gif -index [index: int]')
# fun_label = Label(image=fun_video)
# fun_button = Button(control_bar, image=fun_video)


# Grid
play_button.grid(row=0, column=0, padx=5)
pause_button.grid(row=0, column=1, padx=5)
stop_button.grid(row=0, column=2, padx=5)
replay_button.grid(row=0, column=3, padx=5)
previous_button.grid(row=0, column=4, padx=5)
next_button.grid(row=0, column=5, padx=5)
volume_up_button.grid(row=0, column=6, padx=5)
volume_down_button.grid(row=0, column=7, padx=5)
# fun_label.pack()


root.mainloop()
