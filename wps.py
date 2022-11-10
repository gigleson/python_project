import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed Typing test")
    stdscr.addstr("\n Press any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text ="THe quick brown fox jumped over the lazy brown fox"
    current_text =[]
    
    while True:
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text)>0:
                current_text.pop()
        else:
            current_text.append(key)

      


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_WHITE)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main) 