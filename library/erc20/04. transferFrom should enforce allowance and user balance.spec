vars: ERC20 t
inv:  reverted(t.transferFrom(from, to, amt),
  amt > t.balanceOf(from) || (from != sender && amt > t.allowance(from, sender))
)
