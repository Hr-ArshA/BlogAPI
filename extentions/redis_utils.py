import json
from redis import Redis

def add_to_redis(key:str, value:str) -> bool:
    this_redis = Redis(host='redis', port=6379, password='testpass123', decode_responses=True)

    return this_redis.set(f"{key}:{value}", json.dumps(value))


def get_views_online(key):
        this_redis = Redis(host='redis', port=6379, password='testpass123', decode_responses=True)

        keys = [key for key in this_redis.scan_iter(r'{}:*'.format(key))]
        views = len(keys)
        
        return views