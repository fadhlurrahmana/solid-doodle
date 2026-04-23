document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const humanPhotoInput = document.getElementById('human_photo');
    const productPhotoInput = document.getElementById('product_photo');
    const humanPreview = document.getElementById('human_preview');
    const productPreview = document.getElementById('product_preview');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.querySelector('.btn-loader');
    const resultSection = document.getElementById('resultSection');
    const resultPreview = document.getElementById('resultPreview');
    const downloadBtn = document.getElementById('downloadBtn');
    const newPromoBtn = document.getElementById('newPromoBtn');
    const alertBox = document.getElementById('alertBox');

    let currentOutputFile = '';

    // Preview uploaded images
    humanPhotoInput.addEventListener('change', function(e) {
        previewImage(e.target.files[0], humanPreview);
    });

    productPhotoInput.addEventListener('change', function(e) {
        previewImage(e.target.files[0], productPreview);
    });

    function previewImage(file, previewElement) {
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewElement.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
            };
            reader.readAsDataURL(file);
        }
    }

    // Handle form submission
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Disable button and show loader
        submitBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline';

        const formData = new FormData(uploadForm);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok && data.success) {
                currentOutputFile = data.output_file;
                showResult(data.output_file);
                showAlert(data.message, 'success');
            } else {
                showAlert(data.error || 'Terjadi kesalahan saat memproses.', 'error');
            }
        } catch (error) {
            showAlert('Terjadi kesalahan jaringan: ' + error.message, 'error');
        } finally {
            // Re-enable button
            submitBtn.disabled = false;
            btnText.style.display = 'inline';
            btnLoader.style.display = 'none';
        }
    });

    function showResult(filename) {
        const outputType = document.getElementById('output_type').value;
        
        if (outputType === 'video') {
            resultPreview.innerHTML = `
                <video controls autoplay loop>
                    <source src="/preview/${filename}" type="video/mp4">
                    Browser Anda tidak mendukung tag video.
                </video>
            `;
        } else {
            resultPreview.innerHTML = `
                <img src="/preview/${filename}?${Date.now()}" alt="Promo Result">
            `;
        }

        resultSection.style.display = 'block';
        resultSection.scrollIntoView({ behavior: 'smooth' });
    }

    downloadBtn.addEventListener('click', function() {
        if (currentOutputFile) {
            window.location.href = `/download/${currentOutputFile}`;
        }
    });

    newPromoBtn.addEventListener('click', function() {
        // Reset form
        uploadForm.reset();
        humanPreview.innerHTML = '';
        productPreview.innerHTML = '';
        resultSection.style.display = 'none';
        alertBox.style.display = 'none';
        currentOutputFile = '';
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    function showAlert(message, type) {
        alertBox.textContent = message;
        alertBox.className = `alert ${type}`;
        alertBox.style.display = 'block';

        // Auto hide after 5 seconds
        setTimeout(() => {
            alertBox.style.display = 'none';
        }, 5000);
    }
});
