def lin_reg_peratio(stock_list, date):
    # stock list can be either industry or a list of stocks
    # date should be input as a string

    # market cap
    # use A-share Market Valuation
    # therefore ignore the effect of foreign markets on valuation
    mc = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.a_share_market_val).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = '2016-12-30', interval = '8q')

    # earnings
    # use public p/e ratio to calculate corresponding earnings
    pe = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.pe_ratio).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = '2016-12-30', interval = '8q')

    mc_spec = numpy.array(mc.major_xs(date))
    pe_spec = numpy.array(pe.major_xs(date))
    # give a specific date, pull out the mc and pe data of all companies

    mc_arr = mc_spec[0][0];
    pe_arr = pe_spec[0][0];
    mc_data = mc_arr.astype(float);
    pe_data = pe_arr.astype(float);
    #data structure change, into float arrays

    ean_data = mc_arr/pe_arr;
    ean_data = ean_data.astype(float);
    # use element-wise division to calculate corresponding book value

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ean_data, mc_data)

    return slope, intercept
