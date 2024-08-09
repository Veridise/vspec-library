vars: ERC721 t
spec: []!finished(t.transferFrom(from, to, id),
        old(
          from != t.ownerOf(id) ||
          sender != t.getApproved(id) ||
          !t.isApprovedForAll(from, sender) ||
          from != sender
        )
      )
