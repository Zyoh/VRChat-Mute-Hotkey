import keyboard
from pythonosc import udp_client
import argparse


class VRChatMuteHotkey:
	def __init__(self, ip: str = None, sender_port: int = None, hotkey: str = None) -> None:
		if ip is None:
			ip = "127.0.0.1"
		if sender_port is None:
			sender_port = 9000
		if hotkey is None:
			hotkey = "F8"
	
		self.hotkey: str = hotkey
		self.client = udp_client.SimpleUDPClient(ip, sender_port)
		self.is_muted: bool = True

	def toggle_mute(self, *_):
		self.client.send_message("/input/Voice", self.is_muted)
		self.is_muted = not self.is_muted
		
		if self.is_muted:
			print(f"{'Muted':<10}\r", end="")
		else:
			print(f"{'Unmuted':<10}\r", end="")

	def run(self):
		try:
			keyboard.on_release_key(self.hotkey, self.toggle_mute)
			keyboard.wait()
		except KeyboardInterrupt:
			pass


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address of the device running VRChat. Defaults to this device.")
	parser.add_argument("--sender-port", type=int, default=9000, help="Port to send to.")
	parser.add_argument("--hotkey", type=str, default="F8", help="Hotkey to toggle voice with.")
	args = parser.parse_args()

	app = VRChatMuteHotkey(ip=args.ip, sender_port=args.sender_port, hotkey=args.hotkey)
	app.run()

if __name__ == "__main__":
	main()
