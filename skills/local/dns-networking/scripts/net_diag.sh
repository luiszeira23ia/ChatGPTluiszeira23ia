#!/usr/bin/env bash
set -euo pipefail

HOST=""
PORT="443"
RESOLVER=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host) HOST="$2"; shift 2 ;;
    --port) PORT="$2"; shift 2 ;;
    --resolver) RESOLVER="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

if [[ -z "$HOST" ]]; then
  echo "Usage: net_diag.sh --host <domain-or-ip> [--port 443] [--resolver 1.1.1.1]"
  exit 1
fi

echo "== target =="
echo "host=$HOST port=$PORT resolver=${RESOLVER:-system-default}"

echo "\n== DNS lookup =="
if command -v dig >/dev/null 2>&1; then
  if [[ -n "$RESOLVER" ]]; then
    dig +short "@$RESOLVER" "$HOST" A || true
    dig +short "@$RESOLVER" "$HOST" AAAA || true
  else
    dig +short "$HOST" A || true
    dig +short "$HOST" AAAA || true
  fi
else
  echo "dig not found"
fi

echo "\n== getent hosts =="
getent hosts "$HOST" || true

echo "\n== ping (3 packets) =="
ping -c 3 "$HOST" || true

echo "\n== TCP connectivity =="
if command -v nc >/dev/null 2>&1; then
  nc -vz -w 3 "$HOST" "$PORT" || true
else
  echo "nc not found"
fi

echo "\n== TLS handshake summary =="
if command -v openssl >/dev/null 2>&1; then
  echo | openssl s_client -connect "$HOST:$PORT" -servername "$HOST" 2>/dev/null | openssl x509 -noout -subject -issuer -dates || true
else
  echo "openssl not found"
fi
