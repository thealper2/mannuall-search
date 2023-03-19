import requests
import argparse
import time
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

global username

global WEBSITE

def create_dict(name):
	username = name
	return {
	        'instagram': f'https://www.instagram.com/{username}',
	        'facebook': f'https://www.facebook.com/{username}',
	        'youtube': f'https://www.youtube.com/{username}',
	        'twitter': f'https://twitter.com/{username}',
	        'github': f'https://www.github.com/{username}',
	        'steam': f'https://steamcommunity.com/id/{username}',
	        'medium': f'https://medium.com/@{username}',
	        'google_plus': f'https://plus.google.com/s/{username}/top',
	        'wordpress': f'https://{username}.wordpress.com',
	        'spotify': f'https://open.spotify.com/user/{username}',
	        'canva': f'https://www.canva.com/{username}',
	}


matches = []

def single_search(username="", url="", file_name="", is_out=False, is_list=False):
	WEBSITE = create_dict(username)

	if is_list == True:
		print(f'{Fore.CYAN}List of websites{Fore.RESET}')
		for keys, value in WEBSITE.items():
			print(f'{Fore.CYAN}[*] {keys}{Fore.RESET}')
		exit()

	r = requests.get(WEBSITE[url])

	match=""
	if r.status_code == 200:
		if username in r.text:
			print(f'{Fore.GREEN}[+] {WEBSITE[url]} - {r.status_code} - OK')
			match = WEBSITE[url]
		else:
			print(f'{Fore.BLUE}[?] {WEBSITE[url]} - {r.status_code} - OK{Fore.RESET}')
			match = WEBSITE[url]
	else:
		print(f'{Fore.RED}[-] {WEBSITE[url]} - {r.status_code} - NOTHING{Fore.RESET}')

	if is_out == True:
		with open(file_name, 'a') as f:
			f.write(match + '\n')

def all_search(username="", file_name="", is_out=False):
	WEBSITE = create_dict(username)
	for keys, value in WEBSITE.items():
		if is_out == False:
			single_search(username=username, url=keys)
		else:
			single_search(username=username, url=keys, file_name=file_name, is_out=True)


argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--username', required=False, type=str, help='')
argument_parser.add_argument('--site', required=False, type=str, help='')
argument_parser.add_argument('--all', required=False, action='store_true', help='')
argument_parser.add_argument('--out', required=False, type=str, help='')
argument_parser.add_argument('--list', required=False, action='store_true', help='')
argument = argument_parser.parse_args()

if (argument.username != None and argument.site != None and not argument.all and argument.out == None and not argument.list):
	username = argument.username
	single_search(username=argument.username, url=argument.site)

elif (argument.username != None and argument.site != None and not argument.all and argument.out != None and not argument.list):
	username = argument.username
	single_search(username=argument.username, url=argument.site, file_name=argument.out, is_out=True)

elif (argument.username != None and argument.site == None and argument.all and argument.out == None and not argument.list):
	username = argument.username
	all_search(username=argument.username)

elif (argument.username != None and argument.site == None and argument.all and argument.out != None and not argument.list):
	username = argument.username
	all_search(username=argument.username, file_name=argument.out, is_out=True)

elif (argument.username == None and argument.site == None and not argument.all and argument.out == None and argument.list):
	single_search(is_list=True)
