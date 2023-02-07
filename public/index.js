'use strict';
(function () {

  window.addEventListener('load', init);

  /**
   * Initialization function that should handle anything that needs to occur
   * on page load (include changing from one page to another).
   */
  function init() {
    const template = document.getElementById('template');
    const list = document.getElementById('events');

    if (template) {
      // events is a list found in events.js
      for (let i = 0; i < events.length; i++) {
        const node = template.cloneNode(true);
  
        node.id = "";
        node.querySelector('img').src = events[i].img;
        node.querySelector('h4').innerText = events[i].title;
        node.querySelector('p').innerText = events[i].date;
  
        list.appendChild(node);
      }
    }

    const submit = document.getElementById('contact-submit');
    if (submit) {
      submit.addEventListener('click', function() {
        const subject = document.getElementById('form-subject').value;
        const body = document.getElementById('form-body').value;
        window.open(
          `mailto:datina.ensemble@gmail.com?subject=${subject}&body=${body}`,
          '_blank'
        );
      });
    }

    // The scroll top button should work even without js enabled so it uses
    // an anchor, however that appends an ugly '#scroll-top' to the url so
    // for users with js enabled, we do this:
    const scroll_btn = document.getElementById('scroll-top-button');
    scroll_btn.addEventListener('click', (evt) => {
      window.scrollTo({top: '0'});
      evt.preventDefault();
    });
  }
})();