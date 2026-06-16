from database.DB_connect import DBConnect
from model.team import Team


class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_year():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year
                    from team 
                    where year>= 1980 """

        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_squadre_salario(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.id, t.team_code, t.name, sum(s.salary) as tot_salari
                    from team t, salary s
                    where t.year = %s and s.`year` = %s and
                          t.id = s.team_id
                    group by t.id, t.team_code, t.name  """

        cursor.execute(query, (anno, anno, ))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

