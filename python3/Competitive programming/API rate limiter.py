from datetime import timedelta
import hashlib
import random
import time
from django.core.cache import cache
from django.utils.timezone import now


class SomeClass:
    config = {
        "api_url": "https://some-app.fr/v2/",  # base url of the API
        "rate_limit_hits": 4,  # number of requests allowed per rate_limit_seconds
        "rate_limit_seconds": 1,  # number of seconds to raise the rate_limit_hits
        "timeout": 15,  # number of seconds before timeout
    }

    def __init__(self, api_key):
        self.config["api_key"] = api_key

    def pass_rate_limit(self):
        """Ensure that the rate limit won't be raised"""
        rate_limit_hits = self.config.get("rate_limit_hits", 0)
        rate_limit_seconds = self.config.get("rate_limit_seconds", 0)
        if not rate_limit_seconds or not rate_limit_hits:
            return True
        key = hashlib.md5(
            (self.config["api_url"] + self.config["api_key"][0:8]).encode("utf8")
        ).hexdigest()
        key = f"SomeClass-{key}-hits"
        hits = cache.get(key) or []
        first_relevant_hit_dt = now() - timedelta(seconds=rate_limit_seconds)
        relevant_hits = [dt for dt in hits if dt >= first_relevant_hit_dt]
        if len(relevant_hits) >= rate_limit_hits:
            pause_for = 0
            oldest_relevant_hit = relevant_hits[0]
            free_place_available_at = oldest_relevant_hit + timedelta(seconds=rate_limit_seconds)
            pause_for = free_place_available_at - now()
            if pause_for.seconds <= 0:
                pause_for = pause_for.microseconds / 1000000
            print(f"I am paused for {pause_for:0.4f} at ", now())
            time.sleep(pause_for)
            return self.pass_rate_limit()
        relevant_hits.append(now())
        # because depending the cache used, you can't use 1 seconds or less.
        cache.set(key, relevant_hits, 2 if rate_limit_seconds < 2 else rate_limit_seconds)
        return True

test = SomeClass("osef")

for i in range(0,12):
    print("called at: ", now())
    test.pass_rate_limit()
    print("executed at: ", now())
    time.sleep(random.random() / 4)  # fake API duration process for eg