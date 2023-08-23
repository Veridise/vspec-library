vars: ERC721 t
inv:  finished(t.burn(id),
      t.ownerOf(id) = nulladdr &&
      t.getApproved(id) = nulladdr &&
      t.balanceOf(old(t.ownerOf(id))) = old(t.balanceOf(t.ownerOf(id))) - 1
      )
