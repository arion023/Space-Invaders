import curses


def count_middle_scr(stdscr):
    my, mx = stdscr.getmaxyx()
    return my//2, mx//2

def set_position(key, pos, len):
    if key == curses.KEY_UP and pos>0:
        return pos-1
    elif key == curses.KEY_DOWN and pos<len-1:
        return pos+1
    else:
        return pos


def menu(stdscr, select):


    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_BLUE, -1)

    position_idx = 0
    
    key = None

    while key!=10:

        midy, midx = count_middle_scr(stdscr)
        
        stdscr.erase()

        for word in select:
            if position_idx == select.index(word):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(midy-len(select)//2+select.index(word), midx-len(word)//2, word)       
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(midy-len(select)//2+select.index(word), midx-len(word)//2, word)       

        stdscr.refresh()

        key = stdscr.getch()
        position_idx = set_position(key, position_idx, len(select))

    stdscr.erase()
    return position_idx

def scoreboard():
    pass

def help():
    pass

def ext():
    pass

def load_options():
    pass

