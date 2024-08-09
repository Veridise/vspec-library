vars: ERC20 t
inv:  t.balanceOf(sender) = old(t.balanceOf(sender)) - amt &&
      t.totalSupply() = old(t.totalSupply()) - amt
      over t.burn(amt)

