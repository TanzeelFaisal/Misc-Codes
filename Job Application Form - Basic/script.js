let applications = [];

function submitForm(event) {
    event.preventDefault();
    if (validateForm()) {
        processData();
    } else {
        alert('Please fill out all required fields correctly.');
    }
}

function validateForm() {
    let isValid = true;
    const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const phonePattern = /^\d{11}$/;

    const requiredFields = document.querySelectorAll('input[required], textarea[required], select[required]');
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
        }
    });

    const emailField = document.getElementById('email');
    if (!emailPattern.test(emailField.value)) {
        isValid = false;
        alert('Please enter a valid email address.');
    }

    const phoneField = document.getElementById('phone');
    if (!phonePattern.test(phoneField.value)) {
        isValid = false;
        alert('Please enter a valid phone number.');
    }

    return isValid;
}

function processData() {
    const formData = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        email: document.getElementById('email').value,
        address: document.getElementById('address').value,
        resume: document.getElementById('resume').value,
        coverLetter: document.getElementById('coverLetter').value,
        educationLevel: document.getElementById('educationLevel').value,
        university: document.getElementById('university').value,
        major: document.getElementById('major').value,
        graduationYear: document.getElementById('graduationYear').value,
        jobTitle: document.getElementById('jobTitle').value,
        companyName: document.getElementById('companyName').value,
        employmentDates: document.getElementById('employmentDates').value,
        jobResponsibilities: document.getElementById('jobResponsibilities').value,
        skills: document.getElementById('skills').value,
        certifications: document.getElementById('certifications').value,
        startDate: document.getElementById('startDate').value,
        workSchedule: document.getElementById('workSchedule').value,
        relocate: document.getElementById('relocate').checked,
        referenceName: document.getElementById('referenceName').value,
        referenceContact: document.getElementById('referenceContact').value,
        relationship: document.getElementById('relationship').value,
        whyWorkHere: document.getElementById('whyWorkHere').value,
        agreeTerms: document.getElementById('agreeTerms').checked,
        privacyPolicy: document.getElementById('privacyPolicy').checked,
    };
    applications.push(formData);
}

function viewApplications() {
    const prevTable = document.getElementsByTagName('table')
    console.log(prevTable)

    const tableContainer = document.createElement('div');
    tableContainer.classList.add('container');
    tableContainer.classList.add('applications');

    const table = document.createElement('table');
    const tableHeader = table.createTHead();
    const headerRow = tableHeader.insertRow();
    headerRow.innerHTML = '<th>Name</th><th>Email</th><th>Address</th>';
    
    applications.forEach(application => {
        const row = table.insertRow();
        row.innerHTML = `<td>${application.firstName} ${application.lastName}</td><td>${application.email}</td><td>${application.address}</td>`;
    });

    tableContainer.appendChild(table);
    document.body.appendChild(tableContainer);
}