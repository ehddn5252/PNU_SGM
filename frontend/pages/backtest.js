import React, { useState, useCallback } from "react"
import DashboardLayout from "../components/layout/DashboardLayout"
import FilterForm from "../components/backtest/FilterForm"
import Items from "../components/backtest/Items"
import Result from "../components/backtest/Result"
import MonthGraph from "../components/backtest/MonthGraph"
import OddsGraph from "../components/backtest/OddsGraph"
import MainGraph from "../components/backtest/MainGraph"

import { useSelector, useDispatch } from "react-redux"
import addParameters from "../reducers/group"
import addParametersAction from "../reducers/group"
import { useInput } from "../components/LoginForm"

import axios from "axios"

// 동주 수정사항
import { lineYield_getData } from "../actions/lineYieldActions"
import { winRate_getData } from "../actions/winRateActions"
import { Line, Doughnut } from "react-chartjs-2"

const BackTest = () => {
  //   const response = axios.get("api/hello").then(function (response) {
  //     console.log(response)
  //     console.log(response.data)
  //   })
  // console.log(response)

  // const group = useSelector(state => state.group);
  // console.log(group);

  // const dispatch = useDispatch();

  // const onSubmitForm = useCallback((e) => {
  //     e.preventDefault();
  //     dispatch(addParametersAction({
  //         idNumber,
  //         stretName,
  //         stretNum
  //     }));
  //     setStretNum('');
  //     setStretName('');
  // });

  // 동주 수정사항
  // 메인 그래프
  // 임의로 정한 버튼 나중에 backtest 버튼으로 대체해야함.
  const dispatch = useDispatch()
  const Mainstate = useSelector(state => state.lineYieldReducer)
  const winRatestate = useSelector(state => state.winRateReducer)

  const fetchData = () => {
    dispatch(lineYield_getData())
    dispatch(winRate_getData())
  }

  return (
    <div>
      <DashboardLayout>
        <div className="backtest-contents">
          {/* 결과section */}
          <section className="result-section">
            <div className="result-firstLine">
              <div className="result-firstLine-title">BACKTESTING RESULT</div>
              <div className="result-firstLine-detail">
                맥스턴은 코스피 주식을 기반으로, 거래 수수료0, 거래세0, 거래
                가격은 당일 종가를 기본으로 설정하고 있습니다.
              </div>
              <div className="result-box">
                <div className="item-result-box">
                  <article className="items">
                    <Items />
                  </article>
                  <article className="result">
                    <Result />
                  </article>
                </div>
                <article className="subGraph1">
                  <MonthGraph />
                </article>
                <article className="subGraph2">
                  {/* 임의의 승률 보여줌*/}
                  <Doughnut data={winRatestate.data} />
                </article>
              </div>
            </div>
            <div className="result-secondLine">
              <article className="mainGraph">
                {/* 잘 안보이지만 버튼 누르면 몽고디비에서 코스피 데이터 가져와서 그려줌 */}
                <button onClick={() => fetchData()}>kospiYield</button>
                <Line data={Mainstate.data} />
              </article>
            </div>
          </section>

          {/* 파라미터 section */}
          <section className="parameter-section">
            <div className="parameter-title">PARAMETER</div>
            <div className="parameter-detail">
              맥스턴은 코스피 주식을 기반으로, 거래 수수료0, 거래세0, 거래
              가격은 당일 종가를 기본으로 설정하고 있습니다.
            </div>
            <article className="filterContainer">
              <FilterForm />
              {/* <input 
                                type="text"
                                name="stret_name"
                                value={stretName}
                                onChange={onChangeStretName}
                            />
                            <input 
                                type="number"
                                name="stret_num"
                                value={stretNum}
                                onChange={onChangeStretNum}
                            />
                            <button type="submit">제출</button> */}
            </article>
          </section>
        </div>
      </DashboardLayout>
    </div>
  )
}

export default BackTest
