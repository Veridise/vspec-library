vars: ERC721 t
inv:  reverted(t.burn(id),
  sender != t.getApproved(id) &&
  !t.isApprovedForAll(t.ownerOf(id), sender) &&
  t.ownerOf(id) != sender
)
