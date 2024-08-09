vars: ERC20 t
spec: []!finished(t.transferFrom(from, to, amt),
          amt > old(t.balanceOf(from)) ||
          (from != sender && amt > old(t.allowance(from, sender))))
