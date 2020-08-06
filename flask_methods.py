from flask import Flask,request,jsonify
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["DEBUG"]=True

create_url= "postgresql://postgres:sarneesh@localhost:5432/Library"
db=create_engine(create_url)

@app.route('/')
def Home_page():
    return "Welcome to Books World!"

@app.route('/library',methods = ['GET'])
def get_list_books():
    book= db.execute("select * from book_world.book_details")
    result=[dict (i) for i in book]
    return jsonify(result)


@app.route('/add_books',methods = ['GET','POST'])
def add_books():
    if request.method=="POST":
        book_name=request.form['book_name']
        book_price=request.form['book_price']
        book_author=request.form['book_author']
        author_age=request.form['author_age']
        author_nationality=request.form['author_nationality']
        new_book=db.execute ("INSERT INTO book_world.book_details(book_name,book_price,book_author,author_age,author_nationality)VALUES(%s,%s,%s,%s,%s)".format(book_name,book_price,book_author,author_age,author_nationality))
        db.session.add(new_book)
        db.commit()
        return 'book add successfully'

app.run()