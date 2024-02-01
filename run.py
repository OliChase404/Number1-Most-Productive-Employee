import subprocess
import random
import time
from mimesis import Generic, Code

def flip_coin():
    rand = random.randint(0, 1)
    if rand == 1:
        return True
    else:
        return False

def generate_commit_message():
    msg = ''
    
def generate_code(num_lines=5):
    code = Code()
    return code.python_code(num_lines)
    
def take_break():
    print("I'm taking a break!")
    time.sleep(random.randint(5, 30))
    
def new_feature():
    print("I'm adding a new feature!")
    command = 'touch ./Super_Awesome_App/feature' + str(random.randint(0, 1000000)) + '.py'
    try:
        subprocess.run(command, shell=True)
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-am', 'Add new feature'])
        subprocess.run(['git', 'push'])
    except:
        print("Oh, that didn't work...")
    time.sleep(random.randint(5, 30))



# def work():
#     print("I'm working!")
#     if flip_coin():
    
    
new_feature()