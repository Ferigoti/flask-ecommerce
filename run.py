from app import create_app

# Chama a factory para criar a instância da aplicação
application = create_app()

# Executa a aplicação
if __name__ == '__main__':
    application.run(debug=True)