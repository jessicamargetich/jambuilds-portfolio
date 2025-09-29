// Main JavaScript file for jambuilds.com portfolio

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initNavigation();
    initSmoothScrolling();
    initAnimations();
    initFormHandling();
    initAccessibility();
    initBlogFilters();
    initParallaxScrolling();
});

// Navigation functionality
function initNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('active');
        });

        // Close mobile menu when clicking nav links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Add scroll effect to navigation
    let lastScrollTop = 0;
    const header = document.querySelector('.header');

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            header.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            header.style.transform = 'translateY(0)';
        }

        lastScrollTop = scrollTop;
    });
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Animation and intersection observer
function initAnimations() {
    // Fade in animation for elements
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll(
        '.highlight-card, .project-card, .experience-item, .blog-post, .contact-card, .topic-card, .approach-item'
    );

    animateElements.forEach(el => {
        observer.observe(el);
    });

    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        .highlight-card, .project-card, .experience-item, .blog-post, .contact-card, .topic-card, .approach-item {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }

        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }

        .header {
            transition: transform 0.3s ease;
        }
    `;
    document.head.appendChild(style);
}

// Form handling
function initFormHandling() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', handleContactForm);

        // Real-time validation
        const inputs = contactForm.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', validateField);
            input.addEventListener('input', clearErrors);
        });
    }
}

function handleContactForm(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    // Validate form
    if (!validateForm(form)) {
        showFormMessage('Please fix the errors below.', 'error');
        return;
    }

    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    // Simulate form submission (replace with actual endpoint)
    setTimeout(() => {
        showFormMessage('Thank you for your message! I\'ll get back to you within 24 hours.', 'success');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 1500);
}

function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');

    requiredFields.forEach(field => {
        if (!validateField({ target: field })) {
            isValid = false;
        }
    });

    return isValid;
}

function validateField(e) {
    const field = e.target;
    const value = field.value.trim();
    let isValid = true;

    // Remove existing error styling
    field.classList.remove('error');
    removeFieldError(field);

    // Required field validation
    if (field.hasAttribute('required') && !value) {
        showFieldError(field, 'This field is required');
        isValid = false;
    }

    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Please enter a valid email address');
            isValid = false;
        }
    }

    // Message length validation
    if (field.name === 'message' && value && value.length < 10) {
        showFieldError(field, 'Message must be at least 10 characters long');
        isValid = false;
    }

    if (!isValid) {
        field.classList.add('error');
    }

    return isValid;
}

function showFieldError(field, message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'field-error';
    errorElement.textContent = message;
    errorElement.style.color = 'var(--error-color)';
    errorElement.style.fontSize = '0.875rem';
    errorElement.style.marginTop = 'var(--spacing-1)';

    field.parentNode.appendChild(errorElement);
}

function removeFieldError(field) {
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
}

function clearErrors(e) {
    const field = e.target;
    field.classList.remove('error');
    removeFieldError(field);
}

function showFormMessage(message, type) {
    const form = document.getElementById('contactForm');

    // Remove existing messages
    const existingMessage = form.querySelector('.form-message');
    if (existingMessage) {
        existingMessage.remove();
    }

    // Create new message
    const messageDiv = document.createElement('div');
    messageDiv.className = `form-message ${type}`;
    messageDiv.textContent = message;

    // Insert at the top of the form
    form.insertBefore(messageDiv, form.firstChild);

    // Auto-remove success messages
    if (type === 'success') {
        setTimeout(() => {
            if (messageDiv.parentNode) {
                messageDiv.remove();
            }
        }, 5000);
    }

    // Scroll to message
    messageDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Accessibility improvements
function initAccessibility() {
    // Skip link functionality
    const skipLink = document.querySelector('.skip-link');
    if (skipLink) {
        skipLink.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector('#main-content');
            if (target) {
                target.focus();
                target.scrollIntoView();
            }
        });
    }

    // Keyboard navigation for cards
    const cards = document.querySelectorAll('.project-card, .highlight-card, .topic-card');
    cards.forEach(card => {
        card.setAttribute('tabindex', '0');

        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const link = card.querySelector('a, button');
                if (link) {
                    link.click();
                }
            }
        });
    });

    // Improve focus visibility
    const style = document.createElement('style');
    style.textContent = `
        *:focus {
            outline: 2px solid var(--primary-color);
            outline-offset: 2px;
        }

        .nav-link:focus,
        .btn:focus {
            outline: 2px solid var(--white);
            outline-offset: 2px;
        }
    `;
    document.head.appendChild(style);
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Performance monitoring
function initPerformanceMonitoring() {
    // Log page load performance
    window.addEventListener('load', function() {
        setTimeout(() => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart + 'ms');
        }, 0);
    });
}

// Initialize performance monitoring
initPerformanceMonitoring();

// Blog filtering functionality
function initBlogFilters() {
    const postsContainer = document.getElementById('posts-container');
    const visibleCountElement = document.getElementById('visible-count');
    const noResultsElement = document.getElementById('no-results');
    const clearFiltersBtn = document.getElementById('clear-filters');
    const selectAllFiltersBtn = document.getElementById('select-all-filters');

    if (!postsContainer) return; // Not on blog page

    const posts = Array.from(postsContainer.querySelectorAll('.blog-post'));
    const allCheckboxes = document.querySelectorAll('.filter-checkbox input[type="checkbox"]');
    const postModal = document.getElementById('post-modal');

    // Initialize filter functionality
    allCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterPosts);
    });

    clearFiltersBtn?.addEventListener('click', clearAllFilters);
    selectAllFiltersBtn?.addEventListener('click', selectAllFilters);

    // Initialize post modals
    initPostModals();

    function filterPosts() {
        const activeFilters = getActiveFilters();
        let visibleCount = 0;

        posts.forEach(post => {
            const shouldShow = matchesFilters(post, activeFilters);
            post.style.display = shouldShow ? 'block' : 'none';
            if (shouldShow) visibleCount++;
        });

        updateVisibleCount(visibleCount);
        showNoResultsMessage(visibleCount === 0);
    }

    function getActiveFilters() {
        const filters = {
            years: [],
            formats: [],
            themes: []
        };

        document.querySelectorAll('input[data-filter="year"]:checked').forEach(checkbox => {
            filters.years.push(checkbox.value);
        });

        document.querySelectorAll('input[data-filter="format"]:checked').forEach(checkbox => {
            filters.formats.push(checkbox.value);
        });

        document.querySelectorAll('input[data-filter="theme"]:checked').forEach(checkbox => {
            filters.themes.push(checkbox.value);
        });

        return filters;
    }

    function matchesFilters(post, filters) {
        const postYear = post.dataset.year;
        const postFormats = post.dataset.formats.split(',');
        const postThemes = post.dataset.themes.split(',');

        // Check if post matches year filter
        const yearMatch = filters.years.length === 0 || filters.years.includes(postYear);

        // Check if post matches format filter
        const formatMatch = filters.formats.length === 0 ||
                           postFormats.some(format => filters.formats.includes(format));

        // Check if post matches theme filter
        const themeMatch = filters.themes.length === 0 ||
                          postThemes.some(theme => filters.themes.includes(theme));

        return yearMatch && formatMatch && themeMatch;
    }

    function clearAllFilters() {
        allCheckboxes.forEach(checkbox => {
            checkbox.checked = false;
        });
        filterPosts();
    }

    function selectAllFilters() {
        allCheckboxes.forEach(checkbox => {
            checkbox.checked = true;
        });
        filterPosts();
    }

    function updateVisibleCount(count) {
        if (visibleCountElement) {
            visibleCountElement.textContent = count;
        }
    }

    function showNoResultsMessage(show) {
        if (noResultsElement) {
            noResultsElement.style.display = show ? 'block' : 'none';
        }
        if (postsContainer) {
            postsContainer.style.display = show ? 'none' : 'grid';
        }
    }

    function initPostModals() {
        // Get blog posts data from the template (need to make this available globally)
        const readMoreButtons = document.querySelectorAll('.read-more-btn');
        const modalCloseBtn = document.querySelector('.modal-close');

        readMoreButtons.forEach(button => {
            button.addEventListener('click', openPostModal);
        });

        modalCloseBtn?.addEventListener('click', closePostModal);

        // Close modal when clicking outside
        postModal?.addEventListener('click', function(e) {
            if (e.target === postModal) {
                closePostModal();
            }
        });

        // Close modal with Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && postModal?.getAttribute('aria-hidden') === 'false') {
                closePostModal();
            }
        });
    }

    function openPostModal(e) {
        const postId = e.target.dataset.postId;
        const post = posts.find(p => p.querySelector(`[data-post-id="${postId}"]`));

        if (!post || !postModal) return;

        // Get post data
        const title = post.querySelector('.post-title').textContent;
        const date = post.querySelector('time').getAttribute('datetime');
        const readTime = post.querySelector('.post-read-time').textContent;
        const formats = Array.from(post.querySelectorAll('.format-tag')).map(tag => tag.textContent);
        const themes = Array.from(post.querySelectorAll('.theme-tag')).map(tag => tag.textContent);

        // Populate modal (content would need to be stored in data attributes or fetched)
        document.querySelector('.modal-post-title').textContent = title;
        document.querySelector('.modal-date').textContent = formatDate(date);
        document.querySelector('.modal-read-time').textContent = readTime;

        // Build tags HTML
        const tagsHTML = [
            ...formats.map(format => `<span class="tag format-tag">${format}</span>`),
            ...themes.map(theme => `<span class="tag theme-tag">${theme}</span>`)
        ].join('');
        document.querySelector('.modal-tags').innerHTML = tagsHTML;

        // For now, show placeholder content (in a real implementation, this would load the full post content)
        document.querySelector('.modal-content-body').innerHTML = `
            <p><em>Full article content would be displayed here.</em></p>
            <p>This is a placeholder for the complete article content. In the actual implementation,
            the full post content would be loaded and displayed here with proper formatting,
            images, and interactive elements.</p>
        `;

        // Show modal
        postModal.setAttribute('aria-hidden', 'false');
        postModal.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        // Focus management
        document.querySelector('.modal-close').focus();
    }

    function closePostModal() {
        if (!postModal) return;

        postModal.setAttribute('aria-hidden', 'true');
        postModal.style.display = 'none';
        document.body.style.overflow = '';
    }

    function formatDate(dateString) {
        const date = new Date(dateString);
        const day = date.getDate();
        const month = date.toLocaleDateString('en-US', { month: 'long' });
        const year = date.getFullYear();
        return `${day} ${month} ${year}`;
    }
}

// Parallax scrolling for timeline
function initParallaxScrolling() {
    const parallaxItems = document.querySelectorAll('.parallax-item');
    const parallaxMarkers = document.querySelectorAll('.parallax-marker');

    if (parallaxItems.length === 0) return; // Not on timeline page

    let ticking = false;

    function updateParallax() {
        const scrollTop = window.pageYOffset;
        const windowHeight = window.innerHeight;

        // Update parallax items
        parallaxItems.forEach(item => {
            const rect = item.getBoundingClientRect();
            const speed = parseFloat(item.dataset.speed) || 0.5;

            // Check if element is in viewport
            if (rect.bottom >= 0 && rect.top <= windowHeight) {
                const yPos = -(scrollTop * speed);
                item.style.transform = `translate3d(0, ${yPos}px, 0)`;
            }
        });

        // Update parallax markers with different speeds
        parallaxMarkers.forEach(marker => {
            const rect = marker.getBoundingClientRect();
            const speed = parseFloat(marker.dataset.speed) || 0.3;

            // Check if element is in viewport
            if (rect.bottom >= 0 && rect.top <= windowHeight) {
                const yPos = -(scrollTop * speed);
                marker.style.transform = `translate3d(0, ${yPos}px, 0)`;
            }
        });

        ticking = false;
    }

    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    }

    // Add scroll event listener with debouncing
    window.addEventListener('scroll', requestTick, { passive: true });

    // Initial call
    updateParallax();

    // Add intersection observer for better performance
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('parallax-active');
            } else {
                entry.target.classList.remove('parallax-active');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px 0px'
    });

    // Observe all parallax elements
    [...parallaxItems, ...parallaxMarkers].forEach(element => {
        observer.observe(element);
    });
}

// Export functions for potential external use
window.portfolioUtils = {
    showFormMessage,
    validateField,
    debounce
};