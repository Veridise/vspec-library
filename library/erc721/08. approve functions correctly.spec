vars: ERC721 t, uint256 oid1, uint256 oid2, address o1, address o2
inv: finished(t.approve(spender, id),
  oid1 != id |=>
    spender = t.getApproved(id) &&
    t.getApproved(oid1) = old(t.getApproved(oid1)) &&
    t.ownerOf(oid2) = old(t.ownerOf(oid2)) &&
    t.balanceOf(o1) = old(t.balanceOf(o1)) &&
    t.isApprovedForAll(o1, o2) = old(t.isApprovedForAll(o1, o2))
)
