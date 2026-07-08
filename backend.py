import json

from flask import Flask, abort, render_template

app = Flask(__name__)


def get_all_lists():
    with open("data.json", "r") as f:
        return json.load(f)


@app.route("/")
def index():
    all_lists = get_all_lists()
    return render_template("index.html", lists=all_lists)


@app.route("/lists/<list_id>")
def get_single_list(list_id):
    all_lists = get_all_lists()

    selected_list = None
    for list_data in all_lists.values():
        if list_data.get("id") == list_id:
            selected_list = list_data
            print("complete")
            break

    if not selected_list:
        print("Nope")
        abort(404)

    return render_template("list_template.html", current_list=selected_list)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=8080)
