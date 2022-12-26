class guess:
    def __init__(self, word):
        self.guessed = {"error": False}
        self.word = word
        self.max_guesses = 8
        self.guess_count = 0
        self.state = "start"

    def add_guess_count(self):
        self.guess_count += 1
        for i in self.word:
            if i not in self.guessed:
                return
        self.state = "winner"

    def get_guessed_string(self):
        ret = ""
        for w in self.word:
            if w in self.guessed:
                ret += w
            else:
                ret += "_"
        return ret

    def guess(self, input):
        ret = {}
        input_len = len(input)
        if input_len == 1:
            if self.word.find(input) == -1:
                self.add_guess_count()
                return {"message": "CHAR not found in word"}
            else:
                if input in self.guessed:
                    return {"message": "char already selected", "error": True}
                else:
                    self.guessed[input] = 1
                    self.add_guess_count()
                    return {"message": "ok"}
            pass
        elif input_len == len(self.word):
            if input == self.word:
                ## no needed actually
                self.guessed = {a: 1 for a in self.word}
                self.state = "winner"
                return {"message": "winner", "error": False}
            else:
                self.add_guess_count()
        else:
            ret = {"error": True, "message": "Invalid number of chars"}
        return ret
