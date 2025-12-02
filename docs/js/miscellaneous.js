'use strict';

// Hide Table of Content items whose related paragraph has the 'no-toc' class
function hideTocItems() {
  document.querySelectorAll('[aria-label="On this page"] .md-nav__item').forEach(item => {
    let paragraph_id = item.querySelector('a')?.href.split('#')[1];
    let paragraph = document.getElementById(paragraph_id)
    if (paragraph?.classList.contains('no-toc')) {
      item.style.display = 'none'
    }
  });
}

/*
  Add functionality to tabs 
*/
function tabFunctionality() {
  // === Helpers ===
  function getTabIDFromStorage(label) {
    return sessionStorage.getItem(`tabs-label=${label}`) ?? null;
  }
  
  function getTabButtons(label, index = null) {
    let query = `.tabLabels[label=${label}] > button` 
    if (!!index) query += `:nth-child(${index})`
    return document.querySelectorAll(query);
  }

  function getTabContents(label) {
    const tabContents = Array.from(document.querySelectorAll('[tabcontentfor]')).filter(el => {
      const targetId = el.getAttribute('tabcontentfor').split(' ')[0];
      const targetElement = document.getElementById(targetId);
      if (!targetElement) return false;
      const parent = targetElement.parentElement;
      return parent && parent.getAttribute('label') === label;
    });
    return tabContents;
  }

  function isAssociatedWithActiveTab(elem) {
    // More than one tab can be associated with the same content block 
    // (e.g. tabcontentfor="tab1 tab2")
    const tabIDs = elem.getAttribute('tabcontentfor').split(' ');
    return tabIDs.some(tabID => {
      const tab = document.getElementById(tabID);
      return tab && tab.classList.contains('activeTab');
    });
  }

  function openTab(tab, updateURL = true) {
    // Get the label of the tab and its index
    const label = tab.parentElement.getAttribute('label');
    const index = Array.from(tab.parentElement.children).indexOf(tab) + 1;

    // Deselect all tabs from tabLabels with the associated label
    getTabButtons(label).forEach(btn => btn.classList.remove('activeTab'));

    // Hide content blocks for all tabLabels with the associated label
    getTabContents(label).forEach(elem => {
      elem.classList.remove('activeContent');
    });

    // Select tabs with the same index of the select one in all tabLabels with the associated label
    getTabButtons(label, index).forEach(elem => {
      elem.classList.add('activeTab');
    });

    // Show content blocks associated with the specific tab
    getTabContents(label).forEach(elem => {
      if (isAssociatedWithActiveTab(elem)) {
        elem.classList.add('activeContent');
      }
    });

    // Update URL anchor
    if (updateURL) {
      history.pushState(null, null, `#${tab.id}`);
    }
    // Save active tab in sessionStorage
    sessionStorage.setItem(`tabs-label=${label}`, tab.id);
  }

  function getTabToOpen(tabLabels) {
    const label = tabLabels.getAttribute("label");
    const tabID = getTabIDFromStorage(label) ?? tabLabels?.firstElementChild?.id
    return document.getElementById(tabID)
  }
  
  function openTabsOnPageLoad() {
    let tabsToOpen = []
    let checkedLabel = null;
    // Select tab associated with anchor if present
    const hash = window.location.hash;
    if (hash) {
      const element = document.getElementById(hash.slice(1));
      const tabLabelContainer = element?.parentElement;
      if (tabLabelContainer?.classList.contains("tabLabels")) {
        checkedLabel = tabLabelContainer.getAttribute("label");
        tabsToOpen.push(element);
      }
    }
    // Find a tab to open for each .tabLabels that isn't already opened
    document.querySelectorAll(`.tabLabels:not([label="${checkedLabel}"])`)
      .forEach(tabLabels => {
        const tab = getTabToOpen(tabLabels);
        if (tab) tabsToOpen.push(tab);
      });
    // Open tabs
    tabsToOpen.forEach(tab => {
        openTab(tab, false);
    });
  }

  // Open tabs when the page is loaded
  openTabsOnPageLoad();

  // Open tabs when clicked on them 
  // (Add click listeners to tab buttons)
  document.querySelectorAll(".tabLabels > button").forEach(button => {
    button.addEventListener("click", e => openTab(e.currentTarget));
  });

  // Open tabs when linked to with an anchor link in same page
  // (Add click listeners to anchor links pointing to tab IDs)
  document.querySelectorAll('[href^="#"]:not([class^="md"])').forEach(el => {
    const href = el.getAttribute('href');
    const tabEl = document.getElementById(href.slice(1));
    if (tabEl?.parentElement.classList.contains("tabLabels")) {
      el.addEventListener("click", () => openTab(tabEl), false);
    }
  });
}

/*
  Make links that go to a different website 'external' by adding the
  target="_blank" attribute, and add an external-link icon to them.
*/
function makeLinksExternal() {
  const externalLinkClass = "external-link";
  const currentHost = location.hostname;
  const excludedClasses = ['.vertical-card', '.horizontal-card', '.text-card', '.md-icon'];
  document.querySelectorAll("a[href^='http']")
    .forEach(link => {
      const url = new URL(link.href);
      // Skip internal links (same hostname)
      if (url.hostname === currentHost) {
        return;
      }
      // Make link external (open in new tab)
      link.setAttribute('target','_blank');
      link.setAttribute('rel','noopener');
      
      // Add external-link class only if inside the article element, and not inside 
      // any element having one of the excluded classes
      if (
        link.closest('article') &&
        !link.closest(excludedClasses.join(', '))
      ) {
        link.classList.add(externalLinkClass);
      }
    });
}


/*
  Add button to toggle terminal-animations for the whole page (next to the page title)
*/
function toggleTerminalAnimations(){
  
  // If the current document consists of terminal-window, then 
  // execute the following code.
  if (document.querySelector('terminal-window')) {
    
    // Cookie text in local storage for retrieving whether
    // terminal animation is toggled on or off by the user
    const COOKIE_TEXT = 'ACCESS-Hive-Docs-animated-terminal-state';

    // GETTER: Get the current state of the toggle button.
    // If there is no COOKIE_TEXT in local storage, then 
    // the state is active by default.
    function getCookieState() {
      return localStorage.getItem(COOKIE_TEXT) || 'active';
    }

    // SETTER: Set the current state when the button is pressed.
    function setCookieState(state) {
      localStorage.setItem(COOKIE_TEXT, state);
    }

    // Change the terminal state to static or animated.
    function changeTerminalState(state) {
      let terminalWindows = document.querySelectorAll('terminal-window')

      // If the new state is active, then make the terminal
      // as active by removing the static attribute.
      // And vice versa in the else block.
      if (state == 'active') {
        terminalWindows.forEach(t => {
          t.removeAttribute('static');
        })
      } else {
        terminalWindows.forEach(t => {
          t.setAttribute('static','')
        })
      }
    }

    function toggleState(state) {
      // If the current state is active, set toggled state to inactive.
      // And vice versa.
      const toggledState = getState() === 'active' ? 'inactive' : 'active';

      // Change the state of terminal
      changeTerminalState(toggledState)

      // Save the new state in cookies - local storage
      setCookieState(newstate)
    }

    let state = getCookieState()
    toggleState(state)
  }
} 

function toggleTerminalAnimations2() {
    if (document.querySelector('terminal-window')) {
        const COOKIE_TEXT = 'ACCESS-Hive-Docs-animated-terminal-state';
        const SWITCH_IMG = '/assets/terminal_animation_switch.png';
        const SWITCH_IMG_INACTIVE = '/assets/terminal_animation_switch_inactive.png';
        
        function getState() {
            return localStorage.getItem(COOKIE_TEXT) || 'active';
        }

        function setStateCookie(state) {
            localStorage.setItem(COOKIE_TEXT, state);
        }
        
        function setSwitchIcon(element, state) {
            if (state === 'active') {
                element.classList.add('hidden');
            } else {
                element.classList.remove('hidden');
            }
        }
        
        function applyStateToTerminalWindows(state) {
            let terminalWindows = document.querySelectorAll('terminal-window');
            if (state === 'active') {
                terminalWindows.forEach(t => {
                    t.removeAttribute('static');
                })
            } else {
                terminalWindows.forEach(t => {
                    t.setAttribute('static',"");
                })
            }
        }

        function applyState(container, state) {
            // Change the switch icon and title            
            setSwitchIcon(container.children[1], state);
            setSwitchTooltipText(container.querySelector('.terminal-switch-tooltip'), state);
            // Apply the state to terminal windows
            applyStateToTerminalWindows(state);
        }
        
        function setSwitchTooltipText(element, state) {
            let word = state === 'active' ? 'disable' : 'enable';
            element.innerHTML = `
            Terminal animations are <b>${state}</b>. Click to ${word} them.<br><br>
            In this documentation, the same code is sometimes shown in a <b>code block</b> 
            and also as a <b>terminal animation</b>.<br>
            The <b>code blocks</b> show the commands to be run in a terminal. They can be easily copied
            by clicking on the icon over the right side of the code block.<br>
            The <b>terminal animations</b> are produced using 
            <a href="https://github.com/atteggiani/animated-terminal.js" target="_blank" rel="noopener noreferrer" 
                class="external-link">animated-terminal.js</a>
            and provide examples of the output to expect when the commands are run. 
            Sometimes they might slightly differ from the actual outputs.
            `
        }

        function toggleState(event) {
            const newstate = getState() === 'active' ? 'inactive' : 'active';
            applyState(event.currentTarget, newstate);
            setStateCookie(newstate);
        }

        // Create the Animation switch
        const terminalAnimationsSwitch = document.createElement('img');
        terminalAnimationsSwitch.setAttribute('src',SWITCH_IMG);
        terminalAnimationsSwitch.classList.add('terminal-switch');
        const terminalAnimationsSwitchInactive = document.createElement('img');
        terminalAnimationsSwitchInactive.classList.add('terminal-switch');
        terminalAnimationsSwitchInactive.setAttribute('src',SWITCH_IMG_INACTIVE);
        // Create the Animation Switch tooltip
        const terminalAnimationsTooltip = document.createElement('div');
        terminalAnimationsTooltip.classList.add('terminal-switch-tooltip');
        terminalAnimationsTooltip.addEventListener("mouseenter", (event) => {
            terminalAnimationsTooltip.classList.add('visible');
        });
        terminalAnimationsTooltip.addEventListener("mouseleave", (event) => {
            terminalAnimationsTooltip.classList.remove('visible');
        });
        // Create the Animation Switch Container
        const terminalAnimationsSwitchContainer = document.createElement('div');
        terminalAnimationsSwitchContainer.classList.add('terminal-switch-container');
        terminalAnimationsSwitchContainer.appendChild(terminalAnimationsSwitch);
        terminalAnimationsSwitchContainer.appendChild(terminalAnimationsSwitchInactive);
        terminalAnimationsSwitchContainer.appendChild(terminalAnimationsTooltip);
        terminalAnimationsSwitchContainer.addEventListener('click', toggleState, false);
        let state = getState();
        applyState(terminalAnimationsSwitchContainer, state);
        // Place the Animation switch within the document
        // const h1 = document.querySelector('h1');
        // console.log("hi")
        // h1.parentElement.insertBefore(terminalAnimationsSwitchContainer, h1);
        console.log("hi");
        const searchbar = document.querySelector('.md-search');
        console.log("hi");
        console.log(searchbar)
        searchbar.before(terminalAnimationsSwitchContainer);
    }
}

/*
  Fit text to div if overflowing (for 'card-text-container' and 'fitText' class)
*/
function fitText() {
  const coeff = 0.9;
  const minSize = 8;
  function isOverflowing(el) {
    return el.scrollHeight > el.clientHeight || el.scrollWidth > el.clientWidth;
  }
  function fit(el) {
    el.style.fontSize = null;
    let size = parseFloat(getComputedStyle(el).fontSize);
    while (isOverflowing(el) && size > minSize) {
      size *= coeff;
      el.style.fontSize = `${size}px`;
    }
  }
  const observer = new ResizeObserver(entries => {
    entries.forEach(entry => fit(entry.target));
  })
  document.querySelectorAll('.card-text-container,.fit-text').forEach(el => {
    observer.observe(el);
  })
}


/*
  Make footnote citations link to article
*/
function makeCitationLinks() {
  let match;
  let href;
  document.querySelectorAll('.footnote [id^="fn:"] > p').forEach(el => {
    if (match = el.innerHTML.match('<a\\s*href="https://doi.org/[\\w\./-]*')) { // Assignment to variable NOT AN ERROR!
      href = match[0].slice(9,);
      el.outerHTML = `<a href="${href}" target="_blank">${el.innerHTML}</a>`;
    } else if (match = el.innerHTML.match('URL: <a href="[\\w\./:-]*')) {
      href = match[0].slice(14,);
      el.outerHTML = `<a href="${href}" target="_blank">${el.innerHTML}</a>`;
    }
  })
}

// Join all functions
function main() {
  hideTocItems();
  tabFunctionality();
  makeLinksExternal();
  fitText();
  toggleTerminalAnimations();
  makeCitationLinks();
}

// Run all functions after every navigation event
if (typeof document$ !== 'undefined') {
    // The `document$` is a special observable enabled by the navigation.instant plugin (in mkdocs.yaml)
    document$.subscribe(() => main());
} else {
    // If navigation.instant plugin is not active
    window.addEventListener('load', main);
}