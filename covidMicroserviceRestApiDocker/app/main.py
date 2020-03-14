from connexion.resolver import RestyResolver
from flask_cors import CORS
import connexion

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    cors = CORS(app.app)
    app.add_api('covid.yaml', resolver=RestyResolver('app.api'))
    app.run()
