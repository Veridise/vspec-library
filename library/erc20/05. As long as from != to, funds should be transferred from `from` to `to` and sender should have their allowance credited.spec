vars: ERC20 t
inv:  from != to ==>
      (
        t.balanceOf(from) = old(t.balanceOf(from)) - amt &&
        t.balanceOf(to) = old(t.balanceOf(to)) + amt &&
        ( (from != sender && old(t.allowance(from, sender)) != MAX_UINT256) ==>
          t.allowance(from, sender) = old(t.allowance(from, sender)) - amt )
      )
      over t.transferFrom(from, to, amt)
