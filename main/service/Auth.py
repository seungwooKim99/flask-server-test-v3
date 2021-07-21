def login():
  return 'login'

def register():
  return 'register'

def test():
  return_object = {
    'status' : 'success',
    'message' : 'Auth 라우트 테스트 성공'
  }
  return return_object, 201