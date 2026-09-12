"""Trace minimale d un sous-ensemble RISC-V pour lecture pédagogique."""

def step(state, instruction):
    op, rd, rs1, imm = instruction
    next_state = dict(state)
    if op == "addi": next_state[rd] = state.get(rs1, 0) + imm
    elif op == "add": next_state[rd] = state.get(rs1, 0) + state.get(imm, 0)
    else: raise ValueError("instruction non supportée")
    next_state["pc"] = state.get("pc", 0) + 4
    return next_state

if __name__ == "__main__":
    s=step({"pc":0,"x1":2},("addi","x2","x1",3))
    assert s["x2"] == 5 and s["pc"] == 4
