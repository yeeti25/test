# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:20:55 2019

@author: demopc
"""

import requests

response=requests.get('https://www.google.com')

print(response.status_code)
