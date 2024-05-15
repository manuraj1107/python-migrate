from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # Debugging print statements
    print(f'Current user: {current_user}')
    print(f'Current user type: {type(current_user)}')
    print(f'Current user name: {current_user.name if hasattr(current_user, "name") else "No name attribute"}')
    
    return render_template('profile.html', name=current_user.name)
