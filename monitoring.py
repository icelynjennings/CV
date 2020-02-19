import time
import logging

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

logger = logging.getLogger('sitemap')


class SiteMapMetricsCollector(object):
    def __init__(self, sitemap):
        self.sitemap = sitemap

    def collect(self):
        size = GaugeMetricFamily('sitemap_size',
                                 'Number of URLs currently in the SiteMap.')
        size.add_metric(["size"], float(len(self.sitemap)))
        yield size

        queue_size = GaugeMetricFamily('sitemap_queue_size',
                                       'Approximate number of URLs currently in the SiteMap queue.')
        queue_size.add_metric(["queue_size"],
                              float(self.sitemap.queue.qsize()))
        yield queue_size

        failed_requests = CounterMetricFamily(
            'failed_requests', 'SiteMap scrapes that returned an error code or exception')
        failed_requests.add_metric(
            ["failed_requests"], float(len(self.sitemap.failed_requests)))
        yield failed_requests


def serve(sitemap, port=8000):
    start_http_server(port)
    REGISTRY.register(SiteMapMetricsCollector(sitemap))
    logger.info(f"Serving metrics at https://localhost:{port} ..........")
    while True:
        time.sleep(1)
