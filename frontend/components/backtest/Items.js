import React from "react"
import { useSelector, useDispatch } from "react-redux"
import { stocks_getData } from "../../actions/stocksActions"

const Items = () => {
  const dispatch = useDispatch()
  const stocksState = useSelector(state => state.stocksReducer)
  console.log(stocksState)

  const fetchData = () => {
    dispatch(stocks_getData())
  }
  console.log(stocksState)

  return (
    <>
      <div>{stocksState.loading}</div>
      <div>{stocksState.stocks}</div>
      {/* 임의로 만들어 놓은 버튼! */}
      <button onClick={() => fetchData()}>버튼</button>
    </>
  )
}

export default Items
