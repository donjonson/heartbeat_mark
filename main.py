def on_button_pressed_a():
    global bpressed
    bpressed = 1
    while bpressed:
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(100)
        basic.show_icon(IconNames.HEART)
        basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bpressed
    bpressed = 0
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

bpressed = 0
basic.show_icon(IconNames.HAPPY)
bpressed = 1