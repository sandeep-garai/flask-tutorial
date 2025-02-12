from flask import Flask, render_template
app= Flask(__name__)

post= [
    {
        'author':'Sandeep Garai',
        'title':'First Tutorial',
        'content': 'blog post 1'
    },
    {
        'author':'S Garai',
        'title':'Second Tutorial',
        'content': 'blog post 2'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template('about.html',title="ABOUt")

if __name__=='__main__':
    app.run(debug=True)