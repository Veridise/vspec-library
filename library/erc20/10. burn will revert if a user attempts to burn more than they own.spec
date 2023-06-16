vars: ERC20 t
inv:  reverted(t.burn(amt), amt > t.balanceOf(sender))
