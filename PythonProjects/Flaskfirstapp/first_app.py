from flask import Flask, render_template
app = Flask(__name__)

posts = [

    {
        'author': 'Dawid Roszman',
        'title':'Blog post 1',
        'content':'First post content',
        'date posted': '6.08.2020'
            },
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='title')

if __name__=='__main__':
    app.run(debug=True)