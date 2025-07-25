"""
Rate limiting implementation for Litecard API requests using leaky bucket algorithm.
"""

from leakybucket import LeakyBucket, AsyncLeakyBucket
from leakybucket.persistence import InMemoryLeakyBucketStorage


# Stay conservative and allow 10 / 1 seconds
storage = InMemoryLeakyBucketStorage(
    max_rate=10,
    time_period=1.0
)

# Global throttler instances
throttler = LeakyBucket(storage)
async_throttler = AsyncLeakyBucket(storage)