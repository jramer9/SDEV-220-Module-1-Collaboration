from django.shortcuts import render


def student_form(request):
    """Display the student information form."""
    return render(request, 'students/form.html')


def student_results(request):
    """Handle form submission, validate, and display results."""
    # Only process POST requests
    if request.method != 'POST':
        return render(request, 'students/form.html')

    # Collect submitted values
    name = request.POST.get('student_name', '').strip()
    student_id = request.POST.get('student_id', '').strip()
    major = request.POST.get('major', '')
    standing = request.POST.get('standing', '')
    languages = request.POST.getlist('languages')  # checkboxes
    grad_year = request.POST.get('grad_year', '')
    comments = request.POST.get('comments', '').strip()

    # Validate required fields
    errors = []
    if not name:
        errors.append("Student Name cannot be blank.")
    if not student_id:
        errors.append("Student ID cannot be blank.")

    if errors:
        # Re-render the form with error messages and previously entered values
        context = {
            'errors': errors,
            'name': name,
            'student_id': student_id,
            'major': major,
            'standing': standing,
            'languages': languages,
            'grad_year': grad_year,
            'comments': comments,
        }
        return render(request, 'students/form.html', context)

    # Success – pass values to the results page
    context = {
        'name': name,
        'student_id': student_id,
        'major': major,
        'standing': standing,
        'languages': languages,
        'grad_year': grad_year,
        'comments': comments,
    }
    return render(request, 'students/results.html', context)