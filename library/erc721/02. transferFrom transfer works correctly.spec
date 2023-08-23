vars: ERC721 t
inv:  finished(t.transferFrom(from, to, id),
  to = t.ownerOf(id) &&
  t.getApproved(id) = address(0) &&
  t.balanceOf(from) = old(t.balanceOf(from)) - 1 &&
  t.balanceOf(to) = old(t.balanceOf(to)) + 1
)
