import curses
import time
import signal
from guess import guess
from words import wordsFromFile, wordsFromWikipediaRandom

word = wordsFromWikipediaRandom()

## alternative - wordsFromFile("resources/words.txt")

game = guess(word.get_word())

screen = curses.initscr()


def losser_winner_screen(message):
    for i in range(40):
        screen.clear()
        screen.addstr(5, i, f"You {message}", curses.A_BOLD)
        screen.refresh()
        time.sleep(0.1)

def draw_game(g, w):

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1)
    while 1:
        curses.use_default_colors()
        screen.clear()
        if g.guess_count >= g.max_guesses:
            losser_winner_screen("are Losser :(")
            g = guess(w.get_word())
        elif g.state == "winner":
            losser_winner_screen("Win, YAY")
            g = guess(w.get_word())
        else:
            screen.addstr(0, 0, f"Guess the word {word.title}", curses.color_pair(5))
            # screen.addstr(2, 0, g.word)

            screen.addstr(
                4, 0, f"Guesses: {g.guess_count } out of {g.max_guesses}"
            )  # Python 3 required for unicode
            screen.addstr(5, 0, g.get_guessed_string())

            screen.addstr(8, 0, "entor char or word to guess")
            s = screen.getstr(8, 30, 25)
            g.guess(s.decode("utf-8"))
            screen.addstr(8, 30, "                             ")
            if g.state == "looser":
                screen.clear()
                screen.refresh()


def handler(signum, frame):
    curses.endwin()
    print("quitting, bye")
    exit(0)


signal.signal(signal.SIGINT, handler)
draw_game(game, word)
curses.endwin()
