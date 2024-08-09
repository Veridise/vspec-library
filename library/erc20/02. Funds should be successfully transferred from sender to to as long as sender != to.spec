vars: ERC20 t
inv:  to != sender ==>
      (
        t.balanceOf(sender) = old(t.balanceOf(sender)) - amt &&
        t.balanceOf(to) = old(t.balanceOf(to)) + amt
      )
      over t.transfer(to, amt)
