from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Analytics server"

@app.route("/collect")
def collect():
    analytics_id = request.args.get("id")
    page = request.args.get("page")

    print("\n=== Analytics event received ===")
    print("Analytics ID:", analytics_id)
    print("Page:", page)
    print("User-Agent:", request.headers.get("User-Agent"))
    print("================================\n")

    response = make_response("OK")
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin")

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9100, debug=True)
    