vars: ERC721 t
spec: []!finished(t.burn(id),
  old(
    sender != t.getApproved(id) ||
    !t.isApprovedForAll(t.ownerOf(id), sender) ||
    t.ownerOf(id) != sender
  )
)
