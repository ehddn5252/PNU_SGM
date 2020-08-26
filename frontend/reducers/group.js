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
  console.log(action)
  switch (action.type) {
    case ADD_PARAMETERS: {
      return {
        ...state,
        strategyName: action.data.strategyName,
        strategyNumber: action.data.strategyNumber,
        writerName: action.data.writerName,
        strategyDescription: action.data.strategyDescription,

        investment: action.data.investment,
        investment_Start: action.data.investment_Start,
        investment_End: action.data.investment_End,
        maxStockNumber: action.data.maxStockNumber,
        userMarketCap: action.data.userMarketCap,

        userROE: action.data.userROE,
        userROA: action.data.userROA,
        userSalesPerProfit: action.data.userSalesPerProfit,
        userSalesPerMargin: action.data.userSalesPerMargin,
        userSalesIncrese: action.data.userSalesIncrese,
        userMarginIncrease: action.data.userMarginIncrease,
        userProfitIncrease: action.data.userProfitIncrease,
        userDebtRatio: action.data.userDebtRatio,
        userCurrentRatio: action.data.userCurrentRatio,
        userOperatingActivityCashFlow:
          action.data.userOperatingActivityCashFlow,
        userInvestmentActivityCashFlow:
          action.data.userInvestmentActivityCashFlow,
        userFinancialActivityCashFlow:
          action.data.userFinancialActivityCashFlow,

        userEPS_Start: action.data.userEPS_Start,
        userEPS_End: action.data.userEPS_End,
        userBPS_Start: action.data.userBPS_Start,
        userBPS_End: action.data.userBPS_End,
        userCFPS_Start: action.data.userCFPS_Start,
        userCFPS_End: action.data.userCFPS_End,
        userSPS_Start: action.data.userSPS_Start,
        userSPS_End: action.data.userSPS_End,
        userDPS_Start: action.data.userDPS_Start,
        userDPS_End: action.data.userDPS_End,

        userPER_Start: action.data.userPER_Start,
        userPER_End: action.data.userPER_End,
        userPBR_Start: action.data.userPBR_Start,
        userPBR_End: action.data.userPBR_End,
        userPCR_Start: action.data.userPCR_Start,
        userPCR_End: action.data.userPCR_End,
        userPSR_Start: action.data.userPSR_Start,
        userPSR_End: action.data.userPSR_End,
        userMarketDiviend_Start: action.data.userMarketDiviend_Start,
        userMarketDiviend_End: action.data.userMarketDiviend_End,

        purchaseCondition: action.data.purchaseCondition,
        targetPrice: action.data.targetPrice,
        sellPrice: action.data.sellPrice,
        revalancingPeriod: action.data.revalancingPeriod
      }
    }

    default: {
      return {
        ...state
      }
    }
  }
}
