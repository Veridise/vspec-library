vars: ERC721 t
inv:  reverted(t.transferFrom(from, to, id),
  from != ownerOf(id) ||
  sender != getApproved(id) ||
  !isApprovedForAll(from, sender) ||
  from != sender
)
