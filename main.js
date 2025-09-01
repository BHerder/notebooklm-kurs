// NotebookLM Kurs - Haupt-JavaScript

// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');
    
    if (mobileToggle && nav) {
        mobileToggle.addEventListener('click', function() {
            nav.classList.toggle('active');
        });
    }
    
    // Schließe Mobile Menu beim Klick auf einen Link
    const navLinks = document.querySelectorAll('.nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            nav.classList.remove('active');
        });
    });
});

// Fortschrittsverfolgung
class CourseProgress {
    constructor() {
        this.totalLessons = 7;
        this.currentLesson = this.getCurrentLessonFromURL();
        this.completedLessons = this.getCompletedLessons();
        this.updateProgressDisplay();
    }
    
    getCurrentLessonFromURL() {
        const path = window.location.pathname;
        const match = path.match(/lektion(\d+)\.html/);
        return match ? parseInt(match[1]) : 0;
    }
    
    getCompletedLessons() {
        const completed = localStorage.getItem('notebooklm-completed-lessons');
        return completed ? JSON.parse(completed) : [];
    }
    
    saveCompletedLessons() {
        localStorage.setItem('notebooklm-completed-lessons', JSON.stringify(this.completedLessons));
    }
    
    markLessonComplete(lessonNumber) {
        if (!this.completedLessons.includes(lessonNumber)) {
            this.completedLessons.push(lessonNumber);
            this.saveCompletedLessons();
            this.updateProgressDisplay();
        }
    }
    
    updateProgressDisplay() {
        const progressBar = document.querySelector('.progress-bar');
        const progressText = document.querySelector('.progress-text');
        
        if (progressBar) {
            const percentage = (this.completedLessons.length / this.totalLessons) * 100;
            progressBar.style.width = percentage + '%';
        }
        
        if (progressText) {
            progressText.textContent = `${this.completedLessons.length} von ${this.totalLessons} Lektionen abgeschlossen`;
        }
        
        // Update Lesson Navigation
        this.updateLessonNavigation();
    }
    
    updateLessonNavigation() {
        const lessonCards = document.querySelectorAll('.lesson-card');
        lessonCards.forEach((card, index) => {
            const lessonNumber = index + 1;
            if (this.completedLessons.includes(lessonNumber)) {
                card.classList.add('completed');
                const completedBadge = card.querySelector('.completed-badge');
                if (!completedBadge) {
                    const badge = document.createElement('div');
                    badge.className = 'completed-badge';
                    badge.innerHTML = '✓ Abgeschlossen';
                    card.appendChild(badge);
                }
            }
        });
    }
    
    getNextLesson() {
        return this.currentLesson < this.totalLessons ? this.currentLesson + 1 : null;
    }
    
    getPreviousLesson() {
        return this.currentLesson > 1 ? this.currentLesson - 1 : null;
    }
}

// Initialisiere Fortschrittsverfolgung
let courseProgress;
document.addEventListener('DOMContentLoaded', function() {
    courseProgress = new CourseProgress();
    
    // Mark Current Lesson Complete Button
    const completeButton = document.querySelector('.mark-complete-btn');
    if (completeButton) {
        completeButton.addEventListener('click', function() {
            const currentLesson = courseProgress.currentLesson;
            if (currentLesson > 0) {
                courseProgress.markLessonComplete(currentLesson);
                this.textContent = '✓ Abgeschlossen';
                this.disabled = true;
                this.classList.add('completed');
            }
        });
        
        // Check if current lesson is already completed
        if (courseProgress.completedLessons.includes(courseProgress.currentLesson)) {
            completeButton.textContent = '✓ Abgeschlossen';
            completeButton.disabled = true;
            completeButton.classList.add('completed');
        }
    }
});

// Smooth Scrolling für Anker-Links
document.addEventListener('DOMContentLoaded', function() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// FAQ Toggle Funktionalität
document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        if (question && answer) {
            question.addEventListener('click', function() {
                const isOpen = item.classList.contains('open');
                
                // Schließe alle anderen FAQ Items
                faqItems.forEach(otherItem => {
                    otherItem.classList.remove('open');
                });
                
                // Toggle current item
                if (!isOpen) {
                    item.classList.add('open');
                }
            });
        }
    });
});

// Scroll-to-Top Button
document.addEventListener('DOMContentLoaded', function() {
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '↑';
    scrollTopBtn.className = 'scroll-top-btn';
    scrollTopBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--light-blue) 100%);
        color: white;
        border: none;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
    `;
    
    document.body.appendChild(scrollTopBtn);
    
    // Show/Hide Button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollTopBtn.style.opacity = '1';
            scrollTopBtn.style.visibility = 'visible';
        } else {
            scrollTopBtn.style.opacity = '0';
            scrollTopBtn.style.visibility = 'hidden';
        }
    });
    
    // Scroll to top when clicked
    scrollTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Form Validation (für Kontaktformulare)
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('error');
            isValid = false;
        } else {
            field.classList.remove('error');
        }
    });
    
    // Email Validation
    const emailFields = form.querySelectorAll('input[type="email"]');
    emailFields.forEach(field => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (field.value && !emailRegex.test(field.value)) {
            field.classList.add('error');
            isValid = false;
        }
    });
    
    return isValid;
}

// Animation on Scroll
function animateOnScroll() {
    const elements = document.querySelectorAll('.fade-in-up');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('animate');
        }
    });
}

window.addEventListener('scroll', animateOnScroll);
document.addEventListener('DOMContentLoaded', animateOnScroll);

// Utility Functions
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 5px;
        color: white;
        font-weight: 500;
        z-index: 10000;
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.3s ease;
    `;
    
    if (type === 'success') {
        notification.style.backgroundColor = '#61ce70';
    } else if (type === 'error') {
        notification.style.backgroundColor = '#dc3545';
    } else if (type === 'info') {
        notification.style.backgroundColor = '#01baef';
    }
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Export für andere Module
window.CourseProgress = CourseProgress;
window.showNotification = showNotification;
window.validateForm = validateForm;

