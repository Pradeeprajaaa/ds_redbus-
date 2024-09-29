from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Kerala_link_route(path):   
    LINKS_KERALA = []
    ROUTE_KERALA = []
    
    for i in range(1, 3):  # Set pagination limit to 2 for demonstration
        paths = driver.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if link is not None
                LINKS_KERALA.append(d)
            
        for route in paths:
            ROUTE_KERALA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the button with JavaScript as a fallback if it's intercepted
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
        except TimeoutException:
            print(f"Timeout while waiting for pagination at step {i}")
            break
    
    return LINKS_KERALA, ROUTE_KERALA

# Call the function to get bus route links and names
LINKS_KERALA, ROUTE_KERALA = Kerala_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_k = pd.DataFrame({"Route_name": ROUTE_KERALA, "Route_link": LINKS_KERALA})

# Specify the path to save the CSV
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_k.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_k.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_k)

# Close the browser
driver.quit()

# Open the browser
driver_A = webdriver.Chrome()

# Load the webpage
driver_A.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_A.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_A, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Andhra_link_route(path):   
    LINKS_ANDHRA = []
    ROUTE_ANDHRA = []
    
    # Retrieve route links and names across pagination
    for i in range(1, 5):  # Set pagination limit to 4
        paths = driver_A.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if link is not None
                LINKS_ANDHRA.append(d)
            
        for route in paths:
            ROUTE_ANDHRA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_A, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the button with JavaScript as a fallback if it's intercepted
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_A, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
        except TimeoutException:
            print(f"Timeout while waiting for pagination at step {i}")
            break
    
    return LINKS_ANDHRA, ROUTE_ANDHRA

# Call the function to get bus route links and names
LINKS_ANDHRA, ROUTE_ANDHRA = Andhra_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_A = pd.DataFrame({"Route_name": ROUTE_ANDHRA, "Route_link": LINKS_ANDHRA})

# Specify the path to save the CSV
path = r"C:\Users\ADMIN\Documents\10 state\df_andhra.csv"  # Use a different filename for Andhra routes

# Ensure the directory exists before saving the file
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_A.to_csv(path, index=False)

# Print the DataFrame for confirmation
print(df_A)

# Close the browser
driver_A.quit()
# Open the browser
driver_T = webdriver.Chrome()

# Load the webpage
driver_T.get("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_T.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_T, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Telangana_link_route(path):   
    LINKS_TELANGANA = []
    ROUTE_TELANGANA = []
    
    # Loop through pagination (set limit to 3 pages for this example)
    for i in range(1, 4):
        paths = driver_T.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_TELANGANA.append(d)
            
        for route in paths:
            ROUTE_TELANGANA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_T, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_T, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
        except TimeoutException:
            print(f"Timeout while waiting for pagination at step {i}")
            break
    
    return LINKS_TELANGANA, ROUTE_TELANGANA

# Call the function to get bus route links and names
LINKS_TELANGANA, ROUTE_TELANGANA = Telangana_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_T = pd.DataFrame({"Route_name": ROUTE_TELANGANA, "Route_link": LINKS_TELANGANA})

# Specify the path to save the CSV (update the file name)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_telangana.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_T.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_T)

# Close the browser
driver_T.quit()
# Open the browser
driver_G = webdriver.Chrome()

# Load the webpage
driver_G.get("https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_G.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_G, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Kadamba_link_route(path):   
    LINKS_KADAMBA = []
    ROUTE_KADAMBA = []
    
    # Loop through pagination (set limit to 3 pages for this example)
    for i in range(1, 4):
        paths = driver_G.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_KADAMBA.append(d)
            
        for route in paths:
            ROUTE_KADAMBA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_G, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_G, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_KADAMBA, ROUTE_KADAMBA

# Call the function to get bus route links and names
LINKS_KADAMBA, ROUTE_KADAMBA = Kadamba_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_G = pd.DataFrame({"Route_name": ROUTE_KADAMBA, "Route_link": LINKS_KADAMBA})

# Specify the path to save the CSV
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_kadamba.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_G.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_G)

# Close the browser
driver_G.quit()
# Open the browser
driver_R = webdriver.Chrome()

# Load the webpage
driver_R.get("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_R.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_R, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Rajastan_link_route(path):   
    LINKS_RAJASTAN = []
    ROUTE_RAJASTAN = []
    
    # Loop through pagination (set limit to 3 pages for this example)
    for i in range(1, 4):
        paths = driver_R.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_RAJASTAN.append(d)
            
        for route in paths:
            ROUTE_RAJASTAN.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_R, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_R, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_RAJASTAN, ROUTE_RAJASTAN

# Call the function to get bus route links and names
LINKS_RAJASTAN, ROUTE_RAJASTAN = Rajastan_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_R = pd.DataFrame({"Route_name": ROUTE_RAJASTAN, "Route_link": LINKS_RAJASTAN})

# Specify the path to save the CSV (corrected for Rajasthan)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_rajasthan.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_R.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_R)

# Close the browser
driver_R.quit()
# Open the browser
driver_SB = webdriver.Chrome()

# Load the webpage
driver_SB.get("https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_SB.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_SB, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Southbengal_link_route(path):   
    LINKS_SOUTHBENGAL = []
    ROUTE_SOUTHBENGAL = []
    
    # Loop through pagination (set limit to 5 pages for this example)
    for i in range(1, 6):
        paths = driver_SB.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_SOUTHBENGAL.append(d)
            
        for route in paths:
            ROUTE_SOUTHBENGAL.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_SB, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_SB, next_button)
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_SOUTHBENGAL, ROUTE_SOUTHBENGAL

# Call the function to get bus route links and names
LINKS_SOUTHBENGAL, ROUTE_SOUTHBENGAL = Southbengal_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_SB = pd.DataFrame({"Route_name": ROUTE_SOUTHBENGAL, "Route_link": LINKS_SOUTHBENGAL})

# Specify the path to save the CSV (corrected for South Bengal)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_southbengal.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_SB.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_SB)

# Close the browser
driver_SB.quit()
# Open the browser
driver_H = webdriver.Chrome()

# Load the webpage
driver_H.get("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_H.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_H, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names
def Haryana_link_route(path):   
    LINKS_HARYANA = []
    ROUTE_HARYANA = []
    
    # Loop through pagination (set limit to 5 pages for this example)
    for i in range(1, 6):
        paths = driver_H.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_HARYANA.append(d)
        
        for route in paths:
            ROUTE_HARYANA.append(route.text)
        
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_H, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_H, next_button)
        
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_HARYANA, ROUTE_HARYANA

# Call the function to get bus route links and names
LINKS_HARYANA, ROUTE_HARYANA = Haryana_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_H = pd.DataFrame({"Route_name": ROUTE_HARYANA, "Route_link": LINKS_HARYANA})

# Specify the path to save the CSV (corrected for Haryana)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_haryana.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_H.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_H)

# Close the browser
driver_H.quit()
# Open the browser
driver_AS = webdriver.Chrome()

# Load the webpage
driver_AS.get("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_AS.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_AS, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names for Assam
def Assam_link_route(path):   
    LINKS_ASSAM = []
    ROUTE_ASSAM = []
    
    # Loop through pagination (set limit to 5 pages for this example)
    for i in range(1, 5):
        paths = driver_AS.find_elements(By.XPATH, path)
        
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_ASSAM.append(d)
        
        for route in paths:
            ROUTE_ASSAM.append(route.text)
        
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_AS, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_AS, next_button)
        
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_ASSAM, ROUTE_ASSAM

# Call the function to get bus route links and names for Assam
LINKS_ASSAM, ROUTE_ASSAM = Assam_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_AS = pd.DataFrame({"Route_name": ROUTE_ASSAM, "Route_link": LINKS_ASSAM})

# Specify the path to save the CSV (corrected for Assam)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_assam.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_AS.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_AS)

# Close the browser
driver_AS.quit()
# Open the browser
driver_UP = webdriver.Chrome()

# Load the webpage
driver_UP.get("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_UP.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_UP, 20)

# Scroll to an element before clicking it
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# JavaScript click as a fallback method
def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Function to retrieve bus links and route names for Uttar Pradesh
def UP_link_route(path):   
    LINKS_UP = []
    ROUTE_UP = []
    
    # Loop through pagination (set limit to 5 pages for this example)
    for i in range(1, 6):
        paths = driver_UP.find_elements(By.XPATH, path)
        
        # Retrieve the route links
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_UP.append(d)
        
        # Retrieve the names of the routes
        for route in paths:
            ROUTE_UP.append(route.text)
        
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i+1}"]')
            
            # Scroll to the next button
            scroll_to_element(driver_UP, next_button)
            time.sleep(3)  # Give time for the page to load

            try:
                # Click the next button
                next_button.click()
            except ElementClickInterceptedException:
                print("Element click intercepted. Trying JavaScript click.")
                javascript_click(driver_UP, next_button)
        
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_UP, ROUTE_UP

# Call the function to get bus route links and names for Uttar Pradesh
LINKS_UP, ROUTE_UP = UP_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_UP = pd.DataFrame({"Route_name": ROUTE_UP, "Route_link": LINKS_UP})

# Specify the path to save the CSV (corrected for Uttar Pradesh)
csv_path = r"C:\Users\ADMIN\Documents\10 state\df_uttarpradesh.csv"

# Ensure the directory exists before saving the file
directory = os.path.dirname(csv_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the DataFrame as a CSV file
df_UP.to_csv(csv_path, index=False)

# Print the DataFrame for confirmation
print(df_UP)

# Close the browser
driver_UP.quit()
# Open the browser
driver_WB = webdriver.Chrome()

# Load the webpage
driver_WB.get("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile")
time.sleep(3)

# Maximize the browser window
driver_WB.maximize_window()

# WebDriverWait for element waiting
wait = WebDriverWait(driver_WB, 20)

# Function to retrieve bus links and route names for West Bengal
def Westbengal_link_route(path):   
    LINKS_WESTBENGAL = []
    ROUTE_WESTBENGAL = []
    
    # Loop through pagination (set limit to 5 pages for this example)
    for i in range(1, 6):
        paths = driver_WB.find_elements(By.XPATH, path)
        
        # Retrieve the route links
        for links in paths:
            d = links.get_attribute("href")
            if d:  # Check if the link is valid
                LINKS_WESTBENGAL.append(d)
        
        # Retrieve the names of the routes
        for route in paths:
            ROUTE_WESTBENGAL.append(route.text)
        
        try:
            # Wait for the pagination element to be present and scroll into view
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            
            # Scroll to the next button and wait until it's clickable
            driver_WB.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(2)  # Give it a bit of time to settle
            
            # Wait until the element is clickable
            wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')))
            
            # Try clicking the next button, handle any intercepted exception
            try:
                next_button.click()
            except ElementClickInterceptedException:
                print(f"Click intercepted at page {i}, attempting scroll and retry...")
                driver_WB.execute_script("arguments[0].scrollIntoView();", next_button)
                time.sleep(2)
                next_button.click()
        
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    
    return LINKS_WESTBENGAL, ROUTE_WESTBENGAL

# Call the function to get bus route links and names for West Bengal
LINKS_WESTBENGAL, ROUTE_WESTBENGAL = Westbengal_link_route("//a[@class='route']")

# Create a DataFrame to store the route names and links
df_WB = pd.DataFrame({"Route_name": ROUTE_WESTBENGAL, "Route_link": LINKS_WESTBENGAL})

# Save the DataFrame as a CSV file for West Bengal
path_WB = r"C:\Users\ADMIN\Documents\10 state\df_westbengal.csv"
df_WB.to_csv(path_WB, index=False)

# Assuming df_k, df_A, df_T, df_G, df_R, df_H, df_SB, df_AS, df_UP are pre-loaded DataFrames for each state
# Concatenate all the bus route DataFrames into one
df_final = pd.concat([df_k, df_A, df_T, df_G, df_R, df_H, df_SB, df_AS, df_UP, df_WB], ignore_index=True)

# Save the final concatenated DataFrame as a CSV
final_path = r"C:\Users\ADMIN\Documents\10 state\df_all_routes.csv"
df_final.to_csv(final_path, index=False)

# Print the final DataFrame for confirmation
print(df_final)

# Close the browser
driver_WB.quit()
