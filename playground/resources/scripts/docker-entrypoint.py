import os
import sys
from subprocess import call
from urllib.parse import quote, unquote

NGINX_FILE = "/etc/nginx/nginx.conf"

# Replace base url placeholders with actual base url -> should
decoded_base_url = unquote(os.getenv("BASE_URL", "").rstrip("/"))
call(
    "sed -i 's@{BASE_URL_DECODED}@" + decoded_base_url + "@g' " + NGINX_FILE,
    shell=True,
)
# Set url escaped url
encoded_base_url = quote(decoded_base_url, safe="/%")
call(
    "sed -i 's@{BASE_URL_ENCODED}@" + encoded_base_url + "@g' " + NGINX_FILE,
    shell=True,
)

# Set up playground app analytics
RESOURCES_PATH = os.getenv("RESOURCES_PATH", "/resources")
ACTIVATE_ANALYTICS_SCRIPT = os.path.join(
    RESOURCES_PATH, "scripts", "activate-analytics.py"
)
call(f"{sys.executable} {ACTIVATE_ANALYTICS_SCRIPT}", shell=True)

# Run supervisor
call("supervisord -n -c /etc/supervisor/supervisord.conf", shell=True)
