from flask import Flask, render_template, request
from markdown2 import markdown
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def home():
    start_time = time.time()
    name = request.form.get('Name')
    title = request.form.get('Title')
    theme = request.form.get('Theme')
    para = request.form.get('para')

    if theme == "Dark" or theme == "dark":
        css = "<link rel='stylesheet' href ='https://bootswatch.com/4/darkly/bootstrap.min.css'>"
    else:
        css = "<link rel='stylesheet' href ='https://bootswatch.com/4/flatly/bootstrap.min.css'>"
    template = '''
         <!DOCTYPE html>
         <html>
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>'''+title+'''</title>
                        '''+css+'''
                </head>
                <body>'''

    nav = '''
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <a class="navbar-brand" href="#">'''+name+'''</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarColor01">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home
                    <span class="sr-only">(current)</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Dropdown</a>
                    <div class="dropdown-menu">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <a class="dropdown-item" href="#">Something else here</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Separated link</a>
                    </div>
                </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="text" placeholder="Search">
                <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
        </nav>'''
    end = nav + "<br><div class='container'>"+markdown('#'+name) + "<div class='jumbotron'>"+markdown(para)+'''</div>
            </div></body></html>'''
    with open("static/gen.html", "w") as file:
        file.write(template+end)
    print("done")
    tim = time.time() - start_time
    return render_template('download.html', tim=tim)


if __name__ == "__main__":
    app.run(debug=True)
