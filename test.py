"""The test shows all the attributes that can be deduced from simply defining
rules and transferring a particular amount to a shareholder.

This is not a unit test.
"""

# We need to override the context sender to mimic a call from a particular
# account.
from pikciotok import context

import equity


def test_equity():
    # Let's create a new market share.
    context.sender = "Pikcio SA"
    equity.init(
        supply=13000000,
        name_="Pikciotronics Ltd",
        symbol_="PKT"
    )

    # Add another shareholder
    equity.transfer("John Doe", 1200000 * 10 ** equity.decimals)

    # Let's collect info now.
    print("John's equity: " + str(equity.get_shares("John Doe")))
    print("John's votes: " + str(equity.get_votes("John Doe")))
    print("John's weight: " + str(equity.get_weight("John Doe")))
    print("John's rights:\n- " + '\n- '.join(equity.get_rights("John Doe")))
    print("Is John majority ?: " + str(equity.is_majority("John Doe")))

    # Now let's change how vote works
    print("\nChanging vote policy to 'One person one vote'\n")
    equity.set_vote_mode(equity._VOTE_POLICY_OPOV)

    # And see how tables turn
    print("John's equity: " + str(equity.get_shares("John Doe")))
    print("John's votes: " + str(equity.get_votes("John Doe")))
    print("John's weight: " + str(equity.get_weight("John Doe")))
    print("John's rights:\n- " + '\n- '.join(equity.get_rights("John Doe")))
    print("Is John majority ?: " + str(equity.is_majority("John Doe")))


if __name__ == '__main__':
    test_equity()
