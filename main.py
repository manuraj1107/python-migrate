from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XyZas@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    # Debugging print statements
    print(f'Current user: {current_user}')
    print(f'Current user type: {type(current_user)}')
    print(f'Current user name: {current_user.name if hasattr(current_user, "name") else "No name attribute"}')
    
    return render_template('profile.html', name=current_user.name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
