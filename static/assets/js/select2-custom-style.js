// select2-custom.js

// JavaScript object to hold custom styles for Select2
const select2Styles = {
    container: {
        width: '100%',  // Match the width of the container
    },
    selection: {
        fontSize: '1rem',
        borderColor: '#ebedf2',
        padding: '.6rem 1rem',
        height: 'inherit !important',
        borderWidth: '2px',
        borderRadius: 'var(--bs-border-radius)',
        backgroundColor: 'var(--bs-body-bg)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    rendered: {
        display: 'block',
        fontSize: '1rem',
        color: 'var(--bs-body-color)',
        lineHeight: '1.5',
        paddingRight: '2.25rem',
    },
    arrow: {
        display: 'none',  // Remove default arrow
    },
    dropdown: {
        fontSize: '1rem',
        padding: '.375rem 2.25rem .375rem .75rem',
        fontWeight: '400',
        lineHeight: '1.5',
        color: 'var(--bs-body-color)',
        backgroundColor: 'var(--bs-body-bg)',
        border: '2px solid #ebedf2',
        borderRadius: 'var(--bs-border-radius)',
        maxHeight: '200px',
        overflowY: 'auto',
        boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)', // Dropdown shadow
    },
    option: {
        padding: '.375rem',
        cursor: 'pointer',
    },
    highlightedOption: {
        backgroundColor: '#007bff',
        color: '#ffffff',
    },
    // Apply custom dropdown arrow using background-image
    dropdownArrow: {
        right: '0.75rem',
        top: '50%',
        transform: 'translateY(-50%)',
        width: '16px',
        height: '12px',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center center',
        backgroundSize: '16px 12px',
        display: 'block',
    }
};

// Function to apply the styles to Select2 elements
function applySelect2Styles() {
    // Apply styles to Select2 container
    $('.select2-container').css(select2Styles.container);

    // Apply styles to Select2 selection
    $('.select2-selection--single').css(select2Styles.selection);

    // Apply styles to rendered selection
    $('.select2-selection__rendered').css(select2Styles.rendered);

    // Remove the default arrow
    $('.select2-selection__arrow').css(select2Styles.arrow);

    // Apply styles to the dropdown
    $('.select2-dropdown').css(select2Styles.dropdown);

    // Apply styles to options
    $('.select2-results__option').css(select2Styles.option);

    // Apply styles to highlighted options
    $('.select2-results__option--highlighted').css(select2Styles.highlightedOption);

    // Apply custom dropdown arrow
    $('.select2-selection__arrow').css(select2Styles.dropdownArrow);
}

