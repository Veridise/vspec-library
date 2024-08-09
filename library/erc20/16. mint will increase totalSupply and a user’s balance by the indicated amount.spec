vars: ERC20 t
inv:  t.balanceOf(acc) = old(t.balanceOf(acc)) + amt &&
      t.totalSupply() = old(t.totalSupply()) + amt
      over t.mint(acc, amt)
