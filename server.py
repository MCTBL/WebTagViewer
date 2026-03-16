from flask import Flask, render_template, abort
import json
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)


@app.get("/<dataSeries>/<dataName>")
def get(dataSeries: str = "", dataName: str = ""):
    try:
        with open(f"./data/{dataSeries}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if dataName in data:
                return render_template(f"{dataSeries}.html", data=data[dataName]), 200
    except:
        return render_template(f"{dataSeries}.html"), 200


@app.errorhandler(404)
def page_not_found(error):
    return "<div>404 data not found!</div>", 404


if __name__ == "__main__":
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.run(host='0.0.0.0', port=1145, debug=True)
