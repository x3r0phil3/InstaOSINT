import sys
from cv2 import floodFill
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from matplotlib.style import use
from prettytable import PrettyTable
from pystyle import Center, Box
from colorama import init, Fore
from geopy.geocoders import Nominatim
import json
import os
import requests
import ssl
import time
from utilities import cool_print
ssl._create_default_https_context = ssl._create_unverified_context

class InstaOSINT:
    def __init__(self, target , api):
        init()
        self.count = 0
        self.table = PrettyTable()
        self.target = target
        self.config = json.load(open('config.json'))
        self.isprivate = False
        self.api = api
        self.t = PrettyTable()
        self.api.login(config['username'], config['password'])

    def get_addrs(self):
        ## Reinitializing to ensure the table is empty.
        self.t = PrettyTable()
        self.count = 0
        usrid = get_user_id(self.target)
        cool_print(Fore.YELLOW + f"\rCatched {count} address ! \n")
        self.t.field_names = ["ID", "ZIP", "Address", "City"]
        for post in api.user_medias(usrid):
            if 'location' in api.media_info(post.pk):
                self.count = self.count + 1
                cool_print(Fore.YELLOW + f"Catched {count} address !\n")
                self.t.add_row([post.pk, post.location.zip, post.location.address, post.location.city])
        print('\n'*3)
        print(Center.XCenter(Fore.YELLOW + str(self.t)))
        print('\n'*2)
    