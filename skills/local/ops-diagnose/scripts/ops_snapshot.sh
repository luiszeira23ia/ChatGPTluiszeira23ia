#!/usr/bin/env bash
set -euo pipefail

service="${1:-}"

echo "== timestamp =="
date -u

echo "\n== uptime/load =="
uptime || true

echo "\n== memory =="
free -h || true

echo "\n== disk =="
df -h || true

echo "\n== top cpu (head) =="
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 12 || true

echo "\n== listening ports =="
ss -tulpn | head -n 40 || true

if [[ -n "$service" ]]; then
  echo "\n== systemd status: $service =="
  systemctl status "$service" --no-pager -n 30 || true

  echo "\n== journalctl: $service (last 50) =="
  journalctl -u "$service" -n 50 --no-pager || true
fi
