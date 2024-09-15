from flask import Flask
from routes.auth_routes import auth_bp
from routes.recommendation_routes import rec_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(rec_bp)


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
