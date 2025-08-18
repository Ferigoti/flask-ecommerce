import os
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
from .models import db, User

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o LoginManager
login_manager = LoginManager()

def create_app():
    """Cria e configura a instância da aplicação Flask."""
    application = Flask(__name__)

    # Configurações da aplicação
    application.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "minha_chave_123")
    application.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa as extensões com a aplicação
    CORS(application)
    db.init_app(application)
    login_manager.init_app(application)

    # Configura o user_loader do Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp
    from .routes.cart_routes import cart_bp

    application.register_blueprint(auth_bp)
    application.register_blueprint(product_bp, url_prefix='/api/products')
    application.register_blueprint(cart_bp, url_prefix='/api/cart')

    with application.app_context():
        db.create_all()
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(username='admin', password='123')
            db.session.add(admin_user)
            db.session.commit()
        print("Banco de dados conectado e usuário admin verificado!")

    return application