# Django TODO App - Bug Fixes Report

## Summary
Found and fixed 3 critical bugs in the Django TODO application codebase, focusing on security vulnerabilities, logic errors, and error handling issues.

## Bug #1: Security Vulnerability - Exposed SECRET_KEY
**Severity**: Critical
**Type**: Security Vulnerability
**Location**: `src/djangoproject/settings.py:22`

### Issue Description
The Django SECRET_KEY was hardcoded directly in the settings.py file and committed to version control. This is a critical security vulnerability because:
- The SECRET_KEY is used for cryptographic signing of sessions, cookies, and CSRF tokens
- Anyone with access to the repository can see the secret key
- This could lead to session hijacking, CSRF attacks, and other security breaches

### Original Code
```python
SECRET_KEY = 'gpltt35vwldy-3g1p4iyl8=dy95+jus#6=znvt8)9ncdn@&d*)'
```

### Fix Applied
```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key-change-in-production')
```

### Benefits of the Fix
- Secret key is now read from environment variables
- Default fallback key clearly indicates it's insecure and needs to be changed
- Follows Django security best practices
- Prevents accidental exposure in version control

---

## Bug #2: Logic Error - Incorrect Field Type in Forms
**Severity**: High
**Type**: Logic Error / Data Validation Issue
**Location**: `src/todo/forms.py:7`

### Issue Description
The TaskForm defined the 'due' field as a CharField, but the corresponding model field is a DateTimeField. This mismatch caused:
- Form validation failures when users enter dates
- Potential data corruption or type conversion errors
- Poor user experience with confusing error messages
- No proper date/time input widget for users

### Original Code
```python
due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
```

### Fix Applied
```python
due= forms.DateTimeField(
    widget= forms.DateTimeInput(attrs={
        'placeholder':'Due date (YYYY-MM-DD HH:MM)...', 
        'type': 'datetime-local'
    }), 
    label=False, 
    required=False
)
```

### Benefits of the Fix
- Field type now matches the model definition
- Proper datetime input widget with HTML5 datetime-local support
- Better user experience with date/time picker in modern browsers
- Proper validation of datetime input
- Clear placeholder text showing expected format

---

## Bug #3: Error Handling Issue - Missing Exception Handling
**Severity**: Medium
**Type**: Error Handling / User Experience
**Location**: `src/todo/views.py:21, 36`

### Issue Description
The updateTask and deleteTask views used `task.objects.get(id=pk)` without exception handling. This caused:
- 500 Internal Server Error when accessing non-existent tasks
- Poor user experience with generic error pages
- No proper 404 handling for missing resources
- Potential information disclosure through error messages

### Original Code
```python
def updateTask(request, pk):
    queryset = task.objects.get(id=pk)  # Can raise DoesNotExist exception

def deleteTask(request, pk):
    queryset = task.objects.get(id=pk)  # Can raise DoesNotExist exception
```

### Fix Applied
```python
from django.shortcuts import render, redirect, get_object_or_404

def updateTask(request, pk):
    queryset = get_object_or_404(task, id=pk)

def deleteTask(request, pk):
    queryset = get_object_or_404(task, id=pk)
```

### Benefits of the Fix
- Proper 404 responses for non-existent tasks
- Better user experience with appropriate error handling
- Follows Django best practices for object retrieval
- Prevents 500 errors and improves application stability
- More secure by not exposing internal error details

---

## Additional Issues Identified (Not Fixed)

### Model Naming Convention
The model class 'task' should follow Python naming conventions and be 'Task' (PascalCase). This affects readability and follows PEP 8 standards.

### Potential Performance Issues
The listTask view could benefit from query optimization and proper indexing, especially as the dataset grows.

---

## Recommendations for Further Improvements

1. **Environment Configuration**: Set up proper environment configuration files (.env) for different deployment environments
2. **Input Validation**: Add more robust input validation and sanitization
3. **Authentication**: Consider adding user authentication if this will be a multi-user application
4. **Testing**: Add comprehensive unit and integration tests
5. **Logging**: Implement proper logging for debugging and monitoring
6. **CSRF Protection**: Ensure all forms have proper CSRF protection (already present in Django by default)

---

## Verification Steps

To verify these fixes:

1. **Security Fix**: Set the DJANGO_SECRET_KEY environment variable before running the application
2. **Form Fix**: Test creating tasks with due dates to ensure proper datetime handling
3. **Error Handling Fix**: Try accessing non-existent task URLs (e.g., `/update_task/999/`) to verify 404 responses

These fixes significantly improve the security, reliability, and user experience of the Django TODO application.