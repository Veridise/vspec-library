vars: ERC721 t
inv: reverted(t.approve(spender, id),
  sender != t.ownerOf(id) &&
  !isApprovedForAll(t.ownerOf(id), sender)
)
