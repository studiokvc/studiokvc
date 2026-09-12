"""Contrôle d expiration d un ordre Hyperliquid."""

def tradable(order, now):
    return isinstance(order, dict) and order.get("side") in {"buy","sell"} and order.get("size",0) > 0 and order.get("expires_at",0) >= now and bool(order.get("client_id"))

if __name__ == "__main__":
    o={"side":"buy","size":1,"expires_at":100,"client_id":"c1"}
    assert tradable(o,99)
    assert not tradable(o,101)
