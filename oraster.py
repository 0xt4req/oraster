#!/usr/bin/env python3
#Author : TareqAhamed

import re
import sys
try:
	import requests
	from termcolor import colored
except ModuleNotFoundError:
	print("""Make sure you have the following module installed!
		\n 1. requests [ pip3 install requests ]
		\n 2. termcolor [ pip3 install termcolor ]""")
	sys.exit()


length = len(sys.argv)

if length != 2:
	print(colored("\nUsages: python3 main.py links.txt", "yellow"))
	sys.exit(0)

try:
	target_file = sys.argv[1]
	with open(target_file) as tfile:
		for link in tfile:

			link = link.strip()
			index = link.index("=")
			final_url = link[:index] + "=http://evil.com"
			exp = re.compile("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)")
			try:
				r = requests.get(final_url)
				domain = exp.match(r.url).group(1)
				if domain == "evil.com":
					print(colored(f"{link} => vulnerable", "red"))
				else:
					print(colored(f"{link} => not vulnerable", "green"))
			except requests.exceptions.ConnectionError:
				print(colored(f"{link} => Host or Service Unknown", "yellow"))
except FileNotFoundError:
	print(colored("\nFile Not found!!", "yellow"))
	sys.exit()
except KeyboardInterrupt:
	print(colored("\nQuitting...", "yellow"))
	sys.exit()
