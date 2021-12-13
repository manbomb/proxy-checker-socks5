from termcolor import cprint

def green(s) -> str:
    cprint(s, 'green')

def red(s) -> str:
    cprint(s, 'red')

def yellow(s) -> str:
    cprint(s, 'yellow')