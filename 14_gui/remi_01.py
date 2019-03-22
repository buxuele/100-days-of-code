# date: 2019/03/22 9:03 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com

"""about:
1. test remi, a gui app tool, light, tiny
   # The entire GUI is converted to HTML and is rendered in your browser.
   # see   http://127.0.0.1:8081/
2. pip3 install remi   # https://github.com/dddomodossola/remi
3. update this app later maybe
"""

import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=500, height=500)
        self.lbl = gui.Label("Hey there")
        self.bt = gui.Button("press me")

        # set listener
        self.bt.onclick.connect(self.on_button_pressed)

        # add widget
        container.append(self.lbl)
        container.append(self.bt)

        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text("Button pressed!")
        self.bt.set_text("You are so pretty!")


start(MyApp)
# start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,
#       enable_file_cache=True, update_interval=0.1, start_browser=True)

# set auth
# start(MyApp, username='myusername', password='mypassword')
