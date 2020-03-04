from flask import Flask, render_template
apps = Flask(__name__)

@apps.route('/boot')
def boot():
    return render_template('boot.html')

apps.run(debug=True)