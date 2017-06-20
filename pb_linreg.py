def lin_reg_pbratio(stock_list, date):
    # stock list can be either industry or a list of stocks
    # date should be input as a string

    # market cap
    # use A-share Market Valuation
    # therefore ignore the effect of foreign markets on valuation
    mc = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.a_share_market_val).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = '2016-12-30', interval = '8q')

    # book value
    # use public p/b ratio to calculate corresponding book value
    pb = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.pb_ratio).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = '2016-12-30', interval = '8q')

    mc_spec = numpy.array(mc.major_xs(date))
    pb_spec = numpy.array(pb.major_xs(date))
    # give a specific date, pull out the mc and te data of all companies

    mc_arr = mc_spec[0][0];
    pb_arr = pb_spec[0][0];
    mc_data = mc_arr.astype(float);
    pb_data = pb_arr.astype(float);
    #data structure change, into float arrays

    bv_data = mc_arr/pb_arr;
    bv_data = bv_data.astype(float);
    # use element-wise division to calculate corresponding book value

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(bv_data, mc_data)

    return slope, intercept
