import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
# 연도
years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023])

# 연도별 강수량 데이터 (단위: mm) - 서울 강수량
rainfall_mm = np.array([1233, 1284, 891, 1651, 1286, 1775, 1598])  # 참고용

# 연도별 수력발전량 데이터 (단위: 천 toe)
hydro_power = np.array(
    [600.69, 718.787, 594.539, 826.344, 651.227, 755.117, 791.963])

# 그래프 설정
bar_width = 0.35
index = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 수력발전량 - 왼쪽 Y축
bar1 = ax1.bar(index - bar_width/2, hydro_power, bar_width,
               label='수력발전량 (천 toe)', color='skyblue')
ax1.set_ylabel('수력발전량 (천 toe)', color='skyblue')
ax1.set_xlabel('연도')
ax1.set_xticks(index)
ax1.set_xticklabels(years)
ax1.tick_params(axis='y', labelcolor='skyblue')

# 강수량 - 오른쪽 Y축
ax2 = ax1.twinx()
bar2 = ax2.bar(index + bar_width/2, rainfall_mm,
               bar_width, label='강수량 (mm)', color='orange')
ax2.set_ylabel('강수량 (mm)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 범례
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))

plt.title('최근 7년간 연도별 수력발전량과 강수량 변화')
plt.tight_layout()
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()
