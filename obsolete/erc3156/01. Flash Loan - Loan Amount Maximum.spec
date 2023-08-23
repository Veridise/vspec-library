vars: IERC3156FlashLender f
inv: reverted(f.flashLoan(receiver, token, amt, data), 
              amt > f.maxFlashLoan(token)
)
