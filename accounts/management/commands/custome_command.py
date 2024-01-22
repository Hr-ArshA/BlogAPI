from django.core.management.base import BaseCommand
from redis import Redis
import json
from blog.models import Post, PostViews
from accounts.models import IPAddress


class Command(BaseCommand):
    help = 'Transfers all the IPs stored in the Redis memory to the main database'

    def handle(self, *args, **options):
        this_redis = Redis(host='redis', port=6379, password='testpass123', decode_responses=True)
        ips = set()
        all_seen = this_redis.lrange('new_seen', 0, -1)
        for i in all_seen:
            this = this_redis.rpop('new_seen')
            print(this, type(this))
            ips.add((json.loads(this)['slug'], json.loads(this)['ip']))

        for instance in ips:
            ip = IPAddress.objects.create(ip_address=instance[1])
            queryset = Post.objects.get(slug=instance[0])
            PostViews.objects.create(article=queryset, ip_address=ip).save()
            ip.save()