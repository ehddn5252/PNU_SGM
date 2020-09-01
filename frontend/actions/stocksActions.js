export const stocks_getData = () => async dispatch => {
  try {
    dispatch({
      type: "AWAITING_STOCKS"
    })

    const response = await fetch("http://localhost:3000/api/stocks")
    const data = await response.json()
    const stocks = data.stocks
    console.log(stocks)

    const stocks_data = []

    const count = stocks.length

    for (var i = 0; i < count; i++) {
      stocks_data.push(stocks[i])
    }

    dispatch({
      type: "SUCCESS_STOCKS",
      payload: {
        stocks_data
      }
    })
  } catch (e) {
    dispatch({
      type: "REJECTED_STOCKS"
    })
  }
}
