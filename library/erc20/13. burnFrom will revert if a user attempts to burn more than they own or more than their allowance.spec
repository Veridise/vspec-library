vars: ERC20 t
inv:  reverted(t.burnFrom(from, amt),
  amt > t.balanceOf(from) || (from != sender && amt > t.allowance(from, sender))
)
