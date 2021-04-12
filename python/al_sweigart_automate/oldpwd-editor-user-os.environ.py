#!/usr/bin/env python

import os
def gather_env():
    """
    Gather some environment variables
    """
    OLDPWD = os.environ["OLDPWD"]
    EDITOR = os.environ["EDITOR"]
    USER = os.environ["USER"]
    
    return (OLDPWD, EDITOR, USER)
    

OLDPWD, EDITOR, USER = gather_env()

print(f"User {USER} was in diretory {OLDPWD} and uses {EDITOR} as default editor")

