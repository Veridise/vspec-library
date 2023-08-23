vars: IERC3156FlashLender f
spec: []!finished(f.flashLoan(receiver, token, amt, data),
          f.maxFlashLoan(token) < old(f.maxFlashLoan(token)) ||
          token.balanceOf(address(f)) < old(token.balanceOf(address(f)))
)
