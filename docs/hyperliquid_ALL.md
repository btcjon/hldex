
## Api

Documentation for the Hyperliquid public API

You can also use the API via the Hyperliquid Python SDK… https://github.com/hyperliquiddex/hyperliquid-python-sdk All example API calls use the Mainnet url (https://api.hyperliquid.xyz), but you can make the same requests against Testnet using the corresponding url (https://api.hyperliquid-testnet.xyz)

## Notation

The API currently uses some nonstandard notation. Relevant changes will be batched into a breaking v1 API change.
About Hyperliquid Getting started Technical overview Trading Vaults
Referrals
Abbreviation
Full name
Px
Price
Sz
Size
Szi
Signed size
Ntl
Notional
Side
Side of trad
Open interest rewards Historical data Risks Roadmap Testnet Audits Brand kit

## Asset Ids

FOR DEVELOPERS
API
Tick and lot size
When requests expect an integer for 
asset , use the index of the coin found
in the meta  info response. E.g. BTC = 
0  on mainnet.
Nonces Info endpoint Exchange endpoint Websocket Error responses Rate limits Bridge2
Powered By GitBook
Asset
Asset
Tif
Time in forc
Previous
Brand kit
Next
Tick and lot size
Last modified 4d ago

## About Hyperliquid Getting Started Bridge2 Technical Overview Trading Vaults Points

The hyperliquid bridge native USDC and is secured by the L1 validator set: https://arbiscan.io/address/0¨2df1c51e 09aecf9cacb7bc98cb1742757f163df7

## Referrals

Open interest rewards Historical data Risks
The deposit flow is for the bridge is simple. The user sends native USDC to the bridge and it is credited to the account that sent it in less than 1 minute.

## Roadmap Testnet Audits

Brand kit
The withdrawal flow requires a user wallet signature on the L1 only, and no Arbitrum transaction. The withdrawal from Arbitrum is handled entirely the validators, and the funds arrive in the user wallet in 3c4 minutes. This payload for signTypedData is

## For Developers Api

Tick and lot size Nonces Info endpoint Exchange endpoint Websocket Error responses Rate limits
Bridge2
and the corresponding L1 action is
    #[derive(Debug, Clone, Eip712, #[eip712( name = "Exchange", version = "1", chain_id = 421613, verifying_contract = "0x00 )] struct WithdrawFromBridge2Sign destination: String, usd: String, time: u64, }

struct WithdrawFromBridge2Action {
Example signed L1 action:
    chain: String, payload: WithdrawFromBridge2Si
{ }
    "action": { "type": "withdraw2", "chain": "Arbitrum", "payload": { "destination": "0x000. "usd": "12.3", "time": 1698693262 } }, "nonce": 1698693262 // IMPORTA "signature": {"r": ..., "s": .

}
Previous Rate limits Last modified 1mo ago

## About Hyperliquid Getting Started Technical Overview Error Responses Trading

Vaults Points
Order and cancel errors are returned as a vector with same length as the batched request.
Referrals
Open interest rewards
Below is a list of possible error responses:
Historical data Risks Roadmap Testnet Audits Brand kit
FOR DEVELOPERS
API
Tick and lot size Nonces Info endpoint Exchange endpoint Websocket
Error responses
Rate limits Bridge2
Error source
Error type
Error string
Order
Tick
Price must be divisible by tick size.
Order
MinTrad eNtl
Order must
have minimum value of $10
Order
Margin
Insufficie nt margin to place order.
Order
Reduce Only
Reduce only order would increase position.
Order
BadAloP x
Post only order
would
have immediat ely matched
, bbo was {bbo}.
Order
IocCanc el
Order could not immediat ely match against any resting orders.
Order
BadTrigg erPx
Invalid TP/SL price.
Order
MarketO
rderNoLi quidity
No liquidity available
for market order.
Cancel
Missing Order
Order was never placed, already canceled

Rate limits Last modified 3mo ago

About Hyperliquid Getting started Technical overview

## Exchange Endpoint

Trading Vaults Points Referrals
Open interest rewards
The exchange endpoint is used to interact with and trade on the Hyperliquid chain. It is highly recommended that you examine the Python SDK to see how to generate signatures for these requests.
Historical data Risks Roadmap Testnet Audits Brand kit
FOR DEVELOPERS
API
Tick and lot size Nonces Info endpoint
Exchange endpoint
Websocket Error responses Rate limits Bridge2
POST
https://api.hyperliquid.xyz
/exchange
Place an order
POST
https://api.hyperliquid.xyz
/exchange
Cancel order(s)
POST
https://api.hyperliquid.xyz/exchange 
Cancel order(s) by cloid
POST
https://api.hyperliquid.xyz/exchange
  
Modify an order
POST
https://api.hyperliquid.xyz
/exchange
Modify multiple orders
POST
https://api.hyperliquid.xyz
/exchange
Update leverage
POST
https://api.hyperliquid.xyz
/exchange
Update isolated margin
POST
https://api.hyperliquid.xyz
/exchange
L1 USDC transfer
POST
https://api.hyperliquid.xyz
/exchange
Initiate a Withdrawal Request
Previous
Info endpoint
Next
Websocket

## About Hyperliquid

Getting started

## Info Endpoint Technical Overview

Trading Vaults Points
The info endpoint is used to fetch information about the exchange and specific users. The different request bodies result in different corresponding response body schemas.

## Referrals

Open interest rewards

## Pagination

Historical data Risks Roadmap
Note that responses that take a time range will only return 500 elements or distinct blocks of data. To query larger ranges, use the last returned timestamp
as the next startTime  for pagination.
Testnet Audits Brand kit
FOR DEVELOPERS
API
Tick and lot size Nonces
Info endpoint
Exchange endpoint Websocket Error responses Rate limits Bridge2
POST
https://api.hyperliquid.xyz/info
Retrieve exchange metadata
POST
https://api.hyperliquid.xyz/info
Retrieve all mids for all actively traded coins
POST
https://api.hyperliquid.xyz/info
Retrieve asset contexts (includes mark price, current funding, open interest, etc)
POST
https://api.hyperliquid.xyz/info
Retrieve a user's state
POST
https://api.hyperliquid.xyz/info
Retrieve a user's open orders
POST
https://api.hyperliquid.xyz/info
Retrieve a user's open orders with additional frontend info
POST
https://api.hyperliquid.xyz/info
Retrieve a user's fills
POST
https://api.hyperliquid.xyz/info
Retrieve a user's fills by time
POST
https://api.hyperliquid.xyz/info
Retrieve a user's funding history
POST
https://api.hyperliquid.xyz/info
POST
https://api.hyperliquid.xyz/info
Retrieve historical funding rates Retrieve L2 book snapshot.
POST
https://api.hyperliquid.xyz/info
Retrieve candle snapshot.
POST
https://api.hyperliquid.xyz/info
Query order status by oid or cloid
Previous
Nonces
Next
Exchange endpoint
Last modified 5d ago
About Hyperliquid Getting started

## Nonces

Technical overview Trading Vaults Points
Each request must have a unique nonce. Furthermore, no nonce can be lower than the 10th lowest nonce that has been on the L1. See the python and rust SDKs for example implementations.
Referrals
Open interest rewards Historical data Risks
If sending many requests concurrently, it may be helpful to use batched orders and cancels to ensure that the nonces are ordered within an index distance of 10 when received by the L1. 
Roadmap Testnet Audits Brand kit
FOR DEVELOPERS
API
Tick and lot size
Nonces
Info endpoint Exchange endpoint Websocket Error responses Rate limits Bridge2
Previous
Tick and lot size
Next
Info endpoint
Last modified 4d ago

About Hyperliquid

Getting started

## Rate Limits

Technical overview Trading

The following rate limits apply per IP address:

Vaults Points Referrals
Open interest rewards Historical data Risks Roadmap Testnet Audits Brand kit
FOR DEVELOPERS
API
Tick and lot size Nonces Info endpoint Exchange endpoint Websocket
Use websockets for lowest latency realtime data. See the python SDK for a full-featured example.
Error responses
Rate limits

## Address-Based L1 Rate Limits

Bridge2

The L1 rate limiting logic will allow 10 requests per 1 USDC traded cumulatively since address inception. Even using the minimum order value of 10 USDC, this only requires a fill rate of

All REST requests have a weight limit of 1200 per minute. All
documented exchange  API
requests have a weight of 1. All
documented info  API requests
have a weight of either 2 or 20; these limits can be found in the description for each info request in the Info endpoint section. Maximum of 100 websocket connections Maximum of 1000 websocket subscriptions Maximum of 10 unique users across user-specific websocket
subscriptions Maximum of 600 inbound messages per minute across all websocket connections

1%. Each address starts with an initial buffer of 10000 requests. When rate limited, an address will still be allowed one request every 10 seconds. Note that this rate limit only applies to L1 actions, not info requests.

About Hyperliquid Getting started Technical overview

## Tick And Lot Size Trading Vaults Points

Both Price (px) and Size (sz) have a maximum number of decimals that are accepted. 
Referrals
Open interest rewards Historical data Risks Roadmap Testnet
Prices can have up to 5 significant figures, but no more than 6 decimals
places. For example, 1234.5  is valid but 1234.56  is not (too many significant figures). 0.001234  is valid, but 0.0012345  is not (more than 6
decimal places).
Audits Brand kit
Sizes are rounded to the szDecimals
of that asset. For example, if 
szDecimals = 3  then 1.001  is a
valid size but 1.0001  is not. 

## For Developers

API
Tick and lot size
You can find the szDecimals  for an
asset by making a meta request to the info endpoint
Nonces Info endpoint Exchange endpoint Websocket Error responses Rate limits Bridge2
For developers c Previous
API
Next
Nonces
Last modified 4d ago

About Hyperliquid Getting started

## Websocket

Technical overview Trading

## Vaults Points Referrals

Open interest rewards

WebSocket endpoints are available for real-time data streaming on the Hyperliquid cryptocurrency exchange. The WebSocket URL for the mainnet is wss://api.hyperliquid.xyz/ws , and for the testnet, it is wss://api.hyperliquidtestnet.xyz/ws .

Historical data Risks

## Connection

Roadmap Testnet

## Audits Brand Kit For Developers

To connect to the WebSocket API, establish a WebSocket connection to the respective URL based on your desired network. Once connected, you can start sending subscription messages to receive real-time data updates.

## Api

Tick and lot size Nonces Info endpoint Exchange endpoint
Note: this doc uses Typescript for defining many of the message types. If you prefer to use python, you can checkout the equivalent types in the python sdk 
 and example
connection code 
.
Websocket
Error responses

## Subscription Messages

Rate limits Bridge2
To subscribe to specific data feeds, you need to send a subscription message. The subscription message format is as follows:
here
here

{ "method": "subscribe", "subscription": { ... }
The subscription object contains the details of the specific feed you want to subscribe to. Choose from the following subscription types and provide the corresponding properties:

1.
allMids :

Subscription message: { "type": "allMids" } Data format: AllMids

2.
notification :

Subscription message: { "type": "notification", "user": "<address>" } Data format: Notification

3.
webData2

Subscription message: { "type": "webData2", "user": "<address>" } Data format: WebData2

4.
candle :

Subscription message: { "type": "candle", "coin": "<coin_symbol>", "interval": " <candle_interval>" } Data format: WsTrade[]

5.
l2Book :

Subscription message: { "type": "l2Book", "coin": "<coin_symbol>" } Data format: WsBook

6.
trades :

Subscription message: { "type": "trades", "coin": "<coin_symbol>" } Data format: WsTrade[]

7.
orderUpdates :

Subscription message: { "type": "orderUpdates", "user": "<address>" }
Data format: WsOrder[]

8.
userEvents : 

Subscription message: { "type": "user", "user": " <address>" } Data format: WsUserEvent

9.
userFills : 

Subscription message: { "type": "userFills", 
"user": "<address>" }
Data format: WsUserFills

10.
userFundings : 

Subscription message: { "type": "userFundings", "user": "<address>" }
Data format: 
WsUserFundings

11.
userNonFundingLedgerUpdate
s : 

Subscription message: { "type": "userNonFundingLedgerUpd ates", "user": " <address>" }
Data format: 
WsUserNonFundingLedgerU
pdates

## Data Formats

The server will respond to successful subscriptions with a message containing the channel  property set to "subscriptionResponse" , along with the data  field providing the original subscription. The server will then start sending messages with the channel  property set to the corresponding subscription type e.g. 

"allMids"  and the data  field providing the subscribed data.

The data  field format depends on the subscription type:
AllMids … All mid prices.

Format: AllMids { mids: Record<string, string> }
Notification … A notification message.

Format: Notification { 
notification: string }
WebData2 … Aggregate information about a user, used primarily for the frontend.

Format: WebData2
WsTrade[] … An array of trade updates.

Format: WsTrade[]
WsBook … Order book updates.

Format: WsBook { coin: 
string; levels: 
[Array<WsLevel>, 
Array<WsLevel>]; time: 
number; }

WsOrder … User order updates.

Format: WsOrder[]

WsUserEvent … User events that
are not order updates

Format: WsUserEvent { 
"fills": [WsFill] | 
"funding": WsUserFunding 
| "liquidation": 
WsLiquidation | 
"nonUserCancel": 
[WsNonUserCancel] }

WsUserFills  … Fills snapshot
followed by streaming fills WsUserFundings  … Funding
payments snapshot followed by

funding payments on the hour
WsUserNonFundingLedgerUpdate
s … Ledger updates not including
funding payments: withdrawals,
deposits, transfers, and liquidations

For the streaming user endpoints such as WsUserFills , WsUserFundings the first message has isSnapshot: true  and the following streaming updates have isSnapshot: false . 

## Data Type Definitions

Here are the definitions of the data types used in the WebSocket API…
interface WsTrade { coin: string; side: string; px: string; sz: string; hash: string; time: number; }

interface WsBook {
  coin: string; levels: [Array<WsLevel>, Array<W time: number; }

interface WsLevel {
  px: string; // price sz: string; // size n: number; // number of orders } interface Notification { notification: string; } interface AllMids { mids: Record<string, string>; } type WsUserEvent = WsFill[] | WsUs interface WsUserFill {
  coin: string;
  px: string; // price sz: string; // size
  side: string;
  time: number; startPosition: string; dir: string; // used for fronten closedPnl: string; hash: string; // L1 transaction oid: number; // order id crossed: boolean; // whether ord fee: string; // negative means r tid: number; // unique trade id }
interface WsUserFunding {
  time: number; coin: string; usdc: string; szi: string; fundingRate: string; } interface WsLiquidation { lid: number; liquidator: string; liquidated_user: string; liquidated_ntl_pos: string; liquidated_account_value: string } interface WsNonUserCancel { coin: String; oid: number; } interface WsOrder { order: WsBasicOrder; status: string; statusTimestamp: number; } interface WsBasicOrder { coin: string; side: string; limitPx: string; sz: string; oid: number; timestamp: number; origSz: string; cloid: string | undefined;
Please note that the above data types are in TypeScript format, and their usage corresponds to the respective subscription types.

## Examples

Here are a few examples of subscribing to different feeds using the subscription messages:

1.
Subscribe to all mid prices:

{ "method": "subscribe", "subsc

2. Subscribe to notifications for a
specific user:

{ "method": "subscribe", "subsc

3. Subscribe to web data for a
specific user:

{ "method": "subscribe", "subsc

4. Subscribe to candle updates for a
specific coin and interval:

{ "method": "subscribe", "subsc

5. Subscribe to order book updates
for a specific coin:

{ "method": "subscribe", "subsc

6. Subscribe to trades for a specific
coin:

{ "method": "subscribe", "subsc

## Unsubscribing From Websocket Feeds

To unsubscribe from a specific data feed on the Hyperliquid WebSocket API, you need to send an unsubscribe message with the following format:
jsonCopy code{
  "method": "unsubscribe", "subscription": { ... } }
The subscription  object should match the original subscription message that was sent when subscribing to the feed. This allows the server to identify the specific feed you want to unsubscribe from. By sending this unsubscribe message, you inform the server to stop sending further updates for the specified feed. Please note that unsubscribing from a specific feed does not affect other subscriptions you may have active at that time. To unsubscribe from multiple feeds, you can send multiple unsubscribe messages, each with the appropriate subscription details.

## Timeouts And Heartbeats

The server will close any connection if it hasn't sent a message to it in the last 60 seconds. If you are subscribing to a channel that doesn't receive messages every 60 seconds, you can send heartbeat messages to keep your connection alive. The format for these messages are:
{ "method": "ping" }
The server will respond with:
{ "channel": "pong" }

Next
Error responses
Last modified 3d ago
