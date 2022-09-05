from venv import create
from api import create_app; 
import os; 

app=create_app(); 


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
