## Input:

"Develop a scheduling app that lets users book time with me for 15-, 30-, or 60-minute appointments."

## Output:

"Design a web application that offers an appointment booking system for users. Enable scheduling of 15-, 30-, or 60-minute appointments and integrate necessary features for effective scheduling."

## Flask Application Design:

### HTML Files:

**index.html**:
- Main landing page of the application, providing an introduction and instructions for appointment booking.
- Includes a form for users to specify their preferred appointment duration and time slot.

### Routes:

**@app.route('/', methods=['GET', 'POST'])**
- Handles the main page, serving the index.html file.
- If a POST request is made (i.e., the form is submitted), it validates the user's input.
- Upon successful validation, it schedules the appointment and redirects the user to a confirmation page.

**@app.route('/confirmation')**
- Confirmation page displayed after a successful appointment booking.
- Contains details of the scheduled appointment, including time, duration, and any additional information.