export const winRate_getData = () => async dispatch => {
    try {
      dispatch({
        type: "AWAITING_WINRATE"
      })
  
      const res = await fetch('http://localhost:3000/api/winRatetest');
      const doc = await res.json();
      
      const winRate_data = [];

      winRate_data.push(doc.win);
      winRate_data.push(doc.lose);
  
  
      dispatch({
        type: "SUCCESS_WINRATE",
        payload: {
          winRate_data
        }
      })
    } catch (e) {
      dispatch({
        type: "REJECTED_WINRATE",
      })
    }
  }
  