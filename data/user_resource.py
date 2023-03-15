from data.users import User
from data import db_session
from flask_restful import abort, reqparse, Resource
from flask import jsonify
import datetime


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"News {user_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('id', required=False, type=int)
parser.add_argument('surname', required=True, type=str)
parser.add_argument('name', required=True, type=str)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True, type=str)
parser.add_argument('speciality', required=True, type=str)
parser.add_argument('address', required=True, type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('password_hash', required=True, type=str)
parser.add_argument('modified_date', required=True, default=datetime.datetime.now())


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        data = db_sess.query(User).get(user_id)
        if not data:
            return jsonify({'error': 'Not found'})
        return jsonify({
            'user': data.to_dict()
        })

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        el = db_sess.query(User).get(user_id)
        if not el:
            return jsonify({'error': 'Bad request'})
        db_sess.delete(el)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        args = parser.parse_args()
        if not args or not all(key in args for key in
                               ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                                'password_hash', 'modified_date', ]):
            return jsonify({'error': 'Bad request'})
        db_sess = db_session.create_session()
        if args['id'] and db_sess.query(User).filter(User.id == user_id).first():
            return jsonify({'error': 'Id already exists'})
        user = db_sess.query(User).filter(User.id == user_id).first()
        user.surname = args['surname'],
        user.name = args['name'],
        user.age = args['age'],
        user.position = args['position'],
        user.speciality = args['speciality'],
        user.address = args['address'],
        user.email = args['email'],
        user.password_hash = args['password_hash'],
        user.modified_date = args['modified_date'],
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        data = db_sess.query(User).all()
        return jsonify({'users': [item.to_dict() for item in data]})

    def post(self):
        args = parser.parse_args()
        if not args or not all(key in args for key in
                               ['id', 'address', 'age', 'email', 'modified_date', 'name', 'position', 'surname',
                                'speciality', 'password_hash']):
            return jsonify({'error': 'Bad request'})
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.id == args['id']).first():
            return jsonify({'error': ' Id already exists'})
        if db_sess.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'Email already exists'})
        user = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            password_hash=args['password_hash'],
            modified_date=args['modified_date'],
        )
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
