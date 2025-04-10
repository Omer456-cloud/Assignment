from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/current-time', methods=['GET'])
def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
