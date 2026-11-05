"""Tiny stdlib HTTP client with per-host rate limiting and retries."""
import json
import time
import urllib.error
import urllib.request

USER_AGENT = "trenchlab/0.1 (read-only research scanner)"

_last_call: dict = {}


class HttpError(Exception):
    pass


def get_json(url, min_interval=0.0, retries=3, timeout=20, headers=None):
    """GET a URL and parse JSON. Waits so calls to the same host are at least
    `min_interval` seconds apart. Retries on 429/5xx/network errors."""
    host = url.split("/")[2]
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)

    last_err = None
    for attempt in range(retries + 1):
        wait = _last_call.get(host, 0) + min_interval - time.time()
        if wait > 0:
            time.sleep(wait)
        _last_call[host] = time.time()
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code} for {url}"
            if e.code == 429 or e.code >= 500:
                time.sleep(min(60, 5 * (attempt + 1)))
                continue
            if e.code == 404:
                return None
            raise HttpError(last_err)
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            last_err = f"{type(e).__name__}: {e} for {url}"
            time.sleep(3 * (attempt + 1))
    raise HttpError(last_err or f"failed: {url}")


def post_json(url, payload, timeout=15):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"User-Agent": USER_AGENT, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))
