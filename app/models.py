
from flask_sqlalchemy import  SQLAlchemy
from flask import  url_for

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(80))
    description = db.Column(db.Text, nullable=False)
    pages = db.Column(db.Integer, nullable=False)


    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return url_for('static', filename=f"books/images/{self.image}")

    @property
    def show_url(self):
        return url_for('books.show', id=self.id)
    
    @property
    def edit_url(self):
        return url_for ('books.form_edit', id=self.id)

    @property
    def delete_url(self):
        return url_for('books.delete', id=self.id)
    
    

