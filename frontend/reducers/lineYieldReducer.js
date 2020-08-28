const initalState = {
    loading: false,
    data: {
      labels: [],
      datasets: [{
        label: "KospiYield",
        data: [],
        fill : false,
        backgroundColor: '#224ABA',
        borderColor: '#224ABA',
        pointBorderColor: '#224ABA'
      },
      {
        label: "알고리즘 수익률",
        data: [],
        fill : false,
        backgroundColor: '#FF7031',
        borderColor: '#FF7031',
        pointBorderColor: '#FF7031'
      }
    ]
    }
  };
  
  const lineYieldReducer = (state = initalState, action) => {
    const { type, payload } = action;
  
    switch (type) {
      case "AWAITING_LINEYILD":
        return {
          ...state,
          loading: true
        }
      case "REJECTED_LINEYIELD":
        return {
          ...state,
          loading: false,
        }
      case "SUCCESS_LINEYIELD":
        return {
          ...state,
          loading: false,
          data: {
            labels: payload.labels,
            datasets: [
            {
              label: "KospiYield",
              data: payload.kospi_data,
              fill: false,
              backgroundColor: '#224ABA',
              borderColor: '#224ABA',
              pointBorderColor: '#224ABA'
            },
            {
              label: "알고리즘 수익률",
              data: payload.my_data,
              fill : false,
              backgroundColor: '#FF7031',
              borderColor: '#FF7031',
              pointBorderColor: '#FF7031'
            }
            ]
          }
        }
      default:
        return state;
    }
    return state;
  }
  
  export default lineYieldReducer;
  