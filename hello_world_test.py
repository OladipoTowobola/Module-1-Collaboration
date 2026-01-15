# hello_world.py
# A simple Python program to print "Hello, World!"

def main():
    try:
        print("Hello, World!")  # Output message
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program only if executed directly
if __name__ == "__main__":
    main()
