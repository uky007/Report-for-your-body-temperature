impourt numpy as np

body_temp = np.random.normal(loc=36.5, scale=0.33, size=1)[0]
print(f'今日報告する体温は{body_temp:.1f}℃です．')
