from flask import render_template, Response
from flask import Blueprint, request
from deep_translator import GoogleTranslator
from deep_translator.exceptions import RequestError
import requests

main_rotas = Blueprint('main', __name__)

@main_rotas.route("/", methods=['GET', 'POST'])
def home_page():
    try:
        input_text = request.form.get('text')
        input_option = request.form.get('option')
        if request.method == "POST":
            new_text = GoogleTranslator(source="auto", target=input_option).translate(input_text)
            return render_template('index.html', new_text=new_text, input_text=input_text, input_option=input_option)
        
        return render_template('index.html')
    
    except requests.exceptions.ConnectionError:
        return f"Error ao se conectar, verifique sua internet ou tente mais tarde"
    