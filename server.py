from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])    # decorator related to variable app, defining a route that will go with the server
def server_status():
    return "The server is on."


@app.route("/info", methods=["GET"])
def information():
    output = "This server will allow the user to request blood analyses"
    print("hello")
    return output


@app.route("/HDL", methods=["POST"])
def HDL_request():
    """
        input info: {"HDL": 60}
    """
    from blood_tests import check_HDL
    in_data = request.get_json()
    print(in_data)
    HDL = in_data["HDL"]
    result = check_HDL(HDL)
    answer = {"HDL": HDL, "Analysis": result}
    if answer != "Normal":
        return "Bad HDL", 400
    return jsonify(answer)
    # return "The result for a blood level of {} is {}.".format(HDL, result)


@app.route("/say_hello/<person>/<age>", methods=["GET"])  # variable URL
def say_hello_function(person, age):
    next_year = int(age) + 1
    output = "Hello there, {}! You will be {} years old next year".format(person, next_year)
    return output


if __name__ == '__main__':
    print("here")
    app.run()
