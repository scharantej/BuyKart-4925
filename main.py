
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Sample appointments for demonstration purposes
appointments = []

# Main page route
@app.route('/')
def index():
    return render_template('index.html')

# Appointment booking route
@app.route('/book', methods=['POST'])
def book():
    # Extract appointment details from the request form
    duration = request.form.get('duration')
    time = request.form.get('time')

    # Validate the appointment details
    if not (duration in ['15', '30', '60']):
        return render_template('index.html', error="Invalid appointment duration.")
    if not time:
        return render_template('index.html', error="Please select an appointment time.")

    # Create an appointment object
    appointment = {
        'duration': duration,
        'time': time
    }

    # Add the appointment to the sample data list
    appointments.append(appointment)

    # Redirect to the confirmation page
    return redirect(url_for('confirmation'))

# Confirmation page route
@app.route('/confirmation')
def confirmation():
    # Retrieve the most recent appointment from the sample data list
    appointment = appointments[-1]

    # Render the confirmation page with appointment details
    return render_template('confirmation.html', appointment=appointment)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
