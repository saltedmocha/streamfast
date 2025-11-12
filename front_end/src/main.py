from pathlib import Path
import streamlit as st

# Find and assign to dict automatically
pages_dict = {
    f"page {index}": str(page)
    for index, page in enumerate(
        Path(__file__).resolve().parent.glob("pages/*page*.py"), start=1
    )
}

main_page = st.Page(page=pages_dict["page 1"], title="Main page")
page_two = st.Page(page=pages_dict["page 2"], title="Page 2")
page_nav = st.navigation([main_page, page_two])

if __name__ == "__main__":
    page_nav.run()
