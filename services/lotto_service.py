import re
import random

from collections import Counter


class LottoService:

    # =========================================================
    # 참고 분석 데이터
    # =========================================================

    REFERENCE_DATA = """
    3 7 11 18 21 34
    5 9 14 22 31 42
    1 7 15 19 28 44
    3 11 17 24 33 40
    6 9 12 27 35 41
    7 14 18 21 32 45
    2 8 15 26 37 43
    3 9 11 23 34 44
    5 12 19 28 33 41
    7 14 18 24 35 42
    1 9 15 21 32 45
    3 11 17 26 37 44
    6 12 19 23 34 40
    7 14 18 28 35 41
    2 9 15 24 33 42
    """

    # =========================================================
    # 텍스트 숫자 추출
    # =========================================================

    @staticmethod
    def extract_numbers_from_text(text):

        found = re.findall(
            r"\d+",
            str(text)
        )

        numbers = []

        for num in found:

            try:

                value = int(num)

                if 1 <= value <= 45:

                    numbers.append(value)

            except Exception:
                pass

        return list(set(numbers))

    # =========================================================
    # 참고 데이터 분석
    # =========================================================

    @staticmethod
    def analyze_reference_data():

        numbers = re.findall(
            r"\d+",
            LottoService.REFERENCE_DATA
        )

        parsed_numbers = []

        for num in numbers:

            try:

                value = int(num)

                if 1 <= value <= 45:

                    parsed_numbers.append(value)

            except Exception:
                pass

        return parsed_numbers

    # =========================================================
    # 가중치 후보 생성
    # =========================================================

    @staticmethod
    def build_weighted_candidates(
        reference_numbers,
        symbol_numbers
    ):

        counter = Counter(reference_numbers)

        weighted_pool = []

        for number, freq in counter.items():

            # 기본 가중치
            repeat_count = min(freq, 3)

            weighted_pool.extend(
                [number] * repeat_count
            )

            # 꿈/사주 연관 숫자 가산점
            if number in symbol_numbers:

                weighted_pool.extend(
                    [number] * 2
                )

        return weighted_pool, counter

    # =========================================================
    # 번호 추천
    # =========================================================

    @staticmethod
    def recommend_numbers(symbol_numbers):

        reference_numbers = (
            LottoService.analyze_reference_data()
        )

        weighted_pool, counter = (
            LottoService.build_weighted_candidates(
                reference_numbers,
                symbol_numbers
            )
        )

        selected_numbers = set()

        max_try = 1000
        try_count = 0

        # =====================================================
        # 가중 랜덤 추출
        # =====================================================

        while (
            len(selected_numbers) < 6
            and try_count < max_try
        ):

            number = random.choice(
                weighted_pool
            )

            selected_numbers.add(number)

            try_count += 1

        # =====================================================
        # 부족 시 보완
        # =====================================================

        while len(selected_numbers) < 6:

            selected_numbers.add(
                random.randint(1, 45)
            )

        final_numbers = sorted(
            list(selected_numbers)
        )

        reasons = (
            LottoService.generate_reasons(
                final_numbers,
                counter,
                symbol_numbers
            )
        )

        top_frequency = sorted(
            counter.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        top_numbers = [
            num
            for num, freq in top_frequency
        ]

        return {
            "numbers": final_numbers,
            "reasons": reasons,
            "top_numbers": top_numbers
        }

    # =========================================================
    # 추천 이유 생성
    # =========================================================

    @staticmethod
    def generate_reasons(
        numbers,
        counter,
        symbol_numbers
    ):

        reasons = {}

        for num in numbers:

            reason_parts = []

            freq = counter.get(num, 0)

            reason_parts.append(
                f"참고 데이터에서 {freq}회 등장"
            )

            if num in symbol_numbers:

                reason_parts.append(
                    "꿈/사주 분석 결과와 연관된 숫자"
                )

            else:

                reason_parts.append(
                    "가중 랜덤 분석을 통해 선정된 숫자"
                )

            # 번호대 해석
            if 1 <= num <= 10:

                reason_parts.append(
                    "초기운과 상승운 흐름"
                )

            elif 11 <= num <= 20:

                reason_parts.append(
                    "재물운과 기회운 강화"
                )

            elif 21 <= num <= 30:

                reason_parts.append(
                    "변화와 전환의 흐름"
                )

            elif 31 <= num <= 40:

                reason_parts.append(
                    "안정성과 장기운 흐름"
                )

            else:

                reason_parts.append(
                    "귀인운과 강한 행운 흐름"
                )

            reasons[num] = " / ".join(
                reason_parts
            )

        return reasons