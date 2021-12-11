import os
from glob import glob
from flask import Flask, request
import json

students_json_files = glob(os.path.join('students', '*.json'))

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def main_page():
    return html_list_of_students(students_json_files) + """
    <form method="POST" action="/search">
    <input name="pattern">
    <input type="submit" value="Search">
    </form>
    """


@app.route("/student/<json_file>")
def show_json(json_file):
    with open(f'student/{json_file}', 'r') as reader:
        data = json.load(reader)

    html = f"""
    <h1>Information: {json_file.rstrip(".json")}</h1>
    <p>
    {"<br>".join([f"{key}: {value}" for key, value in data.items() if value is not None])}
    </p>
    """
    return html


@app.route("/search", methods=['POST'])
def list_students_with_pattern():
    pattern = request.form.get('pattern')
    filtered_list = []
    for student_json in students_json_files:
        with open(student_json, 'r') as reader:
            data = reader.read()

        if pattern in data:
            filtered_list.append(student_json)
    return html_list_of_students(filtered_list).replace("Students in the Course:", f'Students with pattern "{pattern}"')


def html_list_of_students(json_files):
    html_script = """
    <h1> Students in the Course:</h1>
    <ul>
    {}
    </ul>
    """.format("".join(
        ["<li><a href=/student/" + student.split('\\')[-1] + ">" + student.split('\\')[-1].rstrip(".json") + "</a></li>" for student in json_files]))
    return html_script


app.run(port="8043", host="0.0.0.0")
