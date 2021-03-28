from random import randint
from flask import Flask, request

app = Flask(__name__)

rules = """
    <h3>Rules: Pick one number and I will try to guess it in 10 tries.</h3>
    
    """
@app.route('/')
def guess_number():
    min_num, max_num = 1, 1000
    answer = 0
    tried = 1
    form = """
    <p>
    <form>
        <p>Input your number in range 1-1000:<br><input type='number' name='a'></p>
        <p><input type='submit'></p>
    </form>
    </p>
    """
    too_big = """
    
    """
    too_small = """
    
    """

    a = request.args.get('a', 0)
    if a != None:
        a = int(a)
        if a < 1 or a > 1000:
            out_of_range = f"{a} is out of range. Try again."
            return rules + form + out_of_range
        else:
            answer = a
            while tried < 10:



                return rules + str(a)

    else:
        return rules + form + "Podaj liczbę z zakresu"


if __name__ == '__main__':
    app.run()
