from app.models.auth.DatabaseFactory import DatabaseFactory

class User():
  def __init__(self, code=0, name="", email="", password=""):
    self.code = code
    self.name = name
    self.email = email
    self.password = password
    self.connection = DatabaseFactory().getConnection()

  def getAllAdmins(self):
    with self.connection.cursor() as cursor:
      sql = "select users.email from users inner join access where access.module=2 and users.code=access.user"

      cursor.execute(sql)
      result = cursor.fetchall()

      if result:
        return result
      else:
        return None

  def updateUser(self, id="", name="", email=""):
    with self.connection.cursor() as cursor:
      sql = "UPDATE users SET users.name=%s, users.email=%s WHERE users.code=%s"

      cursor.execute(sql, (name, email, id))
      self.connection.commit()

      return True

      self.connection.close()


  def updateUserType(self, res, code):
    with self.connection.cursor() as cursor:
      sql = "UPDATE users SET users.isStudent=%s WHERE users.cpf=%s"

      cursor.execute(sql, (int(res), code))
      self.connection.commit()

      return True

      self.connection.close()


  def updateType(self, type, code):
    with self.connection.cursor() as cursor:
      sql = "UPDATE users SET users.studentType=%s WHERE users.cpf=%s"

      cursor.execute(sql, (type, code))
      self.connection.commit()

      return True

      self.connection.close()


  def updatePassword(self, password="", email=""):
    try:
        with self.connection.cursor() as cursor:
          sql = "UPDATE users SET users.password=%s WHERE users.email=%s"

          cursor.execute(sql, (password, email))
          self.connection.commit()

          return True
    finally:
        self.connection.close()

  def getUser(self, id):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT users.*, modules.* FROM access INNER JOIN modules INNER JOIN users WHERE access.user=%s AND users.code=%s AND access.module=modules.code"
        cursor.execute(sql, (id, id))
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def getAllUsers(self):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT users.* FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()



  def getUserByEmail(self, email):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT users.* FROM users WHERE users.email=%s"
        cursor.execute(sql, (email))
        result = cursor.fetchone()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def getUserByCPF(self, cpf):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT users.* FROM users WHERE users.cpf=%s"
        cursor.execute(sql, (cpf))
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()



  def getUserByCNPJ(self, cnpj):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT bussiness.* FROM bussiness WHERE bussiness.cnpj=%s"
        cursor.execute(sql, (cnpj))
        result = cursor.fetchone()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()
