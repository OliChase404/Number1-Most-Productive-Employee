import subprocess
import random
import time
from mimesis import Generic, Code
from faker import Faker

faker = Faker()

features = []

def flip_coin():
    rand = random.randint(0, 1)
    if rand == 1:
        return True
    else:
        return False

def update_feature_list():
    path = './Super_Awesome_App'
    command = ['ls', path]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        features = result.stdout.splitlines()
        # print(features)
        
def push(commit_msg):
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-am', commit_msg])
        subprocess.run(['git', 'push'])
    
    
def generate_code(num_lines=5):
    code = Code()
    return code.python_code(num_lines)
    
def take_break():
    print("I'm taking a break!")
    
def new_feature():
    print("I'm adding a new feature!")
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
        print("Oh, that didn't work...")
        
def delete_feature():
    print('What was I thinking?!')
    update_feature_list()
    feature = random.choice(features)
    command = 'rm ./Super_Awesome_App/' + feature
    print('I deleted ' + feature + 'it was dumb')
    

    
def update_readme():
    print("Better update the README!")
    flip = flip_coin()
    if flip:
        with open('./README.md', 'a') as f:
            f.write('\n\n' + faker.sentence())
    push("Updated the ReadMe")



def work():
    time.sleep(random.randint(5, 30))
    
    
# update_feature_list()
# new_feature()
update_readme()