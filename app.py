from flask import Flask, render_template
from flask import request
from flask import redirect, session,url_for
import db

app = Flask(__name__)
app.secret_key = "8f364d5978c478dcf57587fd97bd6a8c"


@app.route('/')
def home():

    if not session :
        return render_template('login.html')
    else:
        result = db.get_db()
        print(result)
        return render_template("index.html", parfum=result)


@app.post('/login')
def login():
    password = request.form['password']
    if password == "123":
        session['logged_in'] = True
        return redirect(url_for("home"))
    else:
        return render_template("login.html")





@app.post('/add')
def add():
    n_ref = request.form.get('ref')
    name = request.form.get('name')
    stock = request.form.get('stock')
    genre = request.form.get('genre')
    fournisseur = request.form.get('fournisseur')
    db.create_new_parfume(n_ref, name, fournisseur,genre, stock)
    return redirect(url_for('home'))

@app.post('/delete')
def delete():
    ref = request.form.get('ref')
    db.delete_parfume(ref)
    return redirect(url_for('home'))


@app.post('/change')
def change():
    ref = request.form.get('ref')
    stock = request.form.get('stock')
    db.change(ref, stock)
    return redirect(url_for('home'))


@app.post('/edit')
def edit():
    old_ref = request.form.get('old_ref')
    new_ref = request.form.get('new_ref')
    name = request.form.get('name')
    fournisseur = request.form.get('fournisseur')
    db.update_parfume(old_ref, new_ref, name, fournisseur)
    return redirect(url_for('home'))


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    results = db.search_all_fields(keyword)
    return render_template('index.html', parfum=results)