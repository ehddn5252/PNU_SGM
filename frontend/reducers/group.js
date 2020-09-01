export const initialState = {
  strategyName: "",
  strategyNumber: "",
  writerName: "",
  strategyDescription: "",

  investment: "",
  investment_Start: "",
  investment_End: "",
  maxStockNumber: "",
  userMarketCap: "",

  userROE: "",
  userROA: "",
  userSalesPerProfit: "",
  userSalesPerMargin: "",
  userSalesIncrese: "",
  userMarginIncrease: "",
  userProfitIncrease: "",
  userDebtRatio: "",
  userCurrentRatio: "",
  userOperatingActivityCashFlow: "",
  userInvestmentActivityCashFlow: "",
  userFinancialActivityCashFlow: "",

  userEPS_Start: "",
  userEPS_End: "",
  userBPS_Start: "",
  userBPS_End: "",
  userCFPS_Start: "",
  userCFPS_End: "",
  userSPS_Start: "",
  userSPS_End: "",
  userDPS_Start: "",
  userDPS_End: "",

  userPER_Start: "",
  userPER_End: "",
  userPBR_Start: "",
  userPBR_End: "",
  userPCR_Start: "",
  userPCR_End: "",
  userPSR_Start: "",
  userPSR_End: "",
  userMarketDiviend_Start: "",
  userMarketDiviend_End: "",

  purchaseCondition: "",
  targetPrice: "",
  sellPrice: "",
  revalancingPeriod: ""
}

export const ADD_PARAMETERS = "ADD_PARAMETERS"

export const addParametersAction = data => {
  return {
    type: ADD_PARAMETERS,
    data
  }
}

export default (state = initialState, action) => {
  const { type, data } = action

  switch (type) {
    case ADD_PARAMETERS: {
      return {
        ...state,
        investment: data.investment,
        investment_Start: data.investment_Start,
        investment_End: data.investment_End,
        maxStockNumber: data.maxStockNumber,
        userMarketCap: data.userMarketCap,

        userROE: data.userROE,
        userROA: data.userROA,
        userSalesPerProfit: data.userSalesPerProfit,
        userSalesPerMargin: data.userSalesPerMargin,
        userSalesIncrese: data.userSalesIncrese,
        userMarginIncrease: data.userMarginIncrease,
        userProfitIncrease: data.userProfitIncrease,
        userDebtRatio: data.userDebtRatio,
        userCurrentRatio: data.userCurrentRatio,
        userOperatingActivityCashFlow: data.userOperatingActivityCashFlow,
        userInvestmentActivityCashFlow: data.userInvestmentActivityCashFlow,
        userFinancialActivityCashFlow: data.userFinancialActivityCashFlow,

        userEPS_Start: data.userEPS_Start,
        userEPS_End: data.userEPS_End,
        userBPS_Start: data.userBPS_Start,
        userBPS_End: data.userBPS_End,
        userCFPS_Start: data.userCFPS_Start,
        userCFPS_End: data.userCFPS_End,
        userSPS_Start: data.userSPS_Start,
        userSPS_End: data.userSPS_End,
        userDPS_Start: data.userDPS_Start,
        userDPS_End: data.userDPS_End,

        userPER_Start: data.userPER_Start,
        userPER_End: data.userPER_End,
        userPBR_Start: data.userPBR_Start,
        userPBR_End: data.userPBR_End,
        userPCR_Start: data.userPCR_Start,
        userPCR_End: data.userPCR_End,
        userPSR_Start: data.userPSR_Start,
        userPSR_End: data.userPSR_End,
        userMarketDiviend_Start: data.userMarketDiviend_Start,
        userMarketDiviend_End: data.userMarketDiviend_End,

        purchaseCondition: data.purchaseCondition,
        targetPrice: data.targetPrice,
        sellPrice: data.sellPrice,
        revalancingPeriod: data.revalancingPeriod
      }
    }

    default: {
      return {
        ...state
      }
    }
  }
}
