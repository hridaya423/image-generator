from flask import Flask, render_template, request
from backend import project
from flask_bootstrap import Bootstrap5  

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, widgets
from wtforms.validators import InputRequired, Length
import secrets

app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)

csrf = CSRFProtect(app)

csrf.init_app(app)



class TextForm(FlaskForm):
    name = StringField('Prompt', validators=[InputRequired(message=None), Length(10, 100)])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    message = ""
    if form.validate_on_submit():
        message = form.name.data
        
    return render_template('index.html', form=form, message=message)

@app.route('/results', methods=['POST'])
def results():
    prompt = request.form['name']
    dalle_model = project.models.create(
        name='dalle_model',
        engine='openai_engine', # alternatively: engine=server.ml_engines.openai
        predict='img_url',
        options={
            'prompt_template':'{{text}}, 8K | highly detailed realistic 3d oil painting style cyberpunk by MAD DOG JONES combined with Van Gogh | cinematic lighting | happy colors',
            'mode':'image'
        }
    )   
    image = dalle_model.predict({ 'text': prompt })
    print(image)
    return render_template('image.html', image=image)



if __name__ == '__main__':
    app.run(debug=True)
    