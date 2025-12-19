// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
  console.log('Tab switching script loaded');
  
  const tabButtons = document.querySelectorAll('.tab-button');
  const contentSections = document.querySelectorAll('.content-section');
  
  console.log('Found', tabButtons.length, 'tab buttons');
  console.log('Found', contentSections.length, 'content sections');
  
  // Initially show only the "About Me" section
  contentSections.forEach(section => {
    console.log('Section ID:', section.id);
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
    button.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.dataset.target;
      
      console.log('Button clicked, target:', targetId);
      
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
        console.log('Showing section:', targetId);
        targetSection.classList.add('active');
        targetSection.style.display = 'block';
      } else {
        console.error('Target section not found:', targetId);
      }
    });
  });
  
  console.log('Tab switching initialized successfully');
});
