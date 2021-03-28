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
    answ_list = """
        <select type="select" name ="answer">
            <option>Too big</option>
            <option>Too small</option>
            <option>Correct</option>
        </select>
        <input type="submit" value="Oblicz">
        """


    odp = """
    <p>
    <input type="button" name="big" value="Too big">
    <input type="button" name="small" value="Too small">
    <input type="button" name="hit" value="Correct">

    </p>
    """
    answer = request.args.get('big')
    # to_small = request.args.get('small')
    # correct = request.args.get('hit')
    a = request.args.get('a', 0)
    if a != None:
        a = int(a)
        if a < 1 or a > 1000:
            out_of_range = f"{a} is out of range. Try again."
            return rules + form + out_of_range
        else:
            answer = str(request.args.get("answer"," "))
            show_number = f"<p>Your number is {a}</p>"
            return rules + show_number + answer + answ_list + answer

    else:
        return rules + form + "Podaj liczbę z zakresu"


if __name__ == '__main__':
    app.run()
