import keyboard
from pythonosc import udp_client
import time


class VRChatMuteHotkey:
	def __init__(self, sender_ip: str = None, sender_port: int = None, hotkey: str = None) -> None:
		if sender_ip is None:
			sender_ip = "127.0.0.1"
		if sender_port is None:
			sender_port = 9000
		if hotkey is None:
			hotkey = "F8"
	
		self.hotkey = hotkey
		self.client = udp_client.SimpleUDPClient(sender_ip, sender_port)

	def toggle_mute(self):
		self.client.send_message("/input/Voice", 0)
		time.sleep(0.1)
		self.client.send_message("/input/Voice", 1)

	def run(self):
		try:
			keyboard.add_hotkey(self.hotkey, self.toggle_mute)
			keyboard.wait()
		except KeyboardInterrupt:
			pass


def main():
	app = VRChatMuteHotkey()
	app.run()

if __name__ == "__main__":
	main()
