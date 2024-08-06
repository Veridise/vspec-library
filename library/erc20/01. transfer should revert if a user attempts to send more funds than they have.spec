vars: ERC20 t
spec: []!finished(t.transfer(to, amt), amt > old(t.balanceOf(sender)))
