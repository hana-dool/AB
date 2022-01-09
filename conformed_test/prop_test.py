"""
two sample proportion test 를 수행합니다.
"""

from scipy import stats
import numpy as np


class info:
    """실험 결과를 저장합니다.
    """

    def __init__(
        self,
        success_a: int,
        size_a: int,
        success_b: int,
        size_b: int,
        value: float,
        significance: float,
        alternative: str,
        prop_a: float,
        prop_b: float,
        z_statistics: float,
        p_value: float,
        confint: list,
    ):
        info.test_setting = {
            "success_a": success_a,
            "size_a": size_a,
            "sucess_b": success_b,
            "size_b": size_b,
            "vale": value,
            "significance": significance,
            "alternative": alternative,
        }
        info.test_results = {
            "prop_a": prop_a,
            "prop_b": prop_b,
            "z_statistics": z_statistics,
            "p_value": p_value,
            "confint": confint,
        }


def two_proprotions_test(
    success_a: int,
    size_a: int,
    success_b: int,
    size_b: int,
    value: float = 0,
    significance: float = 0.5,
    alternative: str = "two-sided",
):
    """ proportion 에 대해서 two sample independent proportion test 를 진행합니다.
    alternative 에 따라서 아래와 같이 테스트가 진행됩니다.
    - H0: prop_a - prop_b  = value
    - H1: prop_a - prop_b != value   if alternative = 'two-sided'
    - H1: prop_a - prop_b  > value   if alternative = 'larger'
    - H1: prop_a - prop_b  < value   if alternative = 'smaller'

    Parameters
    ----------
    success_a, success_b : 0<int
        각 그룹의 성공 수
    size_a, size_b : 0<int
        각 그룹의 총 샘플 수
    value : float
        테스트 하고자 하는 기본 값
    significant : 0<float<1
        유의수준 값
    alternative : {'two-sided', 'smaller', 'larger'}
        대립가설의 종류. 각각의 구체적인 수준은 위의 값을 참고하세요

    Returns
    -------
    info : calss
        다양한 실험 결과를 가지고 있는 클래스
        info.test_setting = {
            "success_a": success_a,
            "size_a": size_a,
            "sucess_b": success_b,
            "size_b": size_b,
            "vale": value,
            "significance": significance,
            "alternative": alternative,
        }
        info.test_results = {
            "prop_a": prop_a,
            "prop_b": prop_b,
            "z_statistics": z_statstics,
            "p_value": p_value,
            "confint": confint,
        }

    Examples
    --------
    실험의 결과로 다음과 같이 결과가 나왔다고 합시다.
    Control 의 전환, 샘플수 : (30,400) 
    Treatment 의 전환, 샘플 수 : (25,390)
    이에 따른 테스트는 아래와 같습니다.
    two_proprotions_test(30,400,25,390)

    Notes
    -----
    pooled variance 방법론은 쓰지 않았습니다.
    그 이유는 다음과 같습니다.
    - Confidence interval 과의 Alignment 되어야함
    - value 가 nonzero 일때에는 pooled variance 를 쓸 수 없음
    """

    # 기본 Statistic 계산
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    var = prop_a * (1 - prop_a) / size_a + prop_b * (1 - prop_b) / size_b
    se = np.sqrt(var)
    prop_diff = prop_a - prop_b

    # H_0 하에서는 prop_a - prop_b = value 이므로
    z_statistics = (prop_a - prop_b - value) / np.sqrt(var)
    if alternative == "two-sided":
        one_side = 1 - stats.norm(loc=0, scale=1).cdf(abs(z_statistics))
        p_value = one_side * 2
        # z critical value
        z = stats.norm(loc=0, scale=1).ppf(1 - significance / 2)

        # point-estimator +- z * standard-error
        confint = prop_diff + np.array([-1, 0, 1]) * z * se
    elif alternative == "larger":
        one_side = 1 - stats.norm(loc=0, scale=1).cdf(z_statistics)
        p_value = one_side
        z = stats.norm(loc=0, scale=1).ppf(1 - significance)
        confint = prop_diff + np.array([-np.inf, 0, 1]) * z * se

    elif alternative == "smaller":
        one_side = stats.norm(loc=0, scale=1).cdf(z_statistics)
        p_value = one_side
        z = stats.norm(loc=0, scale=1).ppf(1 - significance)
        confint = prop_diff + np.array([-1, 0, np.inf]) * z * se

    return info(
        success_a,
        size_a,
        success_b,
        size_b,
        value,
        significance,
        alternative,
        prop_a,
        prop_b,
        z_statistics,
        p_value,
        confint,
    )


if __name__ == "__main__":
    test = two_proprotions_test(30, 400, 25, 390, 0, 0.05, "smaller")
    print(test.test_setting)
    print(test.test_results)
