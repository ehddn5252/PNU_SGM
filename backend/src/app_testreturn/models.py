from django.db import models

# Create your models here.

class TestReturn(models.Model):
    objects = models.Manager()
    user_name = models.ForeignKey('app_users.Users', on_delete=models.CASCADE, verbose_name='사용자명') # 유저명
    stra_name = models.CharField(max_length=128, verbose_name='전략명') # 전략명
    principal = models.IntegerField(verbose_name="투자 원금") # 투자원금
    profit = models.IntegerField(verbose_name="손익") # 손익
    curr_asset = models.IntegerField(verbose_name="현재 자산") # 현재 자산
    # CAGR = models.IntegerField(verbose_name="누적 수익률") # 누적 수익률 (CAGR)
    # CAGR_by_month = models.IntegerField(verbose_name="월간 수익률") # 월간 수익률
    # registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        """A string representation of the model."""
        return self.stra_name

    class Meta:
        db_table = '유저,전략별 리턴 파라미터'
        verbose_name = '리턴값'
        verbose_name_plural = "리턴값" 