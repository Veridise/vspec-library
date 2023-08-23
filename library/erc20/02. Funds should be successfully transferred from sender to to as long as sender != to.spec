vars: ERC20 t
inv:  finished(t.transfer(to, amt),
  to != sender |=>
    t.balanceOf(sender) = old(t.balanceOf(sender)) - amt &&
    t.balanceOf(to) = old(t.balanceOf(to)) + amt
)
