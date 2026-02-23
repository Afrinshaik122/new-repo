from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '''
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Hello Rajesh</title>
      </head>
      <body>
        <h1>Hello Rajesh - Running in GitHub Actions CI</h1>
      </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
