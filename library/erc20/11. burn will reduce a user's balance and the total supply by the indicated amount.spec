vars: ERC20 t
inv:  finished(t.burn(amt),
  t.balanceOf(sender) = old(t.balanceOf(sender)) - amt &&
  t.totalSupply() = old(t.totalSupply()) - amt
)
