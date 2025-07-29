import redis

class RedisClient:
    def __init__(self, host="localhost", port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def get_client(self):
        return self.client
