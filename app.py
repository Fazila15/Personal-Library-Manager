import streamlit as st
import base64

# Function to encode image in base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Encode background image
bg_image = get_base64_image("images/bg-image.jpg")

# Apply Background
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url({bg_image});
            background-size: cover;
            background-position: center;
            font-family: 'Poppins', sans-serif;
            color: black;
        }}
        .container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 40px;  
            padding: 40px;
        }}
        .card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
            width: 280px;
            height: 380px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s;
            color: black;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        }}
        .card h3 {{
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
            color: black;
        }}
        .card p {{
            font-size: 16px;
            opacity: 0.8;
            margin-bottom: 15px;
            color: black;
        }}
        .card:hover h3, .card:hover p {{
            color: white; 
        }}
        .button-container {{
            display: flex;
            justify-content: center;
            margin-top: auto;
        }}
        .stButton > button {{
            background-color: #0072ff !important;
            color: white !important;
            font-weight: bold !important;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s ease-in-out, transform 0.2s;
            width: 50%;
        }}
        .stButton > button:hover {{
            background-color: #0057cc !important;
            transform: scale(1.05);
            color: black !important;
        }}
       .form-container {{
            text-align: center;
            margin-top: 20px;
        }}
       .form-heading {{
            font-size: 26px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
 </style>
""", unsafe_allow_html=True)

st.title("📚 Personal Library Manager")
st.markdown("### Manage your books efficiently with an interactive UI.")

# Define card options
options = [
    ("📖 Add Book", "Add new books to your personal library."),
    ("❌ Remove Book", "Remove books from your library."),
    ("🔍 Search Book", "Search for books quickly."),
    ("📚 View Library", "View and manage your library."),
]

# Layout for cards
cols = st.columns([1, 0.1, 1])
selected_option = None

for i, (title, description) in enumerate(options):
    col_index = i % 2 * 2  
    with cols[col_index]:
        st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
                <div class="button-container">
        """, unsafe_allow_html=True)
        
        if st.button(f"{title}", key=f"btn_{title}"):
            selected_option = title  
        
        st.markdown("""</div></div>""", unsafe_allow_html=True)

if selected_option:
    with st.container():
        st.markdown(f"""
            <div class="form-container">
                <h3 class="form-heading">{selected_option}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        if selected_option == "📖 Add Book":
            st.text_input("Book Title")
            st.text_input("Author Name")
            st.text_area("Book Description")
            st.file_uploader("Upload Book Cover Image")
            st.button("Add Book")
        elif selected_option == "❌ Remove Book":
            st.text_input("Enter Book Title to Remove")
            st.button("Remove Book")
        elif selected_option == "🔍 Search Book":
            st.text_input("Search by Title")
            st.text_input("Search by Author")
            st.button("Search Book")
        elif selected_option == "📚 View Library":
            st.button("View All Books")
            st.button("Sort by Title")
            st.button("Sort by Author")
            st.button("Filter by Genre")

