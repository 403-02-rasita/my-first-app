import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")


# ====================================================
# จุดที่ 1: กำหนดค่าเริ่มต้นใน session_state
# ====================================================
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# ====================================================
# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
# ====================================================
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ====================================================
# จุดที่ 2-5 และ 8: ฟังก์ชันแสดงผล Dialog
# ====================================================
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()
    score = 0

    # ====================================================
    # จุดที่ 3: สรุปผลและแปลงคำตอบเป็นตัวพิมพ์เล็ก
    # ====================================================
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ====================================================
    # จุดที่ 4: เพิ่มการตรวจข้อ 3 และข้อ 4
    # ====================================================

    # ตรวจข้อ 3
    if u_ans3 == "blue":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "water":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ====================================================
    # จุดที่ 5: คะแนนเต็ม 4
    # ====================================================
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")

    # ====================================================
    # จุดที่ 8: แสดงคำตอบ ans3 และ ans4
    # ====================================================
    st.write(f"📝 คำตอบข้อ 3: {u_ans3}")
    st.write(f"📝 คำตอบข้อ 4: {u_ans4}")


# ====================================================
# 1. ปุ่มเริ่มเล่นเกม
# ====================================================
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# ====================================================
# 2. แถบแสดงเวลานับถอยหลัง
# ====================================================
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ====================================================
# 3. ช่องรับคำตอบ
# ====================================================

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)


# ====================================================
# จุดที่ 6: เพิ่มช่องรับคำตอบข้อ 3 และข้อ 4
# ====================================================

ans3 = st.text_input(
    "ข้อ 3: The sky is `b _ _ e`. ☁️",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "ข้อ 4: I drink `w _ t _ r` every day. 💧",
    value=st.session_state.ans4_val,
)


# ====================================================
# จุดที่ 7: อัปเดตค่าล่าสุดเข้า session_state
# ====================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ====================================================
# 4. ปุ่มส่งคำตอบ
# ====================================================
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


# ====================================================
# 5. แสดง Dialog ผลลัพธ์
# ====================================================
if st.session_state.get("is_ended", False):

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write("นางสาวรสิตา กุลณาวงค์ เลขที่ 2 ม.4/3")
