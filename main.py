import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("""
        <style>
            .stApp {
                background-color: #f5f0e6;  /* Lightest brown background */
            }
            .title-box {
                background-color: #5c4033;  /* Dark brown title box */
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                font-size: 2rem;
                margin-bottom: 1rem;
            }

        [data-testid="stSidebar"] {
            background-color: #a1866f;
        }

        
        .css-1d391kg, .css-h5rgaw {
            color: white !important;
        }ckground-color: #a1866f !important; 
        color: black !important;
    }
        </style>
    """, unsafe_allow_html=True)

# Initialize library in session state
if 'library' not in st.session_state:
    st.session_state.library = []

# Add a book
def add_book():
    st.header("📚 Add a new book")
    title = st.text_input("Enter the title of the book:")
    author = st.text_input("Enter the name of Author:")
    year = st.text_input("Enter the publication year:")
    genre = st.text_input("Enter the genre:")
    read = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        new_book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read
        }
        st.session_state.library.append(new_book)
        st.success(f"Book '{title}' added successfully!")

# Remove a book
def remove_book():
    st.header("🗑️ Remove A Book")
    titles = [book['title'] for book in st.session_state.library]
    if titles:
        book_to_remove = st.selectbox("Select a book to remove:", titles)

        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book['title'] != book_to_remove]
            st.success(f"✅ Book '{book_to_remove}' removed successfully!")
    else:
        st.info("Library is empty")

# Search for a book
def search_book():
    st.header("🔎 Search Library")
    search_by = st.selectbox("Search by:", ['title', 'author'])
    search_term = st.text_input(f"Enter the {search_by}:").lower()

    if st.button("Search"):
        results = [book for book in st.session_state.library if search_term in book[search_by].lower()]
        if results:
            for book in results:
                status = "Read" if book['read'] else "Unread"
                st.write(f"📖 {book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        else:
            st.info("No books found.")

# Display all books
def display_all_books():
    st.header("📚 All Books in Library")
    if st.session_state.library:
        for book in st.session_state.library:
            status = "Read" if book['read'] else "Unread"
            st.write(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        st.info("Library is empty.")

# Show statistics
def display_statistics():
    st.header("📊 Library Statistics")
    total_books = len(st.session_state.library)
    read_books = len([book for book in st.session_state.library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    st.write(f"📚 Total books: {total_books}")
    st.write(f"✅ Books read: {read_books}")
    st.write(f"📈 Percentage read: {percentage_read:.2f}%")

# Main function
def main():
    
    st.markdown("<div class='title-box'>📖 Personal Library Manager</div>", unsafe_allow_html=True)

    # Sidebar option menu
    with st.sidebar:
        choice = option_menu(
            "Main Menu",
            ["Add Book", "Remove Book", "Search", "Display All", "Statistics"],
            icons=["plus-square", "trash", "search", "book", "bar-chart"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical"
        )

    if choice == "Add Book":
        add_book()
    elif choice == "Remove Book":
        remove_book()
    elif choice == "Search":
        search_book()
    elif choice == "Display All":
        display_all_books()
    elif choice == "Statistics":
        display_statistics()

if __name__ == '__main__':
    main()
