**Overview**

Early-stage framework for analysing and signal generation of cross-asset price movement propagation following high-intensity macro-shock events. The strategy is built on an assumption that asset price movements are not independent events and instead follow temporary leader-laggard dynamics that change depending on macro regime and a hawkes process in which previous event intensity raises the likelihood of future events (trending price movements). 

First, an adjacency matrix is used to determine leaders-laggard assets and a rolling window beta correlation matrix is used to determine historical short-term mean-reversion between laggards and leaders. Next, intensity of macro-events are compared to the baseline through a hawkes process analysis of leader price movements. This ensures macro-shocks are true regime shifts and likely to lead to further trending price movements. Finally, a signal is generated when laggard assets haven't reflected the short-term historical estimated beta dynamics with a leader asset on the assumption that there will be a reversion to mean. 

**Key Features**
- Adjacency matrix between related macro assets to determine leader-laggard assets
- Event intensity filter through a hawkes process analysis
- Rolling OLS to determine short-term beta relationship between assets

**Future Improvements**
- Incorporate analysis of market-maker gamma positioning on asset futures options to filter for potential for gamma squeezes
- Sentiment analysis to determine qualitative market narratives heading into macro events
