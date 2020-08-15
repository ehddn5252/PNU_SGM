from django.db import models


class User(models.Model):

    objects = models.Manager()
    username = models.CharField(max_length=32, verbose_name="사용자명", unique=True)
    password = models.CharField(max_length=32, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Users"
        verbose_name = "user"
        verbose_name_plural ="Users"


class Stretagy(models.Model):

    objects = models.Manager()
    # 기본 항목
    stret_name = models.CharField(max_length=128, verbose_name="전략명")
    stret_num = models.IntegerField(verbose_name="전략고유번호", unique=True)
    writer_name = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="전략작성자명")
    stret_descript = models.TextField(verbose_name="전략설명")
        
    # Tab1 기본 항목
    investment = models.IntegerField(verbose_name="투자원금")
    ivm_dttm_s = models.DateTimeField(verbose_name="투자 시작일")
    ivm_dttm_e = models.DateTimeField(verbose_name="투자 마감일")
    max_stock_num = models.IntegerField(verbose_name="최대 보유 종목수")
    u_market_cap = models.IntegerField(verbose_name="대상기업 최소시가총액")

    # Tab2 퀄리티 지표
    u_roe = models.IntegerField(verbose_name="최저 ROE", blank=True)
    u_roa = models.IntegerField(verbose_name="최저 ROA", blank=True)
    u_salesPerProfit = models.IntegerField(verbose_name="매출액대비 순이익률", blank=True)
    u_salesPerMargin = models.IntegerField(verbose_name="매출액 대비 영업이익률", blank=True)
    u_salesIncrease = models.IntegerField(verbose_name="매출액 증가율", blank=True)
    u_marginIncrease = models.IntegerField(verbose_name="영업이익 증가율", blank=True)
    u_profitIncrease = models.IntegerField(verbose_name="순이익 증가율", blank=True)
    u_debtRatio = models.IntegerField(verbose_name="부채비율", blank=True)
    u_currentRatio = models.IntegerField(verbose_name="유동비율", blank=True)
    u_oaCashFlow = models.BooleanField(verbose_name="영업활동현금흐름", blank=True)
    u_iaCashFlow = models.BooleanField(verbose_name="투자활동현금흐름", blank=True)
    u_maCashFlow = models.BooleanField(verbose_name="재무활동현금흐름", blank=True)

    # Tab3 벨류 지표

    # 주당 가치평가 지표
    u_eps_s = models.IntegerField(verbose_name="주당순이익(min)", blank=True)
    u_eps_e = models.IntegerField(verbose_name="주당순이익(max)", blank=True)
    u_bps_s = models.IntegerField(verbose_name="주당순자산(min)", blank=True)
    u_bps_e = models.IntegerField(verbose_name="주당순자산(max)", blank=True)
    u_cfps_s = models.IntegerField(verbose_name="주당현금흐름(min)", blank=True)
    u_cfps_e = models.IntegerField(verbose_name="주당현금흐름(max)", blank=True)
    u_sps_s = models.IntegerField(verbose_name="주당매출액(min)", blank=True)
    u_sps_e = models.IntegerField(verbose_name="주당매출액(max)", blank=True)
    u_dps_s = models.IntegerField(verbose_name="주당배당금(min)", blank=True)
    u_dps_e = models.IntegerField(verbose_name="주당배당금(max)", blank=True)

    # 주가 가치평가 지표
    u_per_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_per_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_pbr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_pbr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_pcr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_pcr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_psr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_psr_s = models.IntegerField(verbose_name="주가수익배수(min)", blank=True)
    u_marketDiviend_s = models.IntegerField(verbose_name="시가 배당률(min)", blank=True)
    u_marketDiviend_e = models.IntegerField(verbose_name="시가 배당률(max)", blank=True)

    # Tab4 매수 & 매도 조건
    purc_cond = models.IntegerField(verbose_name="매수조건(%)")
    targ_price = models.IntegerField(verbose_name="목표가격")
    sell_price = models.IntegerField(verbose_name="손절가격")
    reval_trm = models.IntegerField(verbose_name="리벨런싱 주기 ( 0:분기별 | 1:연간 | 2:선택안함 )")

    def __str__(self):
        return self.stret_name

    class Meta:
        db_table = "Stretagy"
        verbose_name = "Strategy"
        verbose_name_plural ="Stretagy"


class Result(models.Model):
    
    objects = models.Manager()
    # 기본 항목
    stretagy_result = models.ForeignKey('Stretagy', to_field="stret_num", on_delete=models.CASCADE, verbose_name="전략 고유번호당 결과")
    writer_name = models.ForeignKey('User',to_field="username", on_delete=models.CASCADE, verbose_name="전략 작성자명")

    # 결과 항목
    profit_all = models.IntegerField(verbose_name="총 손익")
    currentAsset = models.IntegerField(verbose_name="현재자산")
    cagr = models.IntegerField(verbose_name="누적수익률") 
    m_cagr = models.IntegerField(verbose_name="월간수익률")

    def __str__(self):
        return str(self.stretagy_result)

    class Meta:
        db_table = "Results"
        verbose_name = "result"
        verbose_name_plural ="Results"
