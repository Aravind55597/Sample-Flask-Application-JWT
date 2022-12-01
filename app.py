from flask_cors import CORS; 
from flask import Flask; 
from utils.dbConfig import db; 
from routes.routes import api; 
app = Flask(__name__)

# Allow CORS requests to this API-----------------------------------------------------------------------------------------------------------------------------
CORS(app)

# Register your blueprints------------------------------------------------------------------------------------------------------------------------------------
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
