import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/flaskdynamodb')

import hello

def test_h2():
    assert hello.h2()  == 1