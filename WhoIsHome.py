# -*- coding: utf-8-*-
import re
import json
import requests

WORDS = ["WHO", "HOME"]

"""
 make sure the following is copied and populated in ~/.jasper/profile.yml
 
 ha_url: 
 ha_port: 
 ha_password: 

"""


def handle(text, mic, profile):

    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

	url = profile['ha_url']+':'+profile['ha_port']+'/api/states'
	
	headers = {'x-ha-access': profile['ha_password'],
	           'content-type': 'application/json'}

    r = requests.get(url, headers=headers)

	j = r.json()
	
	i=1
	ii=1
	at_home=""
	at_work=""
	concat=""
	concat2=""
	
	for entity in j:
		if "device_tracker" in entity['entity_id']:
			if "home" == entity['state']:
				#print entity['attributes']['friendly_name']
				if i==1:
					at_home = entity['attributes']['friendly_name']
					concat = " is "
				elif i>1:
					at_home = at_home + " and " + entity['attributes']['friendly_name']
					concat = " are "
				
				i+= 1
			if "Work" == entity['state']:
				#print entity['attributes']['friendly_name']
				if ii==1:
					at_work = entity['attributes']['friendly_name']
					concat2 = " is "
				elif ii>1:
					at_work = at_work + " and " + entity['attributes']['friendly_name']
					concat2 = " are "
				
				ii+= 1
		
	message = ""		
	if i>1:			
		message = at_home + concat + "at home. "
	if ii>1:
		message = message + at_work + concat2 + "at work. "
		
	if i==1 and ii==1:
		message "There is no one at home"	
    	
    #message = "Home Assistant Activated"

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bhome\b', text, re.IGNORECASE))
