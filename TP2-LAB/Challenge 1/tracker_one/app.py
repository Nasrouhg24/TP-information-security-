from flask import Flask, render_template,  request, make_response
import secrets


app = Flask(__name__)
@app.route("/")
def home():
    # Check whether the browser already has an identifier
    track_id = request.cookies.get("track_id")
    is_new = track_id is None
    # Generate an identifier only for a new browser
    if is_new:
        track_id = secrets.token_hex(8)
    # Create the normal HTTP response containing index.html
    response = make_response(render_template("tracker.html"))
    
    # Ask the browser to store the identifier
    if is_new:
        response.set_cookie(
                key="track_id",
                value=track_id
            )
    
    publisher = request.args.get("publisher")
    print("Tracker :")
    print("Publisher:", publisher)

    

    return response
if __name__ == "__main__":
    app.run(host="tracker.test",port=3000, debug=True)

