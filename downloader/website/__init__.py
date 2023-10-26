from flask import Flask,render_template,request





def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kljkldfinoilfllefuufn'

    


    from .views import views

    app.register_blueprint(views,url_prefix='/')


    app.run(debug=True)