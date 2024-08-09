vars: ERC20 t
inv:  (
        t.balanceOf(from) = old(t.balanceOf(from)) - amt &&
        t.totalSupply() = old(t.totalSupply()) - amt &&
        ( (from != sender || old(t.allowance(from, sender)) != MAX_UINT256)
      ) ==>
      t.allowance(from, sender) = old(t.allowance(from, sender)) - amt )
      over t.burnFrom(from, amt)
