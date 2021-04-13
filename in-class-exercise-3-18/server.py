from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

db = list()
test_db = list()


def init_server():
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 102, "B-")
    add_test_to_db(5, "HDL", 60)


def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name, "id": id,
                   "blood_type": blood_type, "test": list()}
    db.append(new_patient)
    print(db)
    sys.stdout.flush()
    return True


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()
    # validate input
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    # define new patient dictionary
    add_patient_to_db(in_data["name"],
                      in_data["id"],
                      in_data["blood_type"])
    # return/display results
    print("Patient added")
    sys.stdout.flush()
    return "Patient added", 200


def validate_new_patient_info(in_dict):
    expected_keys = ("name", "id", "blood_type")
    expected_types = (str, int, str)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            print("{} key not found".format(key))
            sys.stdout.flush()
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            print("{} key has the wrong value type".format(key))
            sys.stdout.flush()
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def add_test_to_db(id, test_name, test_result):
    new_test = {"id": id, "test_name": test_name, "test_result": test_result}
    test_db.append(new_test)
    print(test_db)
    sys.stdout.flush()
    return True


@app.route("/add_test", methods=["POST"])
def post_new_test():
    # get input data from requests
    test_data = request.get_json()
    # validate input

    # define new patient dictionary
    add_test_to_db(test_data["id"],
                   test_data["test_name"],
                   test_data["test_result"])
    # return/display results
    print("Test added")
    sys.stdout.flush()
    return "Test added", 200


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_for_id(patient_id):
    for test in test_db:
        if int(test["id"]) == int(patient_id):
            test_type = test["test_name"]
            result = test["test_result"]
    print("For id {}, the test result for {} is {}".format(
                                                           str(patient_id),
                                                           str(test_type),
                                                           str(result)))
    sys.stdout.flush()
    return str(result)


if __name__ == '__main__':
    init_server()
    app.run()
