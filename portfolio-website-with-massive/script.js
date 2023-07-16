// script.js

// Function to add fade-in effect to elements
function fadeIn(element) {
    element.style.opacity = 0; // Start with opacity set to 0
    let opacity = 0;
    const interval = setInterval(() => {
      opacity += 0.01; // Increase opacity gradually
      element.style.opacity = opacity;
      if (opacity >= 1) {
        clearInterval(interval);
      }
    }, 10); // Adjust the interval to control the speed of the fade-in effect
  }
  
  // Function to animate project items on scroll
  function animateProjects() {
    const projects = document.querySelectorAll('.project');
  
    projects.forEach((project) => {
      if (isElementInViewport(project)) {
        fadeIn(project);
        project.style.transform = 'translateY(0)';
      }
    });
  }
  
  // Function to check if an element is in the viewport
  function isElementInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }
  
  // Event listener for scroll event to animate projects
  window.addEventListener('scroll', animateProjects);
  window.addEventListener('load', () => {
    fadeIn(document.body);
    animateProjects();
  });

// Function to get the current year. Used for copyright footer
document.getElementById("currentYear").textContent = new Date().getFullYear();

  