'''
Easy and quick toggle to silence all print functions
'''
DEBUG = not True

def debug_print(s):
    if DEBUG:
        print(s)