import json
from celery import Celery
from mysql.connector import connect, Error

rabbitmq_app = Celery('rabbitmq_tasks', backend='rpc://user:bitnami@localhost:5672/', broker='amqp://user:bitnami@localhost:5672/')
# redis_app = Celery('redis_tasks', backend='redis://172.17.0.3:6379/0', broker='redis://172.17.0.3:6379/0')


@rabbitmq_app.task()
def rabbitmq_add(x, y):
    # print('HI')
    # return x + y
    try:
        with open('/Users/shaharlevy/data-general/git-repos/birman_project/config.json') as f:
         data = json.load(f)

        print("hello")
        # print(data)

        with connect(
            host=data["host"],
            user=data["user"],
            password=data["password"],
        ) as connection:
            query = "create database db1"
            with connection.cursor() as cursor:
                cursor.execute(query)

                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)

# @redis_app.task()
# def redis_add(x, y):
#     print('H Redis')
#     return x + y