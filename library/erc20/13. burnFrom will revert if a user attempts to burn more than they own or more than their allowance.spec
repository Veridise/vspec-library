vars: ERC20 t
spec: []!finished(t.burnFrom(from, amt),
        old(
          amt > t.balanceOf(from) ||
          (from != sender && amt > t.allowance(from, sender))
        )
      )
