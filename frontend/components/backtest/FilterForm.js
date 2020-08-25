import React, { useCallback, useState } from "react"
import { useSelector, useDispatch } from "react-redux"

import FilterLayout from "../layout/FilterLayout"
import useInput from "../LoginForm"
import addParametersAction from "../../reducers/group"

const FilterForm = () => {
  const group = useSelector(state => state.group)
  console.log(group)

  const dispatch = useDispatch()
  const { strategyName, onChangeStrategyName } = useInput("")
  const { strategyNumber, onChangeStrategyNumber } = useInput("")
  const { writerName, onChangeWriterName } = useInput("")
  const { strategyDescription, onChangeStrategyDescription } = useInput("")

  const { investment, onChangeInvestment } = useInput("")
  const { investment_Start, onChangeInvestment_Start } = useInput("")
  const { investment_End, onChangeInvestment_End } = useInput("")
  const { maxStockNumber, onChangeMaxStockNumber } = useInput("")
  const { userMarketCap, onChangeUserMarketCap } = useInput("")

  const { userROE, onChangeUserROE } = useInput("")
  const { userROA, onChangeUserROA } = useInput("")
  const { userSalesPerProfit, onChangeUserSalesPerProfit } = useInput("")
  const { userSalesPerMargin, onChangeUserSalesPerMargin } = useInput("")
  const { userSalesIncrese, onChangeUserSalesIncrese } = useInput("")
  const { userMarginIncrease, onChangeUserMarginIncrease } = useInput("")
  const { userProfitIncrease, onChangeUserProfitIncrease } = useInput("")
  const { userDebtRatio, onChangeUserDebtRatio } = useInput("")
  const { userCurrentRatio, onChangeUserCurrentRatio } = useInput("")

  const userOperatingActivityCashFlow = useState("")
  // const [
  //   userOperatingActivityCashFlow,
  //   onChangeUserOperatingActivityCashFlow
  // ] = useInput("")
  const userInvestmentActivityCashFlow = useState("")
  // const [
  //   userInvestmentActivityCashFlow,
  //   onChangeUserInvestmentActivityCashFlow
  // ] = useInput("")
  const userFinancialActivityCashFlow = useState("")
  // const [
  //   userFinancialActivityCashFlow,
  //   onChangeUserFinancialActivityCashFlow
  // ] = useInput("")

  const { userEPS_Start, onChangeUserEPS_Start } = useInput("")
  const { userEPS_End, onChangeUserEPS_End } = useInput("")

  const { userBPS_Start, onChangeUserBPS_Start } = useInput("")
  const { userBPS_End, onChangeUserBPS_End } = useInput("")

  const { userCFPS_Start, onChangeUserCFPS_Start } = useInput("")
  const { userCFPS_End, onChangeUserCFPS_End } = useInput("")

  const { userSPS_Start, onChangeUserSPS_Start } = useInput("")
  const { userSPS_End, onChangeUserSPS_End } = useInput("")

  const { userDPS_Start, onChangeUserDPS_Start } = useInput("")
  const { userDPS_End, onChangeUserDPS_End } = useInput("")

  const { userPER_Start, onChangeUserPER_Start } = useInput("")
  const { userPER_End, onChangeUserPER_End } = useInput("")

  const { userPBR_Start, onChangeUserPBR_Start } = useInput("")
  const { userPBR_End, onChangeUserPBR_End } = useInput("")

  const { userPCR_Start, onChangeUserPCR_Start } = useInput("")
  const { userPCR_End, onChangeUserPCR_End } = useInput("")

  const { userPSR_Start, onChangeUserPSR_Start } = useInput("")
  const { userPSR_End, onChangeUserPSR_End } = useInput("")

  const { userMarketDiviend_Start, onChangeUserMarketDiviend_Start } = useInput(
    ""
  )
  const { userMarketDiviend_End, onChangeUserMarketDiviend_End } = useInput("")

  const { purchaseCondition, onChangePurchaseCondition } = useInput("")
  const { targetPrice, onChangeTargetPrice } = useInput("")
  const { sellPrice, onChangeSellPrice } = useInput("")
  // const [revalancingPeriod, onChangeRevalancingPeriod] = useInput("")
  const revalancingPeriod = useState("")

  // const [strategyOpenStatus, onChangeStrategyOpenStatus] = useInput("")
  // const strategyOpenStatus = useState("")

  const onSubmitForm = useCallback(e => {
    e.preventDefault()
    console.log(group)
    dispatch(
      addParametersAction({
        strategyName,
        strategyNumber,
        writerName,
        strategyDescription,

        investment,
        investment_Start,
        investment_End,
        maxStockNumber,
        userMarketCap,

        userROE,
        userROA,
        userSalesPerProfit,
        userSalesPerMargin,
        userSalesIncrese,
        userMarginIncrease,
        userProfitIncrease,
        userDebtRatio,
        userCurrentRatio,
        userOperatingActivityCashFlow,
        userInvestmentActivityCashFlow,
        userFinancialActivityCashFlow,

        userEPS_Start,
        userEPS_End,
        userBPS_Start,
        userBPS_End,
        userCFPS_Start,
        userCFPS_End,
        userSPS_Start,
        userSPS_End,
        userDPS_Start,
        userDPS_End,

        userPER_Start,
        userPER_End,
        userPBR_Start,
        userPBR_End,
        userPCR_Start,
        userPCR_End,
        userPSR_Start,
        userPSR_End,
        userMarketDiviend_Start,
        userMarketDiviend_End,

        purchaseCondition,
        targetPrice,
        sellPrice,
        revalancingPeriod

        // strategyOpenStatus
      })
    )
    console.log(group)
  }, [])

  return (
    <>
      <form onSubmit={onSubmitForm} className="filter-form">
        <FilterLayout title="기본설정(필수)">
          <div>
            투자금
            <input
              type="number"
              name="investment"
              value={investment}
              onChange={onChangeInvestment}
              required
            />
            원
          </div>
          <div>
            투자기간
            <input
              type="number"
              name="investment_Start"
              value={investment_Start}
              onChange={onChangeInvestment_Start}
              required
            />
            ~
            <input
              type="number"
              name="investment_End"
              value={investment_End}
              onChange={onChangeInvestment_End}
              required
            />
          </div>
          <div>
            최대 보유 종목 수
            <input
              type="number"
              name="maxStockNumber"
              value={maxStockNumber}
              onChange={onChangeMaxStockNumber}
              required
            />
            개
          </div>
          <div>
            <input
              type="number"
              name="userMarketCap"
              value={userMarketCap}
              onChange={onChangeUserMarketCap}
              required
            />
          </div>
        </FilterLayout>

        <FilterLayout title="퀄리티 항목(재무제표 항목)">
          <div>
            <details open>
              <summary>퀄리티 항목(재무제표 항목)</summary>
              <div>수익성 지표</div>
              <div>
                <input type="checkbox" /> ROE
                <input
                  type="number"
                  name="userROE"
                  value={userROE}
                  onChange={onChangeUserROE}
                />
                이상
              </div>
              <div>
                <input type="checkbox" /> ROA
                <input
                  type="number"
                  name="userROA"
                  value={userROA}
                  onChange={onChangeUserROA}
                />
                이상
              </div>
              <div>
                <input type="checkbox" /> 매출액 대비 손이익률
                <input
                  type="number"
                  name="userSalesPerProfit"
                  value={userSalesPerProfit}
                  onChange={onChangeUserSalesPerProfit}
                />
                이상
              </div>
              <div>
                <input type="checkbox" /> 매출액 대비 영업이익률
                <input
                  type="number"
                  name="userSalesPerMargin"
                  value={userSalesPerMargin}
                  onChange={onChangeUserSalesPerMargin}
                />
                이상
              </div>
              <div>
                <input type="checkbox" /> 매출액 증가율
                <input
                  type="number"
                  name="userSalesIncrese"
                  value={userSalesIncrese}
                  onChange={onChangeUserSalesIncrese}
                />
                이상
              </div>

              <div>성장성 지표</div>
              <div>
                <input type="checkbox" /> 영업이익 증가율
                <input
                  type="number"
                  name="userMarginIncrease"
                  value={userMarginIncrease}
                  onChange={onChangeUserMarginIncrease}
                />
                이상
              </div>
              <div>
                <input type="checkbox" /> 순이익 증가율
                <input
                  type="number"
                  name="userProfitIncrease"
                  value={userProfitIncrease}
                  onChange={onChangeUserProfitIncrease}
                />
                이상
              </div>

              <div>안정성 지표</div>
              <div>
                <input type="checkbox" /> 부재비율
                <input
                  type="number"
                  name="userMarginIncrease"
                  value={userMarginIncrease}
                  onChange={onChangeUserDebtRatio}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 유동비율
                <input
                  type="number"
                  name="userCurrentRatio"
                  value={userCurrentRatio}
                  onChange={onChangeUserCurrentRatio}
                />
                이상
              </div>

              <div>현금흐름표 항목</div>
              <div>
                영업활동현금흐름
                <label>
                  <input
                    type="radio"
                    name="userOperatingActivityCashFlow"
                    value="-"
                  />
                  -
                </label>
                <label>
                  <input
                    type="radio"
                    name="userOperatingActivityCashFlow"
                    value="+"
                  />
                  +
                </label>
              </div>
              <div>
                투자활동현금흐름
                <label>
                  <input
                    type="radio"
                    name="userInvestmentActivityCashFlow"
                    value="-"
                  />
                  -
                </label>
                <label>
                  <input
                    type="radio"
                    name="userInvestmentActivityCashFlow"
                    value="+"
                  />
                  +
                </label>
              </div>
              <div>
                재무활동현금흐름
                <label>
                  <input
                    type="radio"
                    name="userFinancialActivityCashFlow"
                    value="-"
                  />
                  -
                </label>
                <label>
                  <input
                    type="radio"
                    name="userFinancialActivityCashFlow"
                    value="+"
                  />
                  +
                </label>
              </div>
            </details>
          </div>
        </FilterLayout>

        <FilterLayout title="벨류 항목">
          <div>
            <details open>
              <summary>벨류 항목</summary>
              <div>주당 가치평가 지표</div>
              <div>
                <input type="checkbox" /> 주당순이익(EPS)
                <input
                  type="number"
                  name="userEPS_Start"
                  value={userEPS_Start}
                  onChange={onChangeUserEPS_Start}
                />
                이상
                <input
                  type="number"
                  name="userEPS_End"
                  value={userEPS_End}
                  onChange={onChangeUserEPS_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주당순자산(BPS)
                <input
                  type="number"
                  name="userBPS_Start"
                  value={userBPS_Start}
                  onChange={onChangeUserBPS_Start}
                />
                이상
                <input
                  type="number"
                  name="userBPS_End"
                  value={userBPS_End}
                  onChange={onChangeUserBPS_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주당현금흐름(CFPS)
                <input
                  type="number"
                  name="userCFPS_Start"
                  value={userCFPS_Start}
                  onChange={onChangeUserCFPS_Start}
                />
                이상
                <input
                  type="number"
                  name="userCFPS_End"
                  value={userCFPS_End}
                  onChange={onChangeUserCFPS_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주당매출액(SPS)
                <input
                  type="number"
                  name="userSPS_Start"
                  value={userSPS_Start}
                  onChange={onChangeUserSPS_Start}
                />
                이상
                <input
                  type="number"
                  name="userSPS_End"
                  value={userSPS_End}
                  onChange={onChangeUserSPS_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주당배당금(DPS)
                <input
                  type="number"
                  name="userDPS_Start"
                  value={userDPS_Start}
                  onChange={onChangeUserDPS_Start}
                />
                이상
                <input
                  type="number"
                  name="userDPS_End"
                  value={userDPS_End}
                  onChange={onChangeUserDPS_End}
                />
                이하
              </div>

              <div>주가 가치 평가 지표</div>
              <div>
                <input type="checkbox" /> 주당수익배수(PER)
                <input
                  type="number"
                  name="userPER_Start"
                  value={userPER_Start}
                  onChange={onChangeUserPER_Start}
                />
                이상
                <input
                  type="number"
                  name="userPER_End"
                  value={userPER_End}
                  onChange={onChangeUserPER_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주가순자산배수(PBR)
                <input
                  type="number"
                  name="userPBR_Start"
                  value={userPBR_Start}
                  onChange={onChangeUserPBR_Start}
                />
                이상
                <input
                  type="number"
                  name="userPBR_End"
                  value={userPBR_End}
                  onChange={onChangeUserPBR_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주가현금흐름배수(PCR)
                <input
                  type="number"
                  name="userPCR_Start"
                  value={userPCR_Start}
                  onChange={onChangeUserPCR_Start}
                />
                이상
                <input
                  type="number"
                  name="userPCR_End"
                  value={userPCR_End}
                  onChange={onChangeUserPCR_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 주가매출액배수(PSR)
                <input
                  type="number"
                  name="userPSR_Start"
                  value={userPSR_Start}
                  onChange={onChangeUserPSR_Start}
                />
                이상
                <input
                  type="number"
                  name="userPSR_End"
                  value={userPSR_End}
                  onChange={onChangeUserPSR_End}
                />
                이하
              </div>
              <div>
                <input type="checkbox" /> 시가 배당률
                <input
                  type="number"
                  name="userMarketDiviend_Start"
                  value={userMarketDiviend_Start}
                  onChange={onChangeUserMarketDiviend_Start}
                />
                이상
                <input
                  type="number"
                  name="userMarketDiviend_End"
                  value={userMarketDiviend_End}
                  onChange={onChangeUserMarketDiviend_End}
                />
                이하
              </div>
            </details>
          </div>
        </FilterLayout>

        <FilterLayout title="매수/매도 조건">
          <div>
            <details open>
              <summary>매수/매도 조건</summary>
              <div>매수 조건</div>
              <div>
                시작 날짜 증가 대비
                <input
                  type="number"
                  name="purchaseCondition"
                  value={purchaseCondition}
                  onChange={onChangePurchaseCondition}
                />
                %(마이너스 가능)
              </div>

              <div>매도 조건(조건 부합시 매도, 가격 기준은 전일 송가)</div>
              <div>
                목표가: 매수가+
                <input
                  type="number"
                  name="targetPrice"
                  value={targetPrice}
                  onChange={onChangeTargetPrice}
                />
                %
              </div>
              <div>
                손절가: 매수가+
                <input
                  type="number"
                  name="sellPrice"
                  value={sellPrice}
                  onChange={onChangeSellPrice}
                />
                %
              </div>
              <div>
                리밴런싱:
                <label>
                  <input type="radio" name="revalancingPeriod" value="분기별" />
                  분기별
                </label>
                <label>
                  <input type="radio" name="revalancingPeriod" value="연간" />
                  연간
                </label>
                <label>
                  <input
                    type="radio"
                    name="revalancingPeriod"
                    value="선택안함"
                  />
                  선택안함
                </label>
              </div>
            </details>
          </div>
        </FilterLayout>
        <button type="submit">백테스팅</button>
      </form>
    </>
  )
}

export default FilterForm
