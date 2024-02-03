import subprocess
import random
import time
from mimesis import Generic, Code
from faker import Faker
from rich import print
from rich.console import Console
import os

os.environ["PYTHONIOENCODING"] = "utf-8"


faker = Faker()

console = Console()

features = []

def flip_coin():
    rand = random.randint(0, 1)
    if rand == 1:
        return True
    else:
        return False

def update_feature_list():
    global features
    path = './Super_Awesome_App'
    command = ['ls', path]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        features = result.stdout.splitlines()
        
def push(commit_msg):
        subprocess.run(['git', 'pull'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-am', commit_msg])
        subprocess.run(['git', 'push'])
    
    
def generate_code(num_lines=5):
    code = Code()
    return code.python_code(num_lines)

def generate_random_unicode_character():
    valid_code_points = [code_point for code_point in range(0x0020, 0xD7FF + 1) if code_point < 0xD800 or code_point > 0xDFFF]
    char = random.choice(valid_code_points)
    return chr(char)

def generate_random_unicode_word(length):
    word = ''
    for _ in range(length):
        word += generate_random_unicode_character()
    return word

def generate_random_ascii_character(include_space=False):
    if include_space:
        return chr(random.randint(32, 126))
    else:
        return chr(random.randint(33, 126))
    
def generate_random_ascii_word(length):
    word = ''
    for _ in range(length):
        word += generate_random_ascii_character()
    return word

def generate_random_sentence(length):
    sentence = ''
    for _ in range(length):
        flip = flip_coin()
        if flip:
            sentence += generate_random_unicode_word(random.randint(1, 12)) + ' '
        else:
            sentence += generate_random_ascii_word(random.randint(1, 12)) + ' '
    return sentence

    
def take_break():
    console.print("""[hot_pink]I'm taking a break.""")
    
def new_feature():
    console.print("""[hot_pink]I'm adding a new feature!""")
    name = 'feature' + str(random.randint(0, 1000000)) + '.py'
    i = 0
    while name in features and i < 10000:
        name = 'feature' + str(random.randint(0, 1000000)) + '.py'
        i += 1 
    command = 'touch ./Super_Awesome_App/' + name
    try:
        subprocess.run(command, shell=True)
        push('Added ' + name)
        update_feature_list()
    except:
        console.print("""[hot_pink]Oh, that didn't work...""")
        
def delete_feature():
    update_feature_list()
    print('What was I thinking?!')
    try:
        feature = random.choice(features)
        command = f'rm ./Super_Awesome_App/{feature}'
        subprocess.run(command, shell=True, check=True)
        update_feature_list()
        console.print(f"""[hot_pink] I deleted {feature}, it was dumb""")
        push(f'Deleted {feature}')
    except subprocess.CalledProcessError as e:
        console.print("""[hot_pink]"Oh, that didn't work...""")
    

    
def update_readme():
    console.print("""[hot_pink]Better update the ReadMe.""")
    roll = random.randint(1, 2000)
    if roll == 666:
        console.print("""[hot_pink]Actually, that ReadMe sucks. I'm going to start over.""")
        subprocess.run('rm ./README.md', shell=True)
        subprocess.run('touch ./README.md', shell=True)
    with open('./README.md', 'a') as f:
        f.write('\n' + faker.sentence())
    push("Updated the ReadMe")
    

def text_with_team():
    console.print("""[hot_pink]I should probably check in with the team.""")
    if flip_coin():
        console.print("""[hot_pink]I'll send them a message.""")
        msg = 'Dev: \n'
        msg_length = random.randint(5, 30)
        msg += generate_random_sentence(msg_length)
        with open('team_chat.txt', 'a') as f:
            f.write(msg + '\n')
    else:
        console.print("""[hot_pink]Oh I have a new message""")
        msg = 'Team: \n'
        msg_length = random.randint(5, 30)
        msg += generate_random_sentence(msg_length)
        with open('team_chat.txt', 'a') as f:
            f.write(msg + '\n')
    push('Team chat')
    
def work_on_novel():
    console.print("""[hot_pink]I think I'll work on my novel.""")
    roll = random.randint(1, 140)
    with open('novel.txt', 'a') as f:
        f.write(generate_random_ascii_character(True))
        if roll == 100:
            f.write('\n')
        
def work():
    roll = random.randint(1, 100)
    if roll <= 10:
        take_break()
    elif roll in range(11, 25):
        new_feature()
    elif roll in range(26, 30):
        update_readme()
    elif roll in range(31, 45):
        delete_feature()
    elif roll in range(46, 60):
        text_with_team()
    elif roll in range(61, 100):
        work_on_novel()
    time.sleep(random.randint(300, 18000))
    work()
    
    
# update_feature_list()
# new_feature()
# update_readme()
# take_break()
# delete_feature()
# text_with_team()
# work_on_novel()
work()