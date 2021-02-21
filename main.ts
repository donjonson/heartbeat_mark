input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    bpressed = 1
    while (bpressed) {
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(100)
        basic.showIcon(IconNames.Heart)
        basic.pause(200)
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    bpressed = 0
    basic.showIcon(IconNames.Sad)
})
let bpressed = 0
basic.showIcon(IconNames.Happy)
bpressed = 1
