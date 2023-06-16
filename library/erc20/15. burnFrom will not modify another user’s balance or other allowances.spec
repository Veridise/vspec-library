vars: ERC20 t, address o1, address o2, address o3
inv:  finished(t.burnFrom(from, amt),
  o1 != from && o2 != sender |=>
    t.balanceOf(o1) = old(t.balanceOf(o1)) &&
    t.allowance(from, o2) = old(t.allowance(from, o2)) &&
    t.allowance(o1, o3) = old(t.allowance(o1, o3))
)
