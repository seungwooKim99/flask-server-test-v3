from flask import request
from flask_restx import Resource, Api, Namespace, fields
from ..service.Search import test

api = Namespace(
  name="search",
  description="search 관련 라우트"
)

@api.route('')
class Search(Resource):
  def get(self):
    """Search 관련 라우트"""
    return test()