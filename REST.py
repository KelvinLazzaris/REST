from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'riodejaneiro'
jwt = JWTManager(app)

users = {'User1': {'password': 'senha'}}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username, password = data.get('username'), data.get('password')
    if users.get(username):
        return jsonify({'message': 'Usuário já existe!'}), 400
    users[username] = {'password': password}
    return jsonify({'message': 'Registrado!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data.get('username'), data.get('password')
    if not (users.get(username) and users[username]['password'] == password):
        return jsonify({'message': 'Login inválido!'}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_jwt_identity()), 200

if __name__ == '__main__':
    app.run(debug=True)