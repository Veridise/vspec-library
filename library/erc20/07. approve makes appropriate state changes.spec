vars: ERC20 t, address o1, address o2, address o3
inv:  finished(t.approve(spender, amt),
  o2 != sender && o1 != spender |=>
    t.allowance(sender, spender) = amt &&
    t.allowance(sender, o1) = old(t.allowance(sender, o1)) &&
    t.allowance(o2, o3) = old(t.allowance(o2, o3)) &&
    t.balanceOf(o3) = old(t.balanceOf(o3)) &&
    t.totalSupply() = old(t.totalSupply())
)
