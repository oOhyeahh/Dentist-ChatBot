#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_cors import CORS

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Dental Chatbot'})
    app = app.app
    CORS(app)
    app.run(port=8080,debug=True)


if __name__ == '__main__':
    main()
