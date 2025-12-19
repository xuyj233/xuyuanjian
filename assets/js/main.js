// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
  const tabButtons = document.querySelectorAll('.tab-button');
  const contentSections = document.querySelectorAll('.content-section');
  
  // Initially show only the "About Me" section
  contentSections.forEach(section => {
    if (section.id === 'about-me') {
      section.classList.add('active');
      section.style.display = 'block';
    } else {
      section.classList.remove('active');
      section.style.display = 'none';
    }
  });
  
  // Set initial active button
  tabButtons.forEach(button => {
    if (button.dataset.target === 'about-me') {
      button.classList.add('active');
    }
  });
  
  // Add click event listeners to tab buttons
  tabButtons.forEach(button => {
    button.addEventListener('click', function() {
      const targetId = this.dataset.target;
      
      // Remove active class from all buttons
      tabButtons.forEach(btn => btn.classList.remove('active'));
      
      // Add active class to clicked button
      this.classList.add('active');
      
      // Hide all content sections
      contentSections.forEach(section => {
        section.classList.remove('active');
        section.style.display = 'none';
      });
      
      // Show target content section
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        targetSection.classList.add('active');
        targetSection.style.display = 'block';
      }
    });
  });
});
