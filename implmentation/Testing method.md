# proportion Test

$Z=\frac{\left(\hat{p}_{1}-\hat{p}_{2}\right)-0}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_{1}}+\frac{1}{n_{2}}\right)}}$

- 위 공식에서 아래 공식으로 바꾸는것이 필요할 수 있음!

$Z=\frac{\left(\hat{p}_{1}-\hat{p}_{2}\right)-0}{\sqrt{\frac{\hat{p}_{1}\left(1-\hat{p}_{1}\right)}{n_{1}}+\frac{\hat{p}_{2}\left(1-\hat{p}_{2}\right)}{n_{2}}}}$

- Z 만 바꾸고 , 나머지는 그대로 하면 될것..

## Note : Confidence interval

- Confidence interval for two independent proportions The $(1-\alpha) 100 \%$ confidence interval of $p_{1}-p_{2}$ is given by:

$$
\hat{p}_{1}-\hat{p}_{2} \pm z_{\alpha / 2} \sqrt{\frac{\hat{p}_{1}\left(1-\hat{p}_{1}\right)}{n_{1}}+\frac{\hat{p}_{2}\left(1-\hat{p}_{2}\right)}{n_{2}}}
$$

```python
import scipy.stats
import numpy as np 
def unpooled_twosample_prop(X_a,X_b,N_a,N_b,alpha) :
    P_a = X_a / N_a
    P_b = X_b / N_b
    SE = np.sqrt(P_a*(1-P_a) / N_a + P_b*(1-P_b) / N_b)
    Z = (P_b - P_a) / SE
    p_val = 2*scipy.stats.norm.cdf(-1*abs(Z))
    z_a = scipy.stats.norm.ppf(1 - alpha/2)
    CI = [(P_b-P_a) - z_a*SE , (P_b-P_a) + z_a*SE]
    print(f'Z Statistics : {Z}')
    print(f'p value : {p_val}')
    print(f'CI : {CI}')
```

```
>> pooled_twosample_prop(200,230,950,950,0.05)
Z Statistics : 1.6447699394666537 
p value : 0.10001726351282186 
CI : [-0.006051603887799802, 0.06920949862464193]
```

- 위와 같은 테스트를 수행해야 합니다.

# Mean Testing

$Z= \frac{(\bar{X}-\bar{Y})-\left(\mu_{X}-\mu_{Y}\right)}{\sqrt{\frac{S_{X}^{2}}{n}+\frac{S_{Y}^{2}}{m}}}$

- 위처럼 Z 통계량이 정의됩니다. 즉 계산은 다음과 같이 수행됩니다. 

$ ((\bar{X_A} - \bar{X_B}) -z_{k/2} {\sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}}} \ , \  (\bar{X_A} - \bar{X_B})+ z_{k/2} {\sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}}} )$

```python
import scipy.stats
import numpy as np 
def twosample_mean(A,B,alpha) :
    mean_A = np.mean(A)
    mean_B = np.mean(B)
    std_A = np.std(A)
    std_B = np.std(B)
    SE = np.sqrt(std_A**2/len(A) + std_B**2/len(B))
    Z = (mean_B - mean_A) / SE
    p_val = 2*scipy.stats.norm.cdf(-1*abs(Z))
    z_a = scipy.stats.norm.ppf(1 - alpha/2)
    CI = [(mean_B-mean_A) - z_a*SE , (mean_B-mean_A) + z_a*SE]
    print(f'Z Statistics : {Z}')
    print(f'p value : {p_val}')
    print(f'CI : {CI}')
```

