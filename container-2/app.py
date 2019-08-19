from Person import Person
from flask import Flask, redirect, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    data = Person.getList()
    return render_template('index.html', rows=data)


@app.route('/insert', methods=['POST'])
def insertPage():
    id1 = request.form['ID']
    name = request.form['name']
    age = request.form['age']
    Person(id1, name, age).push()
    return redirect("/")


@app.route('/insert_data')
def insert_data():
    return render_template('add.html')


@app.route('/delete', methods=['POST'])
def deletePage():
    id1 = request.form['selected_option']
    Person.delete(id1)
    return redirect("/")


@app.route('/delete_data')
def delete_data():
    data = Person.getList()
    return render_template('delete.html', action="delete", rows=data)


@app.route('/update', methods=['POST'])
def updateSelectPersonPage():
    id1 = request.form['selected_option']
    if id1 is not None:
        return redirect("/update/details?id=" + id1)


@app.route('/update/person', methods=['POST'])
def updatePerson():
    id1 = request.form['ID']
    name = request.form['name']
    age = request.form['age']
    Person(id1, name, age).update()
    return redirect("/")


@app.route('/update/details', methods=['GET'])
def updatePage():
    id1 = request.args.get('id')
    data = Person.search(id1)
    return render_template('update.html', person=Person(data[0][0], data[0][1], data[0][2]))


@app.route('/update_data')
def update_data():
    data = Person.getList()
    return render_template('delete.html', action="update", rows=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
