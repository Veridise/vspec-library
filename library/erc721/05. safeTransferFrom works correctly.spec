vars: ERC721 t
inv:  to = t.ownerOf(id) &&
      t.getApproved(id) = nulladdr &&
      t.balanceOf(from) = old(t.balanceOf(from)) - 1 &&
      t.balanceOf(to) = old(t.balanceOf(to)) + 1
      over t.safeTransferFrom(from, to, id)
