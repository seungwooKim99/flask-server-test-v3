from flask import request
from flask_restx import Resource, Api, Namespace, fields
from ..service.Auth import test, login, register

api = Namespace(
  name="auth",
  description="auth 관련 라우트"
)

@api.route('')
class Auth(Resource):
  @api.doc('Test를 위한 상단 라우트')
  def get(self):
    """Auth 관련 라우트"""
    return test()