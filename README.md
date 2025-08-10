# market_colour

DESCRIPTION:
------------
This project was inspired by Bloomberg's API news feed for market colour, built using NewsAPI and Python. 

The purpose is to fetch and filter real-time market news for keywords relevant to macro, fixed income, commodities, FX, and credit. This reduces noise and gathers headlines that could impact portfolio positioning or trading decisions.

The keyword set I listed is fully customisable, meaning you can be alter it for:
- Asset class focus (e.g., fixed income vs. commodities)
- Geography (e.g., EM vs. DM)
- Market events (e.g., central bank interest rate changes)

To specify relevancy further, we can also tune the parameter set in lines 67. The line I wrote for the example is "q": "sovereign bond" but can be changed to something like "q": "oil futures" etc.

This project mirrors tools traders and portfolio managers use on a desk to maintain macroeconomic awareness throughout the their day. This allows for faster reaction to relevant news events, such as NFP, CPI, etc.

The concept came from my time on AXA IM’s trading floor, where market colour was constantly discussed between traders and portfolio managers. This script is a retail-level mimicking this.

HOW IT WORKS:
-------------
It follows a similar workflow to Bloomberg’s news feed API:

1) Connects to an API.

2) Requests articles and headlines.

3) Receives data in JSON.

4) Parses and filters the results.

5) Displays them in the Python terminal.


EXAMPLE OUTPUT (This is directly from my terminal:
---------------
Total articles fetched: 100
Articles matching keywords: 88

[1] Jain Global by the numbers: A look at the hedge fund's rollercoaster first year
Bobby Jain debuted one of the most complex and ambitious hedge fund launches ever. BI dug into the numbers behind its first year in business.
https://www.businessinsider.com/bobby-jain-global-first-year-charts-numbers-2025-7

[2] Ballooning U.S. National Debt Makes Short-Term Bonds A Wiser Choice
Market forces will likely dictate yield trends over the long term, and investors should prepare for potential volatility as sovereign risk grows.
https://www.forbes.com/sites/danirvine/2025/07/31/ballooning-us-national-debt-makes-short-term-bonds-a-wiser-choice/

[3] European Democracy Needs Its Middle Class Back
The middle class forms the core of our societies and the scaffolding that keeps our democracies standing. Rather than treat it as the collateral damage of inevitable progress, Europe's leaders should pursue a strategy to rebuild it, financed by European sover…
https://www.project-syndicate.org/commentary/comprehensive-strategy-to-restore-europe-middle-class-by-bertrand-badre-and-eric-hazan-2025-07

[4] Will U.S. Government Bonds Rally?
U.S. long-term interest rates remain elevated in July 2025, with the long bond futures in a two-year consolidation range that is closer to technical support ...
https://www.barchart.com/story/news/33626120/will-u-s-government-bonds-rally



