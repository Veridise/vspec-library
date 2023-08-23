vars: ERC20 t
inv:  reverted(t.transfer(to, amt), amt > t.balanceOf(sender))
