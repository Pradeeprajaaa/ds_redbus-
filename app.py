import streamlit as st
import mysql.connector
import pandas as pd
import time  # Import time for simulating a delay

# Connect to MySQL database using mysql-connector
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bby dragon',  # Replace with your actual password
        database='redbus_travel'
    )

# Function to fetch route names from a specific state table
def fetch_route_names(connection, state):
    query = f"SELECT DISTINCT Route_name FROM {state}_routes ORDER BY Route_name"
    route_names = pd.read_sql(query, connection)['Route_name'].tolist()
    return route_names

# Function to fetch data from the project_info table based on selected ROUTE_NAME
def fetch_data(connection, route_name):
    query = """
    SELECT Bus_name, Bus_type, Price, Ratings, Seats_Available, 
           Start_Time, End_Time, Total_Duration 
    FROM project_info 
    WHERE Route_name = %s
    """
    df = pd.read_sql(query, connection, params=(route_name,))
    return df

# Function to filter data based on RATING and BUS_TYPE
def filter_data(df, rating_range, bus_types):
    filtered_df = df[(df['Ratings'] >= rating_range[0]) & 
                     (df['Ratings'] <= rating_range[1]) & 
                     df['Bus_type'].isin(bus_types)]
    return filtered_df

# Main Streamlit app
def main():
    st.title('Redbus Booking System')

    connection = get_connection()

    try:
        # Step 1: Select State, Route, Rating Slider, and Bus Type
        step1 = st.expander("Step 1: Select Travel Details", expanded=True)

        with step1:
            st.write("### Select State and Route")

            states = ['kerala', 'andhra', 'telangana', 'kadamba', 'rajasthan', 
                      'southbengal', 'haryana', 'assam', 'uttarpradesh', 'westbengal']
            selected_state = st.selectbox('Select State', states)

            if selected_state:
                route_names = fetch_route_names(connection, selected_state)
                selected_route = st.selectbox('Select Route Name', route_names)

            rating_range = st.slider('Select Rating Range', 1, 5, (3, 5))

            if selected_route:
                data = fetch_data(connection, selected_route)
                bus_types = data['Bus_type'].unique().tolist()
                selected_bus_types = st.multiselect('Select Bus Type', bus_types)

        # Step 2: Select Booking Date, Pricing and Seats
        step2 = st.expander("Step 2: Select Booking Details", expanded=True)

        with step2:
            if selected_route and selected_bus_types:
                st.write("### Filter Tickets by Price")

                filtered_data = filter_data(data, rating_range, selected_bus_types)
                if not filtered_data.empty:
                    min_price = int(filtered_data['Price'].min())
                    max_price = int(filtered_data['Price'].max())

                    # Manual price range input
                    manual_min_price = st.number_input('Minimum Price', min_value=0, value=min_price)
                    manual_max_price = st.number_input('Maximum Price', min_value=manual_min_price, value=max(max_price, manual_min_price))

                    filtered_by_price = filtered_data[(filtered_data['Price'] >= manual_min_price) & 
                                                       (filtered_data['Price'] <= manual_max_price)]

                    available_seats = filtered_by_price['Seats_Available'].sum()

                    if available_seats > 0:
                        # Booking Date Selection
                        booking_date = st.date_input("Select Booking Date", min_value=pd.to_datetime("today"))

                        num_seats = st.number_input('Select Number of Seats', min_value=1, max_value=available_seats)
                        price_per_seat = filtered_by_price['Price'].mean()  # Average price for selected buses
                        total_price = num_seats * price_per_seat

                        st.write(f"Price per seat: ₹{price_per_seat:.2f}")
                        st.write(f"Total price for {num_seats} seats: ₹{total_price:.2f}")

                        # Show bus details if a bus type is selected
                        if selected_bus_types:
                            bus_details = data[data['Bus_type'].isin(selected_bus_types)]
                            if not bus_details.empty:
                                st.write("### Bus Details")
                                # Define the columns to show
                                columns_to_display = ['Bus_name', 'Bus_type', 'Price', 'Ratings', 'Seats_Available', 
                                                      'Start_Time', 'End_Time', 'Total_Duration']

                                st.dataframe(bus_details[columns_to_display])
                            else:
                                st.warning("No bus details available for the selected bus types.")

                        # "Book Now" button
                        if st.button('Book Now'):
                            with st.spinner('Processing your booking...'):
                                # Simulate a delay for the booking process
                                time.sleep(3)  # Simulate processing time

                            # After processing, show success message with a checkmark emoji
                            st.success(f"✅ Successfully booked {num_seats} seats for {selected_route} on {booking_date} at ₹{total_price:.2f}")

                            # Simulate animation
                            for i in range(5):  # Simulate 5 steps
                                st.write("🎉 Booking in progress..." + "🚀" * (i + 1))
                                time.sleep(0.5)  # Pause to simulate animation
                                st.empty()  # Clear previous message

                    else:
                        st.warning("No seats available for the selected filters.")
                else:
                    st.write("No buses available for the selected filters.")

        # Terms and Conditions section
        st.expander("Terms and Conditions", expanded=False).markdown("""
        - All bookings are subject to availability.
        - Cancellation policies apply as per the bus operator.
        - Ensure to carry a valid ID proof while traveling.
        - The management holds the right to change the schedule without prior notice.
        - Please check the terms and conditions of the bus operator before booking.
        """)

        # FAQ section
        st.expander("Frequently Asked Questions (FAQ)", expanded=False).markdown("""
        *Q1: How can I cancel my booking?*
        A1: You can cancel your booking by visiting the 'My Bookings' section on our website.

        *Q2: How will I receive my ticket?*
        A2: Your ticket will be emailed to you after booking. You can also download it from the 'My Bookings' section.

        *Q3: What should I do if my bus is late?*
        A3: In case of a delay, please contact the bus operator's customer service.

        *Q4: Can I change my travel date?*
        A4: Yes, you can modify your booking by contacting customer support within the stipulated time frame.
        """)

    finally:
        connection.close()

if __name__ == "__main__":
    main()
