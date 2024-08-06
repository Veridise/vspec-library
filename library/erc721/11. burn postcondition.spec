vars: ERC721 t
inv:  t.ownerOf(id) = nulladdr &&
      t.getApproved(id) = nulladdr &&
      t.balanceOf(old(t.ownerOf(id))) = old(t.balanceOf(t.ownerOf(id))) - 1
      over t.burn(id)
