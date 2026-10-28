"""Serve this archive only on localhost, then open the user's browser."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import webbrowser
from urllib.request import urlopen

root = Path(__file__).resolve().parents[1]

def main():
    # A stable origin keeps browser reading position and settings across launches.
    for port in range(8766, 8776):
        url = f'http://127.0.0.1:{port}/'
        try:
            server = ThreadingHTTPServer(('127.0.0.1', port), partial(SimpleHTTPRequestHandler, directory=str(root)))
            break
        except OSError:
            try:
                with urlopen(url + 'SOURCE_SHA256.txt', timeout=2) as response:
                    matching = response.read() == (root / 'SOURCE_SHA256.txt').read_bytes()
                if matching:
                    print(f'Opening existing archive server: {url}', flush=True)
                    webbrowser.open(url)
                    return
            except (OSError, ValueError):
                pass
    else:
        raise SystemExit('Ports 8766-8775 are occupied. Open index.html directly.')
    print(f'Archive: {url}\nKeep this window open. Ctrl+C stops the server.', flush=True)
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
