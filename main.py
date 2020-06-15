from server import init_app
from config import Config

if __name__ == "__main__":
    app = init_app(Config)
    app.run(debug=True)
