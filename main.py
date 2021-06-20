from flask import Flask, url_for
from app import views

# Warning
import warnings

app = Flask(__name__)

# app.add_url_rule('/predict', 'predict', views.predictpage, methods=['POST', 'GET'])

app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/damageapp','damageapp',views.damageapp)
app.add_url_rule('/damageapp/damage','damage',views.damage,methods=['GET','POST'])

if __name__ == "__main__":
	warnings.filterwarnings("ignore", category=DeprecationWarning)
	app.run()