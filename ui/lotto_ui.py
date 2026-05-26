import streamlit as st


def get_ball_color(number):

    if 1 <= number <= 10:

        return "#fbc400"

    elif 11 <= number <= 20:

        return "#69c8f2"

    elif 21 <= number <= 30:

        return "#ff7272"

    elif 31 <= number <= 40:

        return "#aaaaaa"

    else:

        return "#b0d840"


def lotto_balls(numbers):

    balls_html = ""

    for num in numbers:

        color = get_ball_color(num)

        balls_html += f"""
        <div
            style="
                width:72px;
                height:72px;
                border-radius:50%;
                background:{color};
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:28px;
                font-weight:bold;
                color:white;
                margin:10px;
                box-shadow:
                    0 4px 10px rgba(0,0,0,0.25);
                border:3px solid rgba(255,255,255,0.7);
            "
        >
            {num}
        </div>
        """

    st.markdown(
        f"""
        <div
            style="
                width:100%;
                display:flex;
                justify-content:center;
                align-items:center;
                flex-wrap:wrap;
                margin-top:20px;
                margin-bottom:20px;
            "
        >
            {balls_html}
        </div>
        """,
        unsafe_allow_html=True
    )