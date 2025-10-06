import streamlit as st
import time
from streamlit.runtime.scriptrunner import RerunException, get_script_run_ctx

# ----------------- Rerun Function -----------------
def rerun_app():
    ctx = get_script_run_ctx()
    if ctx is None:
        st.error("Cannot rerun app outside Streamlit context")
        return
    raise RerunException(ctx)

# ----------------- Default Pets with Action GIFs -----------------
default_pets = {
    "Dog": {
        "idle": "https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif",
        "feed": "https://media.giphy.com/media/l2Sqir5K8mMOkhDWw/giphy.gif",
        "play": "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
        "clean": "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif"
    },
    "Cat": {
        "idle": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "feed": "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
        "play": "https://media.giphy.com/media/12PA1eI8FBqEBa/giphy.gif",
        "clean": "https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif"
    },
    "Bunny": {
        "idle": "https://media.giphy.com/media/3o6ZsW3sQ0LWZ5V1aU/giphy.gif",
        "feed": "https://media.giphy.com/media/3oEduN6SO3Jk6dG6Gc/giphy.gif",
        "play": "https://media.giphy.com/media/26gssIytJvy1b1THO/giphy.gif",
        "clean": "https://media.giphy.com/media/3o6MbhRTNTF7W7h7he/giphy.gif"
    }
}

# ----------------- Initialize Session State -----------------
if "pets" not in st.session_state:
    st.session_state.pets = default_pets.copy()

if "selected_pet" not in st.session_state:
    st.session_state.selected_pet = list(st.session_state.pets.keys())[0]

if "pet_stats" not in st.session_state:
    st.session_state.pet_stats = {}
    for pet in st.session_state.pets:
        st.session_state.pet_stats[pet] = {"hunger": 50, "happiness": 50, "status": "Happy"}

if "pet_action" not in st.session_state:
    st.session_state.pet_action = "idle"

# ----------------- Page Setup -----------------
st.set_page_config(page_title="Virtual Pet Game 🐾", layout="centered")
st.title("🐾 Virtual Pet Game")

# ----------------- Pet Selection -----------------
st.subheader("Select Your Pet")
selected = st.selectbox(
    "Choose a pet:",
    list(st.session_state.pets.keys()),
    index=list(st.session_state.pets.keys()).index(st.session_state.selected_pet)
)
st.session_state.selected_pet = selected

pet = st.session_state.selected_pet
stats = st.session_state.pet_stats[pet]

# ----------------- Display Pet -----------------
st.image(st.session_state.pets[pet][st.session_state.pet_action], width=250)
st.write(f"**Mood:** {stats['status']}")
st.write(f"**Hunger:** {stats['hunger']}/100")
st.write(f"**Happiness:** {stats['happiness']}/100")

# ----------------- Actions -----------------
st.subheader("Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Feed 🍲", key=f"feed_{pet}"):
        stats["hunger"] = max(stats["hunger"] - 20, 0)
        stats["happiness"] = min(stats["happiness"] + 5, 100)
        stats["status"] = "Full" if stats["hunger"] < 30 else "Content"
        st.session_state.pet_action = "feed"
        rerun_app()

with col2:
    if st.button("Play 🎾", key=f"play_{pet}"):
        stats["happiness"] = min(stats["happiness"] + 20, 100)
        stats["hunger"] = min(stats["hunger"] + 10, 100)
        stats["status"] = "Excited" if stats["happiness"] > 70 else "Happy"
        st.session_state.pet_action = "play"
        rerun_app()

with col3:
    if st.button("Clean 🛁", key=f"clean_{pet}"):
        stats["happiness"] = min(stats["happiness"] + 10, 100)
        stats["status"] = "Clean" if stats["happiness"] > 50 else "Happy"
        st.session_state.pet_action = "clean"
        rerun_app()

# ----------------- Reset & Delete Pet -----------------
st.subheader("Game Controls")
colA, colB = st.columns(2)

with colA:
    if st.button("Reset Pet 🔄", key=f"reset_{pet}"):
        stats["hunger"] = 50
        stats["happiness"] = 50
        stats["status"] = "Happy"
        st.session_state.pet_action = "idle"
        rerun_app()

with colB:
    if st.button("Delete Pet ❌", key=f"delete_{pet}"):
        if len(st.session_state.pets) > 1:  # prevent deleting last pet
            del st.session_state.pets[pet]
            del st.session_state.pet_stats[pet]
            st.session_state.selected_pet = list(st.session_state.pets.keys())[0]
            st.session_state.pet_action = "idle"
            rerun_app()
        else:
            st.warning("You must have at least one pet!")

# ----------------- Mood Feedback -----------------
st.subheader("Pet Mood Feedback")
if stats["hunger"] > 70:
    st.warning(f"{pet} is very hungry! 🍽️")
elif stats["hunger"] > 40:
    st.info(f"{pet} is a little hungry.")

if stats["happiness"] < 30:
    st.error(f"{pet} is sad! 😢 Play with it!")
elif stats["happiness"] > 80:
    st.success(f"{pet} is super happy! 😄")

# ----------------- Add New Pet -----------------
st.subheader("Add a New Pet 🐾")
with st.form("add_pet_form", clear_on_submit=True):
    new_pet_name = st.text_input("Pet Name")
    new_pet_image_idle = st.text_input("Idle Image URL (GIF or PNG)")
    new_pet_image_feed = st.text_input("Feed Image URL (GIF or PNG)")
    new_pet_image_play = st.text_input("Play Image URL (GIF or PNG)")
    new_pet_image_clean = st.text_input("Clean Image URL (GIF or PNG)")
    submitted = st.form_submit_button("Add Pet ➕")
    if submitted:
        if new_pet_name and new_pet_image_idle:
            if new_pet_name not in st.session_state.pets:
                st.session_state.pets[new_pet_name] = {
                    "idle": new_pet_image_idle,
                    "feed": new_pet_image_feed or new_pet_image_idle,
                    "play": new_pet_image_play or new_pet_image_idle,
                    "clean": new_pet_image_clean or new_pet_image_idle
                }
                st.session_state.pet_stats[new_pet_name] = {"hunger": 50, "happiness": 50, "status": "Happy"}
                st.session_state.selected_pet = new_pet_name
                st.session_state.pet_action = "idle"
                rerun_app()
            else:
                st.warning("A pet with this name already exists!")

# ----------------- Auto Reset Pet Action -----------------
# After showing an action once, reset to idle
if st.session_state.pet_action != "idle":
    time.sleep(2)  # show action GIF for 2 seconds
    st.session_state.pet_action = "idle"
    rerun_app()

# ----------------- Footer -----------------
st.write("---")
st.write("Made with ❤️ using Streamlit")
