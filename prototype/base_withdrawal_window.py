"""Fenêtre temporelle pédagogique pour un retrait Base."""

def eligible(request, now, challenge_period):
    required = {"id", "created_at", "amount", "status"}
    return isinstance(request, dict) and required <= request.keys() and request["amount"] > 0 and request["status"] == "finalized" and now >= request["created_at"] + challenge_period

if __name__ == "__main__":
    r={"id":"w1","created_at":100,"amount":2,"status":"finalized"}
    assert eligible(r,200,50)
    assert not eligible(r,120,50)
