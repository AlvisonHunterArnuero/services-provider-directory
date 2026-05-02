function showToast(message, type = 'alert-info') {
    let toastContainer = document.querySelector('.toast-container-custom');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast toast-top toast-end toast-container-custom z-50 mt-16';
        document.body.appendChild(toastContainer);
    }

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert ${type} shadow-lg`;
    alertDiv.innerHTML = `<span>${message}</span>`;

    toastContainer.appendChild(alertDiv);

    setTimeout(() => {
        alertDiv.style.opacity = '0';
        alertDiv.style.transition = 'opacity 0.5s ease';
        setTimeout(() => alertDiv.remove(), 500);
    }, 3000);
}

document.getElementById('review-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    
    // Extract the provider ID from the form's data attribute
    const proId = form.getAttribute('data-pro-id');

    // Find the selected rating
    const ratingInputs = form.querySelectorAll('input[name="rating"]');
    let rating = 5;
    for (const input of ratingInputs) {
        if (input.checked) {
            rating = parseInt(input.value);
            break;
        }
    }

    const data = {
        rating: rating,
        comment: formData.get('comment')
    };

    try {
        const response = await fetch(`/providers/${proId}/reviews`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            showToast('Review submitted successfully!', 'alert-success');
            setTimeout(() => window.location.reload(), 1500);
        } else {
            const errorData = await response.json();
            showToast(errorData.error || 'Failed to submit review', 'alert-error');
        }
    } catch (err) {
        console.error(err);
        showToast('An error occurred. Please try again.', 'alert-error');
    }
});
