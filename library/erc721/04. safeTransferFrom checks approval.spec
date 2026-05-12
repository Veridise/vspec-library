vars: ERC721 t
spec: []!finished(t.safeTransferFrom(from, to, id),
      from != t.ownerOf(id) ||
      old(
          sender != t.getApproved(id) &&
          !t.isApprovedForAll(from, sender) &&
          from != sender
      )
    )