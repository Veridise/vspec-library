vars: ERC721 t
spec: []!finished(t.approve(spender, id),
       old(
         sender != t.ownerOf(id) ||
         !t.isApprovedForAll(t.ownerOf(id), sender)
  )
)
