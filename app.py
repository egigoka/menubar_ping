import rumps
import ping_
from commands import *

ping_thread = MyThread(ping_.main)
ping_thread.start()

class MenubarPing(rumps.App):
    def __init__(self):
        super(MenubarPing, self).__init__(name="MenubarPing")

    @rumps.timer(1)
    def update_title(self, sender):
        thread = MyThread(self.set_title)
        thread.start()
    
    def set_title(self):
        #title = f"Country: {ping_.State.country} IP: {ping_.State.public_ip} Ups:"
        title = f"{ping_.State.country}"
        for result in ping_.State.statuses:
            title += "🟢" if result else "💔"
        Print.rewrite()
        print("set title title " + title)
        self.title = title

if __name__ == "__main__":
    print("app started")
    MenubarPing().run()
