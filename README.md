# Equity Token

## Type 
**Security token (SEC) / Asset token (FINMA)**

> Assets such as participation in real physical underlyings, companies, or earnings streams, or an entitlement to dividends or interest payments.

https://medium.com

## Description
The equity token helps to maintain a registry of shareholders, along with
the rights associated to their weight.

Those rights are driven by the vote policy, which can be "One dollar one vote"
or "One person one vote".

This token allows shareholders to delegate their power to other shareholders
using allowances, making a difference between "organic" shares/weight and
actual one.

## Characteristics

This token has following properties.

### Decimals
A share is atomic and cannot be split. Thus, it has no decimals.

### Roles
The token creator is called the **emitter**. The emitter is meant to represent 
the board of directors of the company with shares.

The emitter is entitled with all the shares when the token is created. 
Throughout time, the emitter is the only one who can change most of the 
settings of the token.

Each other account is a normal one and does not any hold special permission.

### Supply management
When a company joins a market place, it has a defined number of shares.
However, it is not uncommon to see shares being split or merged.
In those cases, the emitter (only) can perform a stock split to change the
total supply.

The token contract also allow the emitter to mint or burn token as it is part
of the T1 protocol. However, those method might not have a business case to
comply to.

### Transfer conditions
No specific restrictions on transfer.

### Allowances conditions
No specific restrictions on allowances.

One might decide to forbid allowances though, depending
on the use case (maybe the company does not allow it).

### Others
The Shares token introduces another form of allowance called delegation.
This mechanism is also known as vote by proxy.

Delegation lets shareholders temporarily forward their shareholder rights to
someone else. Shareholder rights can only be delegated to one person at a time.
In addition, once a shareholder has delegated his rights, he can't use them, 
unless the delegation his cancel.