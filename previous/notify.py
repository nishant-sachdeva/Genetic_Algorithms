import subprocess 


def send_notification(heading):
	subprocess.Popen(['notify-send'  , heading])