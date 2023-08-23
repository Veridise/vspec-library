vars: ERC20 t
inv:  finished(t.mint(acc, amt),
  t.balanceOf(acc) = old(t.balanceOf(acc)) + amt &&
  t.totalSupply() = old(t.totalSupply()) + amt
)
