vars: ERC20 t, address o1, address o2, address o3, address o4
inv:  (o1 != from && o1 != to && o2 != sender && o3 != from) ==>
      (
        t.balanceOf(o1) = old(t.balanceOf(o1)) &&
        t.allowance(from, o2) = old(t.allowance(from, o2)) &&
        t.allowance(o3, o4) = old(t.allowance(o3, o4)) &&
        t.totalSupply() = old(t.totalSupply())
      )
      over t.transferFrom(from, to, amt)
