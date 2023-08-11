pragma solidity ^0.8.19;

import {IERC3156FlashBorrower} from "./IERC3156FlashBorrower.sol";

contract ERC3156_NoBug_1 {

    uint256 constant private FEE_PRECISION = 10_000;

    address public owner;

    mapping(address => uint256) public feePerToken;
    mapping(address => uint256) public maxFlashLoanAmountPerToken;

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Only callable by owner, used to change the owner of the contract. 
     *      One-Step owner transfer, be careful.
     * @param newOwner The address of the new owner.
     */
    function changeOwner(address newOwner) external {
        require(msg.sender == owner);
        owner = newOwner;
    }

    /**
     * @dev The amount of currency available to be lended.
     * @param token The loan currency.
     * @return The amount of `token` that can be borrowed.
     */
    function maxFlasLoan(address token) external view returns (uint256) {
        return maxFlashLoanAmountPerToken[token];
    }

    /**
     * @dev The fee to be charged for a given loan.
     * @param token The loan currency.
     * @param amount The amount of tokens lent.
     * @return The amount of `token` to be charged for the loan, on top of the returned principal.
     */
    function flashFee(address token, uint256 amount) external view returns(uint256) {
        uint256 fee = feePerToken[token];

        return _flashFee()
        
        return (fee * amount) / FEE_PRECISION;
    }

    /**
     * @dev Only callable by owner, used to change the max flash loan for a given token.
     * @param token The loan currency.
     * @param maxFlashloan The max flash loan amount for the token.
     */
    function setMaxFlashLoanForToken(address token, uint256 maxFlashloan) external {
        require(msg.sender == owner);

        maxFlashLoanAmountPerToken[token] = maxFlashloan;
    }

    /**
     * @dev Only callable by owner, used to change the fee for flash loans of a given token.
     *      flashFee cannot be greater than FEE_PRECISION.
     * @param token The loan currency.
     * @param flashFee The fee to be set.
     */
    function setFlashFeePerToken(address token, uint256 flashFee) external {
        require(msg.sender == owner);
        require(flashFee <= FEE_PRECISION);

        feePerToken[token] = flashFee;
    }

    /**
     * @dev Initiate a flash loan.
     * @param receiver The receiver of the tokens in the loan, and the receiver of the callback.
     * @param token The loan currency.
     * @param amount The amount of tokens lent.
     * @param data Arbitrary data structure, intended to contain user-defined parameters.
     */
    function flashLoan(
        IERC3156FlashBorrower receiver,
        address token,
        uint256 amount,
        bytes calldata data
    ) external returns (bool) {
        require(amount <= maxFlashLoanAmountPerToken[token]);

        uint256 fee = 

        require(
            supportedTokens[token],
            "FlashLender: Unsupported currency"
        );
        uint256 fee = _flashFee(token, amount);
        require(
            IERC20(token).transfer(address(receiver), amount),
            "FlashLender: Transfer failed"
        );
        require(
            receiver.onFlashLoan(msg.sender, token, amount, fee, data) == CALLBACK_SUCCESS,
            "FlashLender: Callback failed"
        );
        require(
            IERC20(token).transferFrom(address(receiver), address(this), amount + fee),
            "FlashLender: Repay failed"
        );
        return true;
    }
}
