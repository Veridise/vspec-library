vars: ERC20 t, address o1, address o2, address o3
inv:  (o1 != sender && o1 != to) ==>
      (
        t.totalSupply() = old(t.totalSupply()) &&
        t.balanceOf(o1) = old(t.balanceOf(o1)) &&
        t.allowance(o2, o3) = old(t.allowance(o2, o3))
      )
      over t.transfer(to, amt)
