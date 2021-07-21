from flask import request
from flask_restx import Resource, Api, Namespace, fields

api = Namespace(
  name="user",
  description="user 관련 라우트"
)

@api.route('')
class Search(Resource):
  def get(self):
    """User 관련 라우트"""
    return "This is User Route!"