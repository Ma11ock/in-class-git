#!/usr/bin/env python

import string
import random

# Generates a password from a length given by a user
letters = string.ascii_letters
print(''.join(random.choice(letters) for i in range(int(input("How long should the password be? ")))))


