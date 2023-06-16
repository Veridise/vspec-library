vars: ERC721 t, uint256 oid, address o1, address o2, address o3
inv:  finished(t.setApprovalForAll(spender, approved),
  o2 != sender && o1 != spender |=>
    approved = t.isApprovedForAll(sender, spender) &&
    t.isApprovedForAll(sender, o1) = old(t.isApprovedForAll(sender, o1)) &&
    t.isApprovedForAll(o2, o3) = old(t.isApprovedForAll(o2, o3)) &&
    t.getApproved(oid) = old(t.getApproved(oid)) &&
    t.ownerOf(oid) = old(t.ownerOf(oid)) &&
    t.balanceOf(o3) = old(t.balanceOf(o3))
)
