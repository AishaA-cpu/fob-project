
from pynput.keyboard import Key, Controller

keyboard = Controller()

# def press_tab():
#     keyboard.press("3")

# Highlight devices
# press_tab()
    #keyboard.press(Key.tab)    

# while are not at the top 
    # move to select_device(Up)
    # select device, spacebar
    # take_screen_shot()
    # save the screen_shot()
    # wait x number of minutes()
    # increament counter of devices to keep track of where we are

# while we are not at the bottom
    # select_device(down)
    # take_screen_shot()
    # save the screen_shot()
    # wait x number of minutes
    # increament counter of devices to keep track of wher ewe are
    

# def select_device(key):
#     keyboard.press(Key.space)

def take_screen_shot():
    with keyboard.pressed(Key.shift, Key.cmd):
        keyboard.press('3')
    



# scroll down devices
# loop through and tab number of times till we get to bottom 
# keyboard.press(Key.downarrow)
# Screen shot
# save

# when we get to end, x number of times
# keyboard.press(Key.uparrow)
# Screen shot
# save






















# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()


