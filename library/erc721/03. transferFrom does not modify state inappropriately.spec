vars: ERC721 t, uint256 oid, address o1, address o2, address o3
inv:  finished(t.transferFrom(from, to, id),
  oid != id && o1 != from && o1 != to |=>
    t.ownerOf(oid) = old(t.ownerOf(oid)) &&
    t.getApproved(oid) = old(t.getApproved(oid)) &&
    t.balanceOf(o1) = old(t.balanceOf(o1)) &&
    t.isApprovedForAll(o2, o3) = old(t.isApprovedForAll(o2, o3))
)
