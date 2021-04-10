from abc import ABC

from IBMI import IBMI


def case_func(bmi: float):
    return {
        bmi < 18.5: 'Underweight',
        18.5 <= bmi < 25.0: 'Normal weight',
        25.0 <= bmi < 30.0: 'Overweight',
        30.0 <= bmi: 'Obesity'
    }[True]


class BMI(IBMI, ABC):

    def bmi(self, weight: float, height: float) -> float:
        super(BMI, self).bmi(weight, height)
        return weight / ((height / 100) ** 2)

    def print_bmi(self, bmi: float):
        super(BMI, self).print_bmi(bmi)
        print(case_func(bmi))


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    bodyIndex = BMI()
    bodyIndex.print_bmi(bodyIndex.bmi(arr[0], arr[1]))
