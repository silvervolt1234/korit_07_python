import random

# logo를 text to ascii arts를 검색해 추가해서 로고 출력
logo = r'''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.  
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |  
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |  
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |  
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |  
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |  
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  
'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)

lives = 6
display = []
end_of_game = False

word_list = ["abolish", "contemporary", "absorb", "accommodate", "advise", "acquire", "adequate", "affect", "afford", "aggressive",
    "aid", "alert", "allege", "allowance", "amuse", "analyze", "ancient", "announce", "anxious", "apparent",
    "appeal", "appreciate", "approach", "appropriate", "approve", "argue", "arise", "artificial", "ascend", "assert",
    "assess", "associate", "assume", "attempt", "attend", "attitude", "authority", "avoid", "aware", "benefit",
    "bizarre", "blame", "boost", "boundary", "brave", "breach", "breathe", "broad", "capture", "career",
    "cautious", "celebrate", "challenge", "character", "circumstance", "civil", "claim", "coexist", "collapse", "commit",
    "communicate", "community", "compare", "compete", "complain", "complex", "complicate", "comply", "compose", "comprehend",
    "comprise", "compromise", "conceal", "concentrate", "concept", "concern", "conclude", "concrete", "condemn", "conduct",
    "confer", "confess", "confine", "confirm", "conflict", "conform", "confront", "consecutive", "consequence", "conserve",
    "considerable", "consistent", "constitute", "construct", "consult", "consume", "contact", "contain", "contend", "context",
    "contract", "contradict", "contribute", "controversy", "convention", "convert", "convince", "cooperate", "correspond", "courage",
    "critical", "crucial", "cultivate", "curious", "decline", "decrease", "dedicate", "define", "degrade", "delay",
    "deliberate", "demand", "demonstrate", "deny", "depart", "depend", "depict", "depress", "derive", "descend",
    "describe", "deserve", "designate", "desire", "desperate", "destroy", "determine", "develop", "devise", "devote",
    "diagnose", "differ", "difficult", "diligent", "diminish", "disappear", "disappoint", "discipline", "discover", "discourage",
    "discuss", "disrupt", "distinct", "distinguish", "distort", "diverse", "divide", "domestic", "dominate", "dramatic",
    "durable", "dynamic", "eager", "eccentric", "efficient", "elaborate", "elect", "eliminate", "embrace", "emerge",
    "emphasize", "enable", "encourage", "endorse", "engage", "enhance", "enormous", "entertain", "entire", "environment",
    "erode", "essential", "establish", "evaluate", "evident", "evolve", "exaggerate", "exceed", "excellent", "exception",
    "exhaust", "exhibit", "exist", "expand", "expect", "expensive", "experience", "explain", "explicit", "explore",
    "expose", "express", "extend", "extraordinary", "fabricate", "facilitate", "familiar", "fascinate", "favorable", "feasible",
    "feature", "federal", "feeble", "fierce", "finance", "flexible", "flourish", "fluctuate", "focus", "forbid",
    "forecast", "formulate", "foster", "fragile", "frequent", "fulfill", "fundamental", "furthermore", "generate", "generous"]
chosen_word = random.choice(word_list)
print(chosen_word)
for i in chosen_word:
    display.append('_')
print(display)

while not end_of_game:
    print(stages[lives])
    guess = input('단어 입력 : ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            print(display)
    if '_' not in display:
        print(stages[lives])
        print(' '.join(display))
        print('게임 클리어')
        end_of_game = True
    if guess not in chosen_word:
        lives -= 1
        print(f'{lives} 번 남았습니다')
        print(display)
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print('게임 오버')
            print(f'정답은 {chosen_word}입니다.')
