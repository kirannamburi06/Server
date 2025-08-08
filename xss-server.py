from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = {
        "time": now,
        "ip": request.remote_addr,
        "method": request.method,
        "path": path,
        "query": request.args.to_dict(),
        "headers": dict(request.headers),
        "body": request.get_data(as_text=True)
    }
    print("\n[HIT] ----------------")
    print(log_data)
    with open("hits.log", "a") as f:
        f.write(str(log_data) + "\n")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
