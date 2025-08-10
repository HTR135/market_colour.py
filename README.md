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


EXAMPLE OUTPUT (This is directly from my terminal):
<img width="1080" height="681" alt="Screenshot 2025-08-10 at 23 02 59" src="https://github.com/user-attachments/assets/b8168fbe-4b4e-4b91-b9dc-b031111799e3" />




