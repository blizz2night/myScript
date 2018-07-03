var proxy = "SOCKS5 127.0.0.1:1080; SOCKS 127.0.0.1:1080";

var domains = {

  "maven.fabric.io"

};

var direct = "DIRECT";

var hasOwnProperty = Object.hasOwnProperty;

function FindProxyForURL(url, host) {
    if (/(?:^|\.)fabric\.io$/.test(url)) return proxy;
    return direct;
}
