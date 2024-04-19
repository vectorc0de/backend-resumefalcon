import redis


class RedisWrapper:
    def task_status(self, id_task, id_user):
        return True

    def save_summary(self, content, user_id, task_id):
        return True

    def get_summary(self, content, user_id, task_id):
        return True

    def save_achievements(self, content, user_id, task_id):
        return True

    def save_other(self, content, user_id, task_id):
        return True

    def save_education(self, content, user_id, task_id):
        return True

    def save_personal_projects(self, content, user_id, task_id):
        return True

    def save_sended(self, content, user_id, task_id):
        return True

    def save_employment(self, content, user_id, task_id):
        return True

    def save_user_data(self, content, user_id, task_id):
        return True

    def connect_server(self, hst, prt):
        r = redis.Redis(host=hst, port=prt, decode_responses=True)
        return r