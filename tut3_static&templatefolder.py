from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template('index.html')
# ye index.html file templates folder ke andar jo padi hai use uthayegi or dsiplay kregi via using render_template class


@app.route('/about')
def func2():
    #person naam ke variable me Mudit save krdia.
    #return statement me name jo likha hai yahi same likha hona chahye
    person = 'Mudit'
    return render_template('about.html', name = person)

app.run(debug=True)




