from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")
    # Information about the request and network connection
    print("IP address :", request.remote_addr)
    print("HTTP method :", request.method)
    
    # Examples of passive HTTP features
    print("User-Agent :", request.headers.get("User-Agent"))
    print("Accept-Language :", request.headers.get("Accept-Language"))
    # TODO: Add the other passive features identified in Task 0.
    # Example:
    # print("Feature name :", request.headers.get("Header-Name"))
    print("Referer :", request.headers.get("Referer"))
    print("Accept-Encoding  :", request.headers.get("Accept-Encoding"))
    print("Origin  :", request.headers.get("Origin"))
    print("Cookies   :", request.cookies)
    print("Sec-CH-UA : ", request.headers.get("Sec-CH-UA")) #browser brand 

    print("================================\n")
    return render_template("index.html")

@app.route("/typing-results", methods=["POST"])
def typing_results():
    data = request.get_json()

    print("\n========== TYPING RESULTS ==========")
    print("Typing time :", data["typing_time"], "seconds")
    print("Typing speed:", data["typing_speed"], "words/minute")
    print("Corrections :", data["corrections"])
    print("====================================\n")

    return {"status": "received"} 

@app.route("/fingerprint-hash", methods=["POST"])
def fingerprint_hash():

    data = request.get_json()

    fingerprint = data.get("fingerprint")

    print("\n========== BROWSER FINGERPRINT ==========")
    print("SHA-256:", fingerprint)
    print("=========================================\n")

    return {"status": "received"}

@app.route("/fingerprint", methods=["POST"])
def fingerprint():
    data = request.get_json()

    print("\n========== BROWSER FINGERPRINT ==========")

    for feature, value in data.items():
        print(f"{feature}: {value}")

    print("=========================================\n")

    return {"status": "received"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1000, debug=True)
