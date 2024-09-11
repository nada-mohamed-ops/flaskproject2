from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from app.books import  book_blueprint
from app.models import Book, db
from app.books.forms import bookForm
import  os


@book_blueprint.route('', endpoint='index')
def index():
    books = Book.query.all()
    return render_template("books/index.html", books=books)


@book_blueprint.route("/<int:id>",  endpoint="show")
def show(id):
    book = db.get_or_404(Book, id)
    return render_template("books/show.html", book=book)

@book_blueprint.route("/form/create", endpoint="form_create", methods=["POST", "GET"])
def create_book():
    form  = bookForm()
    if request.method=='POST':
        if form.validate_on_submit():
            image_name=None
            if request.files.get('image'):
                image= form.image.data
                image_name =secure_filename(image.filename)
                image.save(os.path.join('app/static/books/images/', image_name))
            book = Book(title=request.form['title'],image=image_name,pages=request.form['pages'],description=request.form['description'])
            db.session.add(book)
            db.session.commit()
            return redirect(book.show_url)

    return  render_template("books/create.html", form=form)


@book_blueprint.route("/form/update/<int:id>", endpoint="form_edit", methods=["POST", "GET"])
def edit(id):
    book = db.get_or_404(Book, id)
    form  = bookForm(obj=book)
    if request.method=='POST':
        if form.validate_on_submit():
            book.title = form.title.data
            book.pages = form.pages.data
            book.description = form.description.data
            if request.files.get('image'):
                image= form.image.data
                image_name =secure_filename(image.filename)
                image.save(os.path.join('app/static/books/images/', image_name))
                book.image = image_name
            db.session.commit()
            return redirect(book.show_url)

    return  render_template("books/edit.html", form=form , book=book)


@book_blueprint.route("/<int:id>/delete", endpoint="delete", methods=["POST"])
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return  redirect(url_for("books.index"))








