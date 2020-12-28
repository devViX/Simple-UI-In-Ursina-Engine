from ursina import *
app = Ursina()

gold = 0 #global variable
counter = Text(text='0', scale=3, y=.2, x=-.02, color=color.gold)
button = Button(text='+', scale=.125)
button.tooltip = Tooltip('<gold>Add number<white>by clicking')

def button_click():
    global gold
    gold += 1
    counter.text = str(gold)

def update():
    global gold
    if gold >= 10:
        counter.x = -.05
    if gold >= 100:
        counter.x = -.07
        button.disabled = True
        counter.color = color.green
    global value
    if slider.value >= 10:
        slidercounter.x = -.05
    if slider.value >= 100:
        slidercounter.x = -.07
        slidercounter.color = color.green
    else:
        slidercounter.color = color.gold

button.on_click = button_click

#slider = ThinSlider(text=name, min=0, max=100, default=value, x=-.65, y=(-i*.04*.75) - .15, step=1, dynamic=True)
value = 0
slidercounter = Text(text='0', scale=3, color=color.gold, x=-.03, y=-.3)
slider = ThinSlider(text='value', default=value, min=0, max=100, y=-.4, x=-.2, step=1, dynamic=True, scale=1)
slider.tooltip = Tooltip('<gold>Value')


def on_slider_changed(slider=slider):
    slidercounter.text = str(slider.value)



slider.on_value_changed = on_slider_changed
app.run()
