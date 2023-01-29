from flask import Flask, jsonify


app = Flask(__name__)
app.debug = True

@app.route('/hello')
def helloDocker():
    return jsonify({
        'message': 'Just testing Dockerfile with Flask application'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
