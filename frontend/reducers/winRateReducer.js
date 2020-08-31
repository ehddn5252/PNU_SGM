const initalState = {
  loading: false,
  data: {
    labels: ["Win", "Lose"],
    datasets: [
      {
        data: [],
        backgroundColor: ["#224ABA", "#FF7031"],
        hoverBackgroundColor: ["#224ABA", "#FF7031"]
      }
    ]
  }
}

const winRateReducer = (state = initalState, action) => {
  const { type, payload } = action

  switch (type) {
    case "AWAITING_WINRATE":
      return {
        ...state,
        loading: true
      }
    case "REJECTED_WINRATE":
      return {
        ...state,
        loading: false
      }
    case "SUCCESS_WINRATE":
      return {
        ...state,
        loading: false,
        data: {
          labels: ["Win", "Lose"],
          datasets: [
            {
              data: payload.winRate_data,
              backgroundColor: ["#224ABA", "#FF7031"],
              hoverBackgroundColor: ["#224ABA", "#FF7031"]
            }
          ]
        }
      }
    default:
      return state
  }
  return state
}

export default winRateReducer
