from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'God is a good God. All through my life,i have realized that he is a fiathful God'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

