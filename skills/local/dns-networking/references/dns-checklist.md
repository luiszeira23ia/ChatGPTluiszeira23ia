# DNS Checklist

1. Resolve using system resolver.
2. Resolve using public resolver (1.1.1.1 / 8.8.8.8).
3. Compare A/AAAA/CNAME outputs and TTL behavior.
4. Verify NS delegation and SOA for authority issues.
5. Check propagation and stale-cache possibility.
6. Confirm app uses expected resolver/network namespace.
