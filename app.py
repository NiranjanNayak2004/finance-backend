from flask import Flask
from config import Config
from extensions import db, jwt

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.record_routes import record_bp
from routes.dashboard_routes import dashboard_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
@app.route("/")
def home():
    return "Finance Backend is Running "

if __name__ == "__main__":
    app.run(debug=True)