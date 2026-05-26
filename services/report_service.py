import os
import io

from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle,
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)

from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus.flowables import HRFlowable

from core.logger import logger


# =========================================================
# 저장 폴더
# =========================================================

REPORT_DIR = os.path.join(
    "outputs",
    "reports"
)

os.makedirs(
    REPORT_DIR,
    exist_ok=True
)


# =========================================================
# 폰트 등록
# =========================================================

FONT_DIR = os.path.join(
    "assets",
    "fonts"
)

FONT_PATH = os.path.join(
    FONT_DIR,
    "NanumGothic.ttf"
)

pdfmetrics.registerFont(
    TTFont(
        "NanumGothic",
        FONT_PATH
    )
)


class ReportService:

    # =====================================================
    # PDF 생성
    # =====================================================

    @staticmethod
    def generate_pdf(data: dict):

        pdf_buffer = io.BytesIO()

        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40,
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            name="TitleStyle",
            parent=styles["Heading1"],
            fontName="NanumGothic",
            fontSize=24,
            leading=32,
            textColor=colors.HexColor("#6d28d9"),
            alignment=1,
            spaceAfter=20,
        )

        section_style = ParagraphStyle(
            name="SectionStyle",
            parent=styles["Heading2"],
            fontName="NanumGothic",
            fontSize=16,
            leading=24,
            textColor=colors.HexColor("#4c1d95"),
            spaceBefore=20,
            spaceAfter=10,
        )

        content_style = ParagraphStyle(
            name="ContentStyle",
            parent=styles["BodyText"],
            fontName="NanumGothic",
            fontSize=11,
            leading=22,
            textColor=colors.HexColor("#111827"),
        )

        lotto_style = ParagraphStyle(
            name="LottoStyle",
            parent=styles["BodyText"],
            fontName="NanumGothic",
            fontSize=20,
            leading=28,
            alignment=1,
            textColor=colors.white,
        )

        footer_style = ParagraphStyle(
            name="FooterStyle",
            parent=styles["BodyText"],
            fontName="NanumGothic",
            fontSize=9,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#6b7280"),
        )

        elements = []

        # =================================================
        # 타이틀
        # =================================================

        elements.append(
            Paragraph(
                "🔮 Mystic Dream Lotto",
                title_style
            )
        )

        elements.append(
            Paragraph(
                "AI 꿈 · 사주 · 로또 분석 리포트",
                content_style
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =================================================
        # 섹션 생성 함수
        # =================================================

        def add_section(title, content):

            elements.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#8b5cf6")
                )
            )

            elements.append(
                Spacer(1, 10)
            )

            elements.append(
                Paragraph(
                    title,
                    section_style
                )
            )

            elements.append(
                Paragraph(
                    str(content).replace(
                        "\n",
                        "<br/>"
                    ),
                    content_style
                )
            )

            elements.append(
                Spacer(1, 14)
            )

        # =================================================
        # 꿈 내용
        # =================================================

        add_section(
            "🌙 꿈 내용",
            data["dream_text"]
        )

        # =================================================
        # 사주 정보
        # =================================================

        saju_info = f"""
        출생일: {data["birth_date"]}<br/><br/>
        생시: {data["birth_time"] or "모름"}<br/><br/>
        성별: {data["gender"] or "미입력"}
        """

        add_section(
            "🪐 사주 정보",
            saju_info
        )

        # =================================================
        # 로또 번호
        # =================================================

        elements.append(
            Paragraph(
                "🎯 추천 로또 번호",
                section_style
            )
        )

        lotto_numbers = ", ".join(
            map(
                str,
                data["lotto_numbers"]
            )
        )

        lotto_table = Table(
            [[
                Paragraph(
                    lotto_numbers,
                    lotto_style
                )
            ]],
            colWidths=[450]
        )

        lotto_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#7c3aed")
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.HexColor("#7c3aed")
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    18
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    18
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    10
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    10
                ),
            ])
        )

        elements.append(
            lotto_table
        )

        elements.append(
            Spacer(1, 20)
        )

        # =================================================
        # 번호 추천 이유
        # =================================================

        elements.append(
            Paragraph(
                "🎲 번호 추천 이유",
                section_style
            )
        )

        for number, reason in data[
            "lotto_reasons"
        ].items():

            reason_table = Table(
                [[
                    Paragraph(
                        f"<b>{number}번</b><br/><br/>{reason}",
                        content_style
                    )
                ]],
                colWidths=[450]
            )

            reason_table.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        colors.white
                    ),
                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.HexColor("#ddd6fe")
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        14
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        14
                    ),
                ])
            )

            elements.append(
                reason_table
            )

            elements.append(
                Spacer(1, 10)
            )

        # =================================================
        # 분석 결과
        # =================================================

        add_section(
            "🌙 꿈 해몽 분석",
            data["dream_result"]
        )

        add_section(
            "🪐 사주 분석",
            data["saju_result"]
        )

        # =================================================
        # Footer
        # =================================================

        elements.append(
            Spacer(1, 30)
        )

        elements.append(
            Paragraph(
                f"""
                생성일시:
                {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                <br/><br/>
                Mystic Dream Lotto
                """,
                footer_style
            )
        )

        # =================================================
        # PDF 빌드
        # =================================================

        doc.build(elements)

        pdf_buffer.seek(0)

        return pdf_buffer

    # =====================================================
    # PDF 저장
    # =====================================================

    @staticmethod
    def save_report(data: dict):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filepath = os.path.join(
            REPORT_DIR,
            f"report_{timestamp}.pdf"
        )

        pdf_buffer = (
            ReportService.generate_pdf(
                data
            )
        )

        with open(filepath, "wb") as f:

            f.write(
                pdf_buffer.read()
            )

        logger.info(
            f"PDF 리포트 저장 완료: {filepath}"
        )

        return filepath