def test_add_patient_to_db():
    from server import add_patient_to_db
    from server import db
    name = "Alana Gonzales"
    id = 100
    blood_type = "O+"
    add_patient_to_db(name, id, blood_type)
    patient_added = db[-1]
    expected = {"name": name, "id": id, "blood_type": blood_type, "test": []}
    assert patient_added == expected
