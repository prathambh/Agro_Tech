from app import create_app
app = create_app()
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a securely generated random string

if __name__ == '__main__':
    app.run(debug = True)
    

    