### The following function lists the top specified number of stocks by market
### cap
import numpy

def top_cap_stocks(top_num, date):
    # date put in a string the same format as "2016-12-30"

    mc = get_fundamentals(
            query(
                fundamentals.eod_derivative_indicator.market_cap),entry_date=date
        )

    mc_data = mc.major_xs(date)
    mc_data = mc_data.sort('market_cap', ascending=False)

    ##### stocks sorted by market cap at this point

    mc_real = mc_data[0:top_num]

    ##### top_num stocks ranked by market cap pulled out

    stocks = mc_real.index
    stocks = numpy.array(stocks)

    ##### A list of all qualifying stocks as a numpy ndarray dtype = object
    return stocks
