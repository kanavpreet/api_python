from flask import Flask
import os

app = Flask(__name__)

@app.route("/hello/<string:message>")
def hello(message):
    if message is NONE:
       return "hello strager"
    if message is not NONE:
       return "hello" + message


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
